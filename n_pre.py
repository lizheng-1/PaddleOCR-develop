'''
主函数，识别图片的同时，将识别出的文字分类，看是否属于店铺名
'''
from paddleocr import PaddleOCR
from lstm import test
import os
import re
from paddleocr import PaddleOCR
from tools.infer.utility  import draw_ocr
from PIL import Image
import pandas as pd
import wx
import wx.xrc
# from miaoshu import miaoshu_test
# 图形开始
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
        i+=1
        result = ocr.ocr(img_path+'/'+img, cls=True)

        image = Image.open(img_path+'/'+img).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='/doc/simfang.ttf')
        im_show = Image.fromarray(im_show)
        # im_show.show()
        # im_show.save是保存识别后的图片
        sp = save_path+"/"+img
        im_show.save(sp)
        print("图片保存的位置："+sp)
        #存储所有的图片路径
        n_qian_pic_path.append(img_path+'/'+img)
        n_hou_pic_path.append(save_path+"/"+img)
        if j==0:
            one_hou_pic_path = save_path+"/"+img
            one_qian_pic_path = img_path+'/'+img
        j = j + 1
        if str(result) == "None":
            continue
        for line in result:
            texts = line[1][0]
            if texts == "":
                continue

            if texts in names:
                continue
            texts = re.findall('[\u4e00-\u9fa50-9]+', texts, re.S)  # 只要字符串中的中文，字母，数字
            texts = "".join(texts)

            label = test.pre(texts)
            if len(texts) < 3:
                label = "非商铺名"
            if label == "商铺名":
                #print(texts, " ：", label)
                stR = stR + str(img) + ":" + str(texts) + "\n"
                imgs.append(img)
                #labels.append(label)
                names.append(texts)
        dataframe = pd.DataFrame({'图片名': imgs, '商铺名称': names})
        if csv_path[-3:]=="xls":
            dataframe.to_excel(csv_path, index=True)
        elif csv_path[-3:]=="csv":
            dataframe.to_csv(csv_path, index=True,sep=',')
        else:
            print("请选择csv或者xls文件")
    stR = stR + "\n" + "共识别了" + str(n) + "张图片" + "\n" + "共检测出商铺名" + str(i) + "个\n"
    dangqian_jindu = dangqian_jindu + 1
    window.m_gauge1.SetValue(dangqian_jindu)
    print("当前正在识别" + str(dangqian_jindu))
    print(i)

    return stR,one_qian_pic_path,one_hou_pic_path,n_qian_pic_path,n_hou_pic_path


# # # # 分别问图片的地址和保存scv数据文件的地址
# img_path = r'img\new_img'
# save_path = r"F:\chrome\zrbdata\data\result"
# csv_path = r'F:\chrome\zrbdata\data\result5.csv'
# pre_save(img_path,save_path,csv_path)



