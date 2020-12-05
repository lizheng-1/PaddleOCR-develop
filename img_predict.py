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
    im_show.show()
    # im_show.save()


path1 = r'img\000.png'
path2 = r'img\11.png'
# path="img/4.jpg"
# save_path=r"img/result_img/result.jpg"
one_pred(path1)

