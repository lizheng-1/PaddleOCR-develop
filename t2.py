from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
ocr = PaddleOCR() # need to run only once to download and load model into memory
img_path = r'F:\chrome\zrbdata\data\images\33.jpg'
result = ocr.ocr(img_path, rec=False)
print("+++",result)
for line in result:
    print(line)

# 显示结果
from PIL import Image

image = Image.open(img_path).convert('RGB')
im_show = draw_ocr(image, result, txts=None, scores=None, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
im_show.show()
