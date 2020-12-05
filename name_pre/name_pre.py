from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image
import name_test
import re
import pandas as pd
import miaoshu.miaoshu_test as ms
def one_pred(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    save_path = img_path
    result = ocr.ocr(img_path, cls=True)
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
    im_show = Image.fromarray(im_show)
    n_qian_pic_path=[]
    n_hou_pic_path=[]
    # print(result)
    n = 0
    stR=""
    name = ""
    all = ""
    phone = ""#电话
    shopName="" #店铺名
    describe = ""#描述
    otherinfo = "没有其他信息"
    n_qian_pic_path.append(img_path + '/' + path[-3:])
    n_hou_pic_path.append(save_path + "/" + path[-3:])
    for line in result:
        n += 1
        texts = line[1][0]

        if len(texts) < 4:
            nm = name_test.pre(texts)
            if nm == "姓名":
                name = name + texts

        nm1 = re.findall('[\u4e00-\u9fa5]+', texts[:3], re.S)
        nm = name_test.pre(nm1)
        if nm == "姓名":
            name = name + str(nm1)
        if texts[0] == "东":
            a1 = texts
        r = name_test.pre(texts)
        if len(texts) < 2:
            continue
        if r == "商铺名":
            shopName = shopName + texts
            continue
        if texts[0] == "孙":
            a2 = re.findall('[\u4e00-\u9fa5]+',texts,re.S)
        s = ms.pre(texts)
        if s == "描述":
            describe = describe + texts
            continue
        stR = stR+str(line[1][0])+":"+str(line[1][1])+"\n"
        phones = texts.split("1")
        if texts[:2] == "地址":
            a3 = texts
        if texts[:2] == "电话":
            a4 = re.findall('[0-9]+',texts,re.S)
        if re.match(r'^[0-9]\d{9,12}$', texts):
            phone =  "1" +  texts
       # print("++",phone)

        for i in phones:
            # print(i)
            if re.match(r'^[0-9]\d{9}$', i):
                a = "1" + i
                # print(a)
                phone = phone + ";"+a
    # 存储所有的图片路径

    phone = phone[1:]
    all = all + "\n公司名称：" + str(a1) + "\n姓名："+ "".join(a2) + "\n手机："+phone+"\n" +str(a3) + "\n电话："+"".join(a4[:2]) + ";" + "".join(a4[2:])
    #print("+++",name)
    print(all)
    one_hou_pic_path = save_path + "/" + path[-3:]
    one_qian_pic_path = img_path + '/' + path[-3:]
    # print("****",shopName,phone,describe,otherinfo)
    #return im_show.show()
    im_show.show()
    return shopName,phone,describe,otherinfo,one_qian_pic_path,one_hou_pic_path

def txt_result(txt_file,csv_file):
    f=open(txt_file,encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        if len(line)<3:
            continue
        name_test.pre(line)
    dataframe = pd.DataFrame({'name':names,"labels":labels})
    dataframe.to_csv(csv_file, index=True, sep=',')

path=r'F:\chrome\zrbdata\data/1.png'
one_pred(path)

