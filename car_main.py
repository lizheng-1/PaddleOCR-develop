from car import car_test
'''
主函数，识别图片的同时，将识别出的文字分类，看是否属于店铺名
'''
from paddleocr import PaddleOCR
from lstm import test
import os
from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image
import pandas as pd
import wx
import re
import wx.xrc
from car.video import video_frame as vf
#图形开始
app = wx.App()
window = wx.Frame(None, title = u"实时识别状态展示", size = (969,150),style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
window.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

gbSizer3 = wx.GridBagSizer( 0, 0 )
gbSizer3.SetFlexibleDirection( wx.BOTH )
gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

window.m_staticText10 = wx.StaticText( window, wx.ID_ANY, u"正在识别：", wx.DefaultPosition, wx.DefaultSize, 0 )
window.m_staticText10.Wrap( -1 )

gbSizer3.Add(  window.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

window.m_staticText11 = wx.StaticText( window, wx.ID_ANY, u"图片名字", wx.DefaultPosition, wx.DefaultSize, 0 )
window.m_staticText11.Wrap( -1 )

window.m_staticText11.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
window.m_staticText11.SetMinSize( wx.Size( 800,30 ) )

gbSizer3.Add(  window.m_staticText11, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

window.m_staticText12 = wx.StaticText( window, wx.ID_ANY, u"进度：", wx.DefaultPosition, wx.DefaultSize, 0 )
window.m_staticText12.Wrap( -1 )

gbSizer3.Add(  window.m_staticText12, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

window.m_staticText13 = wx.StaticText( window, wx.ID_ANY, u"正在识别的图片：", wx.DefaultPosition, wx.DefaultSize, 0 )
window.m_staticText13.Wrap( -1 )

gbSizer3.Add(  window.m_staticText13, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

window.m_gauge1 = wx.Gauge( window, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
window.m_gauge1.SetValue( 0 )
window.m_gauge1.SetMinSize( wx.Size( 800,-1 ) )

gbSizer3.Add(  window.m_gauge1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

window.SetSizer( gbSizer3 )
window.Layout()

window.Centre( wx.BOTH )

#图形结束


def pre_save(img_path,save_path,csv_path,m_filePicker11=None):
    cechu = []
    ocr = PaddleOCR(use_angle_cls=True, lang="ch") # need to run only once to download and load model into memory
    i = 0
    names =[]
    #abels = []
    imgs=[]
    one_qian_pic_path = ""
    one_hou_pic_path = ""
    #存放所有的图片路径
    n_qian_pic_path = []
    n_hou_pic_path = []
    j=0
    stR = ""
    # 启动窗口
    window.Show(True)

    jindu_len = len(os.listdir(img_path)) + 2
    print("共："+str(jindu_len-2))
    window.m_gauge1.SetRange(jindu_len)
    dangqian_jindu = 1
    n=0
    aaa = []
    for img in os.listdir(img_path):
        n+=1
        window.m_staticText11.SetLabel("正在识别："+img_path+'/'+img)
        print("当前正在识别"+str(dangqian_jindu)+"-->"+"正在识别："+img_path+'/'+img)
        window.m_gauge1.SetValue(dangqian_jindu)
        dangqian_jindu = dangqian_jindu + 1

        #动态显示进度条
        if dangqian_jindu==jindu_len:
            window.m_gauge1.SetValue(dangqian_jindu)
        print(img_path+'/'+img)
        i += 1
        result = ocr.ocr(img_path+'/'+img, cls=True)
        image = Image.open(img_path+'/'+img).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
        im_show = Image.fromarray(im_show)
        # im_show.show()
        # im_show.save是保存识别后的图片
        im_show.save(save_path+"/"+img)
        #存储所有的图片路径
        n_qian_pic_path.append(img_path+'/'+img)
        n_hou_pic_path.append(save_path+"/"+img)

        for line in result:
            if line[1][0] =="":
                continue
            #print("+++",line)
            if len(re.findall("[\u4e00-\u9fa5]",str(line[1][0]))) > 2:
                continue
            if len(str(line[1][0])) < 6:
                continue
            car_board = one_pred(str(line[1][0]))
            aaa.append(car_board)
            #print("***",car_board)

        if j==0:
            one_hou_pic_path = save_path+"/"+img
            one_qian_pic_path = img_path+'/'+img
        j = j + 1
        if str(result) == "None":
            continue
        dataframe = pd.DataFrame({'图片名': imgs, '车牌号': names})
        if csv_path[-3:]=="xls":
            dataframe.to_excel(csv_path, index=True)
        elif csv_path[-3:]=="csv":
            dataframe.to_csv(csv_path, index=True,sep=',')
        else:
            print("请选择csv或者xls文件")

    n = 0
    for i in aaa:
        if i != None:
            if str(i) not in set(cechu):
                cechu.append(str(i))
               # n += 1
    # for i in aaa:
    #     if i != None:
    #         if str(i) not in cechu:
    #             stR = stR + str(i) + "\n"
    #             n +=1
    for p in set(cechu):
        print(p)
    #print(stR)
    stR = stR # + "共识别出的车牌数为：" + str(n)
    print("共识别出的车牌数为：" ,len(set(cechu)))
    dangqian_jindu = dangqian_jindu + 1
    window.m_gauge1.SetValue(dangqian_jindu)
    # print("当前正在识别" + str(dangqian_jindu))
    # print("+++",cechu)
    # print(stR)
    return stR,one_qian_pic_path,one_hou_pic_path,n_qian_pic_path,n_hou_pic_path
#图片拼接为视频
import os
import cv2
from PIL import Image

# 图片合成视频
def picvideo(pthoto_path,save_path):
    # path = r'C:\Users\Administrator\Desktop\1\huaixiao\\'#文件路径
    filelist = os.listdir(pthoto_path)  # 获取该目录下的所有文件名
    # print(filelist)
    # print(pthoto_path+'/'+filelist[1])
    size = Image.open(pthoto_path+'/'+filelist[0]).size
    # print(size)

    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
    如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 7
    # size = (591,705) #图片的分辨率片
    # time=len(filelist)/fps
    # file_path = save_path+'/' + str(int(time)) + ".mp4"  # 导出路径
    n=len(filelist)
    file_path = save_path + "/car_after.mp4"
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
    video = cv2.VideoWriter(file_path, fourcc, fps, size)
    for item in filelist:
        #if item.endswith('.jpg'):  # 判断图片后缀是否是.png
            item = pthoto_path + '/' + item
            img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            video.write(img)  # 把图片写进视频
    video.release()     # 释放

def one_pred(text):
    a = text[0]
    province = ["京","沪","津","渝","鲁","冀","晋","蒙","辽","吉","黑","苏","浙","皖","闽","赣","豫","湘","鄂","粤","桂","琼","川","贵","云","藏","陕","甘","青","宁","新","港","澳","台"]
    if str(a) in province:
        # print(a)
        c = car_test.pre(text)
        if c == "车牌":
            print("\n识别出车牌号为：",text)
            return text
        else:
            return 0

# 视频地址
video_path=r'img/car_befor.mp4'
# 视频分帧的图片地址
photo_path=r'img\video_img'
# 识别后图片的地址
save_path=r'img\video_save'
# 保存scv数据文件的地址
csv_path=r'img\chepai12.csv'

# 视频分帧
vf.fenzhen(video_path,photo_path)

# 预测+保存数据
pre_save(photo_path,save_path,csv_path)

# 视频合成
video_path = r"img"
picvideo(save_path,video_path)
