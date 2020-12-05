
import io
import random
import numpy as np
import paddle
import paddle.fluid as fluid
from paddle.fluid.dygraph.nn import Conv2D, Pool2D, Linear, Embedding
from paddle.fluid.dygraph.base import to_variable
import sys

def data_reader(file_path, word_dict, phrase, epoch, shuffle=False):
    unk_id = len(word_dict)
    all_data = []
    with io.open(file_path, "r", encoding='utf8') as fin:
        for line in fin:
            cols = line.strip().split("\t")
            if len(cols) != 2:
                sys.stderr.write("[NOTICE] Error Format Line!")
                continue
            label = int(cols[1])
            wids = cols[0].split(",")
            all_data.append((wids, label))

    if shuffle:
        if phrase == "train":
            random.shuffle(all_data)

    def reader():
        for epoch_index in range(epoch):
            for doc, label in all_data:
                yield doc, label

    return reader


def load_vocab(file_path):
    vocab = {}
    with io.open(file_path, 'r', encoding='utf-8') as f:
        wid = 0
        for line in f:
            if line.strip() not in vocab:
                vocab[line.strip()] = wid
                wid += 1
    vocab["<unk>"] = len(vocab)
    return vocab


class SentaProcessor(object):
    def __init__(self, data_dir, vocab_path):
        self.data_dir = data_dir
        self.vocab = load_vocab(vocab_path)

    def get_train_data(self, data_dir, epoch, shuffle):
        return data_reader((self.data_dir + "train_list.txt"), self.vocab,
                           "train", epoch, shuffle)

    def get_eval_data(self, data_dir, epoch, shuffle):
        return data_reader((self.data_dir + "eval_list.txt"), self.vocab,
                           "dev", epoch, shuffle)

    def data_generator(self, batch_size, phase='train', epoch=1, shuffle=True):
        if phase == "train":
            return paddle.batch(
                self.get_train_data(self.data_dir, epoch, shuffle),
                batch_size,
                drop_last=True)
        elif phase == "eval":
            return paddle.batch(
                self.get_eval_data(self.data_dir, epoch, shuffle),
                batch_size,
                drop_last=True)
        else:
            raise ValueError(
                "Unknown phase, which should be in ['train', 'eval'].")


class SimpleConvPool(fluid.dygraph.Layer):
    def __init__(self,
                 num_channels,
                 num_filters,
                 filter_size,
                 batch_size=None):
        super(SimpleConvPool, self).__init__()
        self.batch_size = batch_size
        self._conv2d = Conv2D(num_channels=num_channels,
                              num_filters=num_filters,
                              filter_size=filter_size,
                              padding=[1, 1],
                              act='tanh')

    def forward(self, inputs):
        x = self._conv2d(inputs)
        x = fluid.layers.reduce_max(x, dim=-1)
        x = fluid.layers.reshape(x, shape=[self.batch_size, -1])
        return x


class CNN(fluid.dygraph.Layer):
    def __init__(self):
        super(CNN, self).__init__()
        self.dict_dim = train_parameters["vocab_size"]
        self.emb_dim = 128
        self.hid_dim = 128
        self.fc_hid_dim = 96
        self.class_dim = 2
        self.channels = 1
        self.win_size = [3, self.hid_dim]
        self.batch_size = train_parameters["batch_size"]
        self.seq_len = train_parameters["padding_size"]
        self.embedding = Embedding(
            size=[self.dict_dim + 1, self.emb_dim],
            dtype='float32',
            is_sparse=False)
        self._simple_conv_pool_1 = SimpleConvPool(
            self.channels,
            self.hid_dim,
            self.win_size,
            batch_size=self.batch_size)
        self._fc1 = Linear(input_dim=self.hid_dim * self.seq_len, output_dim=self.fc_hid_dim, act="softmax")
        self._fc_prediction = Linear(input_dim=self.fc_hid_dim,
                                     output_dim=self.class_dim,
                                     act="softmax")

    def forward(self, inputs, label=None):
        emb = self.embedding(inputs)
        o_np_mask = (inputs.numpy().reshape(-1, 1) != self.dict_dim).astype('float32')
        mask_emb = fluid.layers.expand(
            to_variable(o_np_mask), [1, self.hid_dim])
        emb = emb * mask_emb
        emb = fluid.layers.reshape(
            emb, shape=[-1, self.channels, self.seq_len, self.hid_dim])
        conv_3 = self._simple_conv_pool_1(emb)
        fc_1 = self._fc1(conv_3)
        prediction = self._fc_prediction(fc_1)

        if label is not None:
            acc = fluid.layers.accuracy(prediction, label=label)
            return prediction, acc
        else:
            return prediction


'''
参数配置
'''
train_parameters = {
    "epoch": 100,  # 训练轮次
    "batch_size": 256,  # 批次大小
    "lr": 0.0002,  # 学习率
    "padding_size": 150,  # padding纬度
    "vocab_size": 33256,  # padding的值
    "skip_steps": 500,  # 每10个批次输出一次结果
    "save_steps": 500,  # 300个批次保存一次
    "checkpoints": "save_dir/"  # 训练时每个批次的大小
}

def train():
    with fluid.dygraph.guard(place=fluid.CUDAPlace(0)):
        # with fluid.dygraph.guard(place = fluid.CPUPlace()):

        processor = SentaProcessor(
            data_dir=r"data/",
            vocab_path=r"data/dict.txt")

        train_data_generator = processor.data_generator(
            batch_size=train_parameters["batch_size"],
            phase='train',
            epoch=train_parameters["epoch"],
            shuffle=True)

        model = CNN()
        sgd_optimizer = fluid.optimizer.Adagrad(learning_rate=train_parameters["lr"], parameter_list=model.parameters())
        steps = 0
        total_cost, total_acc = [], []
        for eop in range(train_parameters["epoch"]):
            for batch_id, data in enumerate(train_data_generator()):
                steps += 1
                doc = to_variable(
                    np.array([
                        np.pad(x[0][0:train_parameters["padding_size"]],
                               (0, train_parameters["padding_size"] - len(x[0][0:train_parameters["padding_size"]])),
                               'constant',
                               constant_values=(train_parameters["vocab_size"]))
                        for x in data
                    ]).astype('int64').reshape(-1))
                label = to_variable(
                    np.array([x[1] for x in data]).astype('int64').reshape(
                        train_parameters["batch_size"], 1))

                model.train()
                prediction, acc = model(doc, label)
                loss = fluid.layers.cross_entropy(prediction, label)
                avg_loss = fluid.layers.mean(loss)
                avg_loss.backward()
                sgd_optimizer.minimize(avg_loss)
                model.clear_gradients()
                total_cost.append(avg_loss.numpy()[0])
                total_acc.append(acc.numpy()[0])

                if steps % train_parameters["skip_steps"] == 0:
                    print("step: %d, ave loss: %f, ave acc: %f" %
                          (steps, avg_loss.numpy(), acc.numpy()))
                if steps % train_parameters["save_steps"] == 0:
                    save_path = train_parameters["checkpoints"] + "/" + "save_dir_" + str(steps)
                    print('save model to: ' + save_path)
                    fluid.dygraph.save_dygraph(model.state_dict(), save_path)





