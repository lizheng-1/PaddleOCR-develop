
from flask import Flask, redirect, url_for ,request
import base64
import json
import mobile_pre
import requests
import ossUtil
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

def get_phono_img(url):
    img_url = url
    img_path = r"F:\lzpython\PaddleOCR-develop\img\phone.jpg"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
    s = requests.Session()
    response = s.get(url=img_url, headers=headers)
    content = response.content
    f = open(img_path, 'wb')
    f.write(content)
    f.close()
    return img_path


@app.route("/ocr_one",methods=["GET","POST"])
def ocr_one():
    if request.method == "GET":
        print("进入到了：2/ocr_one [GET]")
        # imgUrl = request.args.get("imgUrl")
        imgUrl = request.args['imgUrl']
        print(imgUrl)
        # imgUrl = request.args.get("imgUrl")
        print("+++",request)
        img_path = get_phono_img(imgUrl)
        shopName, phone, describe, otherinfo,fanhui_img = mobile_pre.one_pred(img_path)

        ossOCRImgUrl = ossUtil.upload_oss_file(fanhui_img)
        print(ossOCRImgUrl)
        # 6、封装返回的结果
        # 返回的结果  需要修改成识别之后的：
        resultData = {
            "shopName": shopName,  # 店铺名
            "phone": phone,  # 电话
            "describe": describe,  # 描述
            "otherinfo": otherinfo, # 其他信息
            "ossOCRImgUrl":ossOCRImgUrl
        }

        # 7、返回数据
        print(json.dumps(resultData))
    return json.dumps(resultData)


if __name__ == "__main__":
    # app.run(host="192.168.1.101",port=8080)
    # app.run(host="127.0.0.1", port=8080)
    app.run(host="0.0.0.0", port=8080)


