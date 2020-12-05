#图片拼接为视频
import os
import cv2
from PIL import Image
# 图片合成视频
def picvideo(pthoto_path,save_path):
    # path = r'C:\Users\Administrator\Desktop\1\huaixiao\\'#文件路径
    filelist = os.listdir(pthoto_path)  # 获取该目录下的所有文件名
    print(filelist)
    print(pthoto_path+'/'+filelist[1])
    size = Image.open(pthoto_path+'/'+filelist[0]).size
    print(size)
    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
    如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 3
    # size = (591,705) #图片的分辨率片
    # time=len(filelist)/fps
    # file_path = save_path+'/' + str(int(time)) + ".mp4"  # 导出路径
    n=len(filelist)
    file_path = save_path + '/'+str(int(n)) + ".mp4"
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for item in filelist:
        #if item.endswith('.jpg'):  # 判断图片后缀是否是.png
            item = pthoto_path + '/' + item
            img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            video.write(img)  # 把图片写进视频
    video.release()     # 释放

photo_path = r"F:\lzpython\PaddleOCR-develop\img\video_save"
video_path = r"F:\lzpython\PaddleOCR-develop\img"
picvideo(photo_path,video_path)
print('666')

