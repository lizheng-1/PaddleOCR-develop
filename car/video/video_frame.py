#视频分帧
import cv2
import os
import shutil
def fenzhen(video_path,photo_path):
    i=0
    j=1
    frame = 15
    camera = cv2.VideoCapture(video_path)
    while True:
        i += 1
        res, image = camera.read()
        if i % frame == 0:
            j += 1
            cv2.imwrite(photo_path+'/{0:0>3}.jpg'.format(j), image)
            print('{0:0>3}.jpg'.format(j))

        if not res:
            print("图片提取结束,共提取了{}张图片".format(j))
            break
    camera.release()


# for i in range(1,22):
#     photo_path = "E:/gfdata/Video/{}".format(i)
#     video_path = r'E:/gfdata/Video/{}.mp4'.format(i)
#     if not os.path.exists(photo_path):
#         # 如果不存在就自己生成一个
#         os.mkdir(photo_path)
#     fenzhen(video_path,photo_path,frame)
#     shutil.move(video_path,photo_path)
#
# video_path=r'F:\chrome\zrbdata\data/a.mp4'
# photo_path=r'F:\chrome\zrbdata\data\video_img/'
# frame=5
# fenzhen(video_path,photo_path,frame)
