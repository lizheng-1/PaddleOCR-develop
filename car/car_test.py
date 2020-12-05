import pandas as pd
from lstm.util.lstm_train import SentaProcessor,train_parameters,CNN
import numpy as np
import paddle.fluid as fluid
from paddle.fluid.dygraph.base import to_variable

# 获取数据
def load_data(sentence):
    # 读取数据字典
    with open(r'F:\lzpython\PaddleOCR-develop\car\data\dict.txt', 'r', encoding='utf-8') as f_data:
        dict_txt = eval(f_data.readlines()[0])
    dict_txt = dict(dict_txt)
    # 把字符串数据转换成列表数据
    keys = dict_txt.keys()
    data = []
    for s in sentence:
        # 判断是否存在未知字符
        if not s in keys:
            s = '<unk>'
        data.append(int(dict_txt[s]))
    return data

train_parameters["batch_size"] = 1
lab = ['车牌', '非车牌']
names =[]
labels = []
def pre(text):
    with fluid.dygraph.guard(place = fluid.CUDAPlace(0)):
        data = load_data(text)
        data_np = np.array(data)
        data_np = np.array(np.pad(data_np,(0,150-len(data_np)),"constant",constant_values =train_parameters["vocab_size"])).astype('int64').reshape(-1)
        infer_np_doc = to_variable(data_np)
        model_infer = CNN()
        model, _ = fluid.load_dygraph(r"F:\lzpython\PaddleOCR-develop\car\save_dir\save_dir_9000.pdparams")
        model_infer.load_dict(model)
        model_infer.eval()
        result = model_infer(infer_np_doc)
        result = lab[np.argmax(result.numpy())]
        print(text,'预测结果为：', result)
        labels.append(result)
        names.append(text)
    return result

def txt_result(txt_file,csv_file):
    f=open(txt_file,encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        if len(line)<3:
            continue
        pre(line)
    dataframe = pd.DataFrame({'name':names,"labels":labels})
    dataframe.to_csv(csv_file, index=True, sep=',')

