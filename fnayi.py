from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image

def one_pred(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img_path, cls=True)
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
    im_show = Image.fromarray(im_show)

    n = 0
    stR=""
    for line in result:
        #print(line[1])
        n += 1
        texts = line[1][0]
        stR = stR + "," + str(texts)
        #print(texts)
    print(stR)
    im_show.show()
    return stR
#
# path1 = r'img\10.png'
# path2 = r'img\11.png'
# text = one_pred(path1)


