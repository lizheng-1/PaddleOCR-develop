from paddleocr import PaddleOCR

from tools.infer.utility  import draw_ocr
from PIL import Image
from lstm import test
import re
import miaoshu.miaoshu_test as ms


def one_pred(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img_path, cls=False)
    # print(result)
    n = 0
    stR=""
    phone = ""#电话
    shopName="" #店铺名
    describe = ""#描述
    otherinfo = "没有其他信息"
    print("+++",result)
    for line in result:
        n += 1
        texts = line[1][0]
        if texts == "":
            continue
        if len(texts) < 2:
            continue
        r = test.pre(texts)
        if len(texts) < 3:
            continue
        if r == "商铺名":
            shopName = shopName + texts
            continue
        s = ms.pre(texts)
        if s == "描述":
            describe = describe + texts
            continue
        stR = stR+str(line[1][0])+":"+str(line[1][1])+"\n"
        phones = texts.split("1")
       # print("++",phone)
        for i in phones:
            # print(i)
            if re.match(r'^[1-9]\d{9}$', i):
                a = "1" + i
                # print(a)
                phone = phone + ";"+a
            else:
                phone = " 图片中没有电话信息"
    phone = phone[1:]
    print("****",shopName,phone,describe,otherinfo)
    #return im_show.show()

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
    im_show = Image.fromarray(im_show)
    # im_show.show()
    # im_show.save是保存识别后的图片
    fanhui_img = 'result.jpg'
    im_show.save(fanhui_img)

    return shopName,phone,describe,otherinfo,fanhui_img

# path是图片路径，
# path=r'F:\chrome\zrbdata\data\images\33.jpg'
# # path="img/4.jpg"
# # save_path=r"img/result_img/result.jpg"
# one_pred("img\ygf.png")

