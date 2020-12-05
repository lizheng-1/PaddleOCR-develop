# encoding=utf-8

import oss2
import time

def upload_oss_file(localFileUrl):
	#生成日期文件名
	fileName = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

	endpoint = 'http://oss-cn-beijing.aliyuncs.com'
	auth = oss2.Auth('....', '....')
	bucket = oss2.Bucket(auth, endpoint, '8042965')

	#上传的文件名
	current_file_path = 'ocr/' + str(fileName) + "." +  localFileUrl.split(".")[1]

	# 上传到oss
	bucket.put_object_from_file(current_file_path, localFileUrl)

	#获取OSS的图片路径
	oss_img_file = bucket.sign_url('GET', current_file_path, 60*60)  # 请求方式 路径 有效时间(秒)

	return oss_img_file


key = r'img\video_img\002.jpg'
upload_oss_file(key)

