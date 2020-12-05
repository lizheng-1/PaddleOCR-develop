'''
这里是评估模型好坏的
fluid.load_dygraph(r"save_dir/save_dir_153500.pdparams")
save_dir_153500.pdparams是权重文件
'''
import numpy as np
import paddle.fluid as fluid
from paddle.fluid.dygraph.base import to_variable
from util.lstm_train import SentaProcessor,train_parameters,CNN
import os
def to_eval(weight):
    with fluid.dygraph.guard(place = fluid.CUDAPlace(0)):
        processor = SentaProcessor(
                data_dir=r"data/",
                vocab_path=r"../../../chrome/zrbdata/ocr_lstm/lstm/data/dict.txt")
        eval_data_generator = processor.data_generator(
                batch_size=train_parameters["batch_size"],
                phase='eval',
                epoch=train_parameters["epoch"],
                shuffle=True)

        model_eval = CNN()
        model, _ = fluid.load_dygraph(weight)
        model_eval.load_dict(model)
        model_eval.eval()
        total_eval_cost, total_eval_acc = [], []
        for eval_batch_id, eval_data in enumerate(eval_data_generator()):
            eval_np_doc = np.array([np.pad(x[0][0:train_parameters["padding_size"]],
                                    (0, train_parameters["padding_size"] -len(x[0][0:train_parameters["padding_size"]])),
                                    'constant',
                                    constant_values=(train_parameters["vocab_size"]))
                            for x in eval_data
                            ]).astype('int64').reshape(-1)
            eval_label = to_variable(np.array([x[1] for x in eval_data]).astype(
                                    'int64').reshape(train_parameters["batch_size"], 1))
            eval_doc = to_variable(eval_np_doc)
            eval_prediction, eval_acc = model_eval(eval_doc, eval_label)
            loss = fluid.layers.cross_entropy(eval_prediction, eval_label)
            avg_loss = fluid.layers.mean(loss)
            total_eval_cost.append(avg_loss.numpy()[0])
            total_eval_acc.append(eval_acc.numpy()[0])
    print("Final validation result: ave loss: %f, ave acc: %f\n" %(np.mean(total_eval_cost), np.mean(total_eval_acc)))
    return np.mean(total_eval_cost), np.mean(total_eval_acc)
import os
def change(path):
    i=1
    for filename in os.listdir(path):   #‘logo/’是文件夹路径，你也可以替换其他
        file=path+filename
        os.rename(file,path+'/'+str(i).rjust(3, '0')+'.pdparams')
        # print(file)
        #os.rename(file,path+'b{}.'.format(i)+type1)
        i+=1

change("save_dir/")

a = []
b = []
for weight in os.listdir("save_dir/"):
    print(weight)
    loss,acc = to_eval("save_dir/"+weight)
    a.append(loss)
    b.append(acc)

print(a,b)

