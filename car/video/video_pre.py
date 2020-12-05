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
import wx.xrc
import video_frame as vf
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
        #存储所有的图片路径
        n_qian_pic_path.append(img_path+'/'+img)
        n_hou_pic_path.append(save_path+"/"+img)

        for line in result:
            if line[1][0] =="":
                continue
            if len(line) < 6:
                continue
            # print("+++",line)
            car_board = one_pred(str(line[1][0]))
            aaa.append(car_board)
            #print("***",car_board)

        if j == 0:
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

    for i in aaa:
        if i != None:
            stR = stR + str(i) + "\n"

    dangqian_jindu = dangqian_jindu + 1
    window.m_gauge1.SetValue(dangqian_jindu)
    print("当前正在识别" + str(dangqian_jindu))
    print(i)
    print(stR)
    return stR,one_qian_pic_path,one_hou_pic_path,n_qian_pic_path,n_hou_pic_path
def one_pred(text):

    a = text[0]
    province = ["京","沪","津","渝","鲁","冀","晋","蒙","辽","吉","黑","苏","浙","皖","闽","赣","豫","湘","鄂","粤","桂","琼","川","贵","云","藏","陕","甘","青","宁","新","港","澳","台"]
    if str(a) in province:
        # print(a)
        c = car_test.pre(text)
        if c == "车牌":
            ss = str(text)
            print("\n识别出车牌号为：",text)
            return text
        else:
            return 0
# one_pred("鲁A18430")


video_path=r'F:\chrome\zrbdata\data/a.mp4'
photo_path=r'F:\chrome\zrbdata\data\video_img'
# 分别为图片的地址和保存scv数据文件的地址
save_path=r'F:\chrome\zrbdata\data\video_save/'
csv_path=r'F:\chrome\zrbdata\data\chepai12.csv'
vf.fenzhen(video_path,photo_path,15)
pre_save(photo_path,save_path,csv_path)

