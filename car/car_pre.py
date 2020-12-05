from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image

def one_pred(img_path):
    # ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    # img_path = img_path
    # result = ocr.ocr(img_path, cls=True)
    # image = Image.open(img_path).convert('RGB')
    # boxes = [line[0] for line in result]
    # txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    # im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
    province = ["京","沪","津","渝","鲁","冀","晋","蒙","辽","吉","黑","苏","浙","皖","闽","赣","豫","湘","鄂","粤","桂","琼","川","贵","云","藏","陕","甘","青","宁","新","港","澳","台"]
    for line in result:
        text = line[1][0]
        a = str(line[1][0][0])
        #print(a)
        if str(a) in province:
            print(a)
            c = car_test.pre(text)
            if c == "车牌":
                print("\n识别出车牌号为：",text)
    return text


# path=r'F:\chrome\zrbdata\data\video_img/yk26.jpg'
# one_pred(path)
