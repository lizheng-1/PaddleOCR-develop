'''
训练自定义的数据，data
'''
from util.lstm_train import SentaProcessor,train_parameters,CNN
from util.data_pro import create_data_list,create_dict
import numpy as np
import paddle.fluid as fluid
from paddle.fluid.dygraph.base import to_variable

'''
参数配置
'''
train_parameters = {
    "epoch": 100,  # 训练轮次
    "batch_size": 256,  # 批次大小
    "lr": 0.005,  # 学习率
    "padding_size": 150,  # padding纬度
    "vocab_size": 33256,  # padding的值
    "skip_steps": 1000,  # 每10个批次输出一次结果
    "save_steps": 1000,  # 300个批次保存一次
    "checkpoints": "save_dir/"  # 训练时每个批次的大小
}

def train():
    with fluid.dygraph.guard(place=fluid.CUDAPlace(0)):
        # with fluid.dygraph.guard(place = fluid.CPUPlace()):
        processor = SentaProcessor(
            data_dir="data/",
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

# # 创建数据字典
all_data=r"data/newdata.txt"
dict =r"data/dict.txt"
create_dict(all_data, dict)
# # 创建数据列表
create_data_list("data")
# # 训练 权重的储存地址为save_dir
train()
