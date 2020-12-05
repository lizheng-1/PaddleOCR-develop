from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image
from lstm import test
import re
import miaoshu.miaoshu_test as ms


def one_pred(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img_path, cls=True)
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
    im_show = Image.fromarray(im_show)
    # im_show.show()
    # im_show.save是保存识别后的图片
    im_show.save("img/result_img/result.jpg")
    n = 0
    stR=""
    phone = "" #电话
    shopName="" #店铺名
    describe = "" #描述
    for line in result:
        texts = line[1][0]
        if texts == "":
            continue
        if len(texts) < 2:
            continue
        # print(line[1])
        n += 1
        stR = stR + str(texts) + ":" + str(texts) + "\n"

        texts = re.findall('[\u4e00-\u9fa50-9]+', texts, re.S)  # 只要字符串中的中文，字母，数字
        texts = "".join(texts)

        if len(texts)<3:
            continue
        r = test.pre(texts)
        if r == "商铺名":
            shopName = shopName + texts + ','
            continue
        s = ms.pre(texts)
        if s == "描述":
            describe = describe + texts
            continue
        # print("+++",texts)

        if re.match(r'^[1-9]\d{11}$', texts) or len(texts) == 11:
            phone = str(texts)
            continue
        else:
            phones = texts.split("1")
       # print("++",phone)
            for i in phones:
                # print(i)
                if re.match(r'^[1-9]\d{7,11}$', i):
                    a = "1" + i
                    # print(a)
                    phone = phone +a +";"
                    continue
    stR = stR + "\n" + "共识别出" + str(n) + "段文本" + "\n其中商铺名为：" + shopName # + "\n电话为：" +str(phone) # + "\n描述为："+describe
    print(stR)
    return stR



# save_path=r"img/result_img/result.jpg"
# one_pred(path)

