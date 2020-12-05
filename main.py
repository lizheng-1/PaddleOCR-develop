# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
# 识别单张图片
import one_pre
# 多张图片
import n_pre
###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"识别窗口", pos = wx.DefaultPosition, size = wx.Size( 1383,770 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"请选择图片或者目录：" ), wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0)
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gbSizer1.SetMinSize( wx.Size( 50,50 ) )
		self.m_staticText12 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择识别的图片：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap(-1)

		gbSizer1.Add( self.m_staticText12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 13 )

		self.m_filePicker11 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入", u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 600,-1 ), wx.FLP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_filePicker11, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_dirPicker21 = wx.DirPickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入", u"Select a folder", wx.DefaultPosition, wx.Size( 600,-1 ), wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker21, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"或选择识别图片的目录：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		gbSizer1.Add( self.m_staticText111, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 13 )

		self.m_toggleBtn11 = wx.ToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"识别多张", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_toggleBtn11, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button7 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"识别单张", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button7, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		# self.m_dirPicker2 = wx.DirPickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入", u"Select a folder", wx.DefaultPosition, wx.Size( 600,-1 ), wx.DIRP_DEFAULT_STYLE )
		# gbSizer1.Add( self.m_dirPicker2, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_dirPicker2 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入", u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 600,-1 ), wx.FLP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker2, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"*必选", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		gbSizer1.Add( self.m_staticText9, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		# self.m_filePicker2 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入1", u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 600,-1 ), wx.FLP_DEFAULT_STYLE )
		# gbSizer1.Add( self.m_filePicker2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		# self.m_filePicker2 = wx.DirPickerCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入1", u"Select a file",
		# 									   u"*.*", wx.DefaultPosition, wx.Size(600, -1), wx.FLP_DEFAULT_STYLE)
		# gbSizer1.Add(self.m_filePicker2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_filePicker2 = wx.DirPickerCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"请选择或者输入", u"Select a folder",
											 wx.DefaultPosition, wx.Size(600, -1), wx.DIRP_DEFAULT_STYLE)
		gbSizer1.Add(self.m_filePicker2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"*必选", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		gbSizer1.Add( self.m_staticText10, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"识别结果图片存放位置：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		gbSizer1.Add( self.m_staticText61, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 13 )

		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"识别结果数据文件存放位置：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 13 )


		sbSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"数据展示区域:" ), wx.VERTICAL )

		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"原图：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer11.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"识别后的图：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer11.Add( self.m_staticText5, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"识别的信息：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer11.Add( self.m_staticText6, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap2.SetMinSize( wx.Size( 400,400 ) )
		self.m_bitmap2.SetMaxSize( wx.Size( 400,400 ) )

		gbSizer11.Add( self.m_bitmap2, wx.GBPosition( 1, 0 ), wx.GBSpan( 2, 2 ), wx.ALL, 0 )

		self.m_bitmap21 = wx.StaticBitmap( sbSizer10.GetStaticBox(), wx.ID_ANY,  wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_bitmap21.SetMinSize( wx.Size( 500,430 ) )
		self.m_bitmap21.SetMaxSize( wx.Size( 400,400 ) )

		gbSizer11.Add( self.m_bitmap21, wx.GBPosition( 1, 3 ), wx.GBSpan( 2, 2 ), wx.ALL, 0 )

		self.m_textCtrl1 = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,50 ), wx.TE_DONTWRAP|wx.TE_MULTILINE )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_textCtrl1.SetMinSize( wx.Size( 400,400 ) )
		self.m_textCtrl1.SetMaxSize( wx.Size( 500,700 ) )
		#显示结果的字体
		font1 = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, '宋体')
		self.m_textCtrl1.SetFont(font1)

		gbSizer11.Add( self.m_textCtrl1, wx.GBPosition( 1, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_toggleBtn4 = wx.ToggleButton( sbSizer10.GetStaticBox(), wx.ID_ANY, u"查看原图的大图", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn4.SetValue( True )
		gbSizer11.Add( self.m_toggleBtn4, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.m_toggleBtn5 = wx.ToggleButton( sbSizer10.GetStaticBox(), wx.ID_ANY, u"查看识别后的大图", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.m_toggleBtn5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )


		sbSizer10.Add( gbSizer11, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer10, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events  按钮事件
		self.m_toggleBtn11.Bind( wx.EVT_TOGGLEBUTTON, self.btn_shibie_n_pic )
		self.m_button7.Bind( wx.EVT_BUTTON, self.btn_shibie_one_pic )
		self.m_toggleBtn4.Bind( wx.EVT_TOGGLEBUTTON, self.SelectShibieqian )
		self.m_toggleBtn5.Bind( wx.EVT_TOGGLEBUTTON, self.selectShibiehou )
		# self.m_toggleBtn6.Bind( wx.EVT_TOGGLEBUTTON, self.danzhangShibiehou)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	#识别N个图
	def btn_shibie_n_pic( self, event ):
		self.shibie_type = "n"

		# 目录路径
		self.dirPath = self.m_dirPicker21.Path
		print(self.dirPath)

		# 图片要保存的目录位置
		self.save_pic_path = self.m_filePicker2.Path

		# csv文件要保存的位置
		self.save_csv_path = self.m_dirPicker2.Path
		#开始识别图片
		res,one_qian_pic_path,one_hou_pic_path,n_qian_pic_path,n_hou_pic_path= n_pre.pre_save(self.dirPath,self.save_pic_path,self.save_csv_path,self.m_filePicker11)

		#把路径保存到全局，方便拿到
		self.n_qian_pic_path = n_qian_pic_path
		self.n_hou_pic_path = n_hou_pic_path

		bitMap = self.picToBitMap(400, 600, one_qian_pic_path)
		self.m_bitmap2.SetBitmap(bitMap)  # 显示原图

		bitMap2 = self.picToBitMap(400, 700, one_hou_pic_path)
		self.m_bitmap21.SetBitmap(bitMap2)  # 显示识别后的图片

		self.m_textCtrl1.SetValue(res) #显示识别的信息

		event.Skip()

	#识别单个图
	###########################################################################
	## 点击开始识别按钮的触发事件
	###########################################################################
	def btn_shibie_one_pic( self, event ):
		self.shibie_type = "one"

		# 单独文件路径
		self.filePath = self.m_filePicker11.Path

		self.flag = "one_pic"

		value = one_pre.one_pred(self.filePath)
		self.save_path = "img/result_img/result.jpg"

		bitMap2 = self.picToBitMap(400, 700, "img/result_img/result.jpg")
		self.m_bitmap21.SetBitmap(bitMap2)  # 显示识别后的图片
		# 期望图像显示的大小（窗口大小）
		# 参数1：期望缩小图片的高
		# 参数2：期望缩小图片的宽
		# 参数3：期望缩小图片的路径
		bitMap = self.picToBitMap(400, 600, self.filePath)
		self.m_bitmap2.SetBitmap(bitMap)  # 显示原图

		bitMap2 = self.picToBitMap(400, 700, self.save_path)
		self.m_bitmap21.SetBitmap(bitMap2)  # 显示识别后的图片

		self.m_textCtrl1.SetValue(value)  # 显示识别的信息
		print(self.filePath)

		# 把路径保存到全局，方便拿到
		self.n_qian_pic_path = self.filePath
		self.n_hou_pic_path = "img/result_img/result.jpg"

		event.Skip()

	#查看识别前的图片
	def SelectShibieqian( self, event ):
		print("----查看识别前的图片----")

		#识别类型
		shibieType = self.shibie_type

		if shibieType=="one":
			print("1")

			# 从单独文件路径拿到图片，然后缩放后转换成bitMap图（位图）
			# bitMap = self.picToBitMap(900,1300,self.filePath)

			# 封装要查看的图片成[bitMap,bitMap2,bitMap3,bitMap4]形式,方便之后翻页
			# self.images = [bitMap]
			self.images = []

			one_images = self.picToBitMap(900, 1300, self.n_qian_pic_path)

			# 启动图片查看界面
			app = wx.App()
			# frame = MyFrame_SelectPic(self.images)
			# frame = MyFrame_SelectPic(self.images)
			frame = MyFrame_SelectPic_1(one_images)
			frame.Show()
			app.MainLoop()

			# 默认必须要有的
			event.Skip()


		elif shibieType=="n":
			print("n")
			# 从单独文件路径拿到图片，然后缩放后转换成bitMap图（位图）
			# bitMap = self.picToBitMap(900,1300,self.filePath)

			# 封装要查看的图片成[bitMap,bitMap2,bitMap3,bitMap4]形式,方便之后翻页
			# self.images = [bitMap]
			self.images = []

			for img_path in self.n_qian_pic_path:
				self.images.append(self.picToBitMap(900, 1300, img_path))

			# 启动图片查看界面
			app = wx.App()
			# frame = MyFrame_SelectPic(self.images)
			frame = MyFrame_SelectPic(self.images)
			frame.Show()
			app.MainLoop()

			# 默认必须要有的
			event.Skip()



	#查看识别后的图片
	def selectShibiehou( self, event):
		#print("selectShibiehou")
		# if self.flag == "one_pic":
		# 	# 从单独文件路径拿到图片，然后缩放后转换成bitMap图（位图）
		# 	# bitMap = self.picToBitMap(1000, 1300, self.save_path)
		# 	bitMap = wx.Bitmap(self.save_path, wx.BITMAP_TYPE_ANY)
		# 	# 封装要查看的图片成[bitMap,bitMap2,bitMap3,bitMap4]形式,方便之后翻页
		# 	self.images = [bitMap
		# 				   # wx.Bitmap('C:\\Users\\zhengsu\\Pictures\\小埋.jpg', wx.BITMAP_TYPE_ANY)
		# 				   ]

		# 识别类型
		shibieType = self.shibie_type

		if shibieType == "one":
			bitmap_one = wx.Bitmap(self.n_hou_pic_path, wx.BITMAP_TYPE_ANY)

			# 启动图片查看界面
			app = wx.App()
			# frame = MyFrame_SelectPic(bitmap_one)
			frame = MyFrame_SelectPic_1(bitmap_one)
			frame.Show()
			app.MainLoop()
			event.Skip()
		elif shibieType=="n":
			self.images = []
			for img_path in self.n_hou_pic_path:
				self.images.append(wx.Bitmap(img_path, wx.BITMAP_TYPE_ANY))

			# 启动图片查看界面
			app = wx.App()
			frame = MyFrame_SelectPic(self.images)
			frame.Show()
			app.MainLoop()
			event.Skip()

	# 对一个pil_image对象进行缩放，让它在一个预想范围内，还能保持比例
	def resize(self,w_box, h_box, pil_image_w,pil_image_h):  # 参数是：要适应的窗口宽、高、Image原图片
		f1 = 1.0 * w_box / pil_image_w # 获取图像的原始大小
		f2 = 1.0 * h_box / pil_image_h
		factor = min([f1, f2])
		width = int(pil_image_w * factor)
		height = int(pil_image_h * factor)
		return width, height #返回缩放后的大小

	# 普通图片 转换成位图的方法
	def picToBitMap(self,w_box,h_box,filePath):

		bmp = wx.BitmapFromImage(wx.ImageFromStream(filePath))
		w = bmp.GetWidth()  # 获取图片的高和宽
		h = bmp.GetHeight()

		# resize函数使用过程（按比例缩放图片的大小）：
		# ==================================================================
		# w_box = w_box  # 期望图像显示的大小（窗口大小）
		# h_box = h_box
		# 缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的大小】
		width, height = self.resize(w_box, h_box, w, h)

		img = wx.Image(filePath, wx.BITMAP_TYPE_ANY).Scale(width, height)  # 通过wx.Image 加载图片，并缩放图片到长宽为25,25的尺寸

		bitMap = wx.Bitmap(img, wx.BITMAP_TYPE_ANY)  # 把普通图片转换成后的位图
		return bitMap


#
# 显示图片的demo
#
class MyFrame_SelectPic_1(wx.Frame):
	eve = 0

	#images:传递过来的图片
	def __init__(self,images=None):
		super().__init__(parent=None, title="vbox", size=(1500, 800), pos=(100, 100))  # 继承wx.Frame类
		self.Center()
		self.panel = wx.Panel(parent=self)  # 面板
		vbox = wx.BoxSizer(wx.VERTICAL)
		self.image = wx.StaticBitmap(self.panel, -1, images)
		vbox.Add(self.image, 5, wx.CENTER)
		self.panel.SetSizer(vbox)


class MyFrame_SelectPic(wx.Frame):
	eve = 0

	#images:传递过来的图片
	def __init__(self,images=None):
		super().__init__(parent=None, title="vbox", size=(1500, 800), pos=(100, 100))  # 继承wx.Frame类
		self.Center()
		self.panel = wx.Panel(parent=self)  # 面板
		vbox = wx.BoxSizer(wx.VERTICAL)

		#如果默认的图片不等于空，就赋值，否则就等于默认的
		if images!=None:
			self.bmps = images
		else: #就等于默认的图片
			self.bmps = [
				wx.Bitmap('F:\lzpython\PaddleOCR-develop\img\hengshu.png', wx.BITMAP_TYPE_ANY),
				wx.Bitmap('F:\lzpython\PaddleOCR-develop\img\hengshu.png', wx.BITMAP_TYPE_ANY)
			]

		# 初始值 从0开始
		self.start_index = 0
		# 最大长度
		self.end_index = len(self.bmps)

		self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0])

		next = wx.Button(self.panel, id=1, label='切换下一张')
		self.Bind(wx.EVT_BUTTON, self.on_click, next)

		vbox.Add(next, 1, wx.CENTER)
		vbox.Add(self.image, 5, wx.CENTER)

		self.panel.SetSizer(vbox)

	#切换下一张图片
	def on_click(self, event):
		# event_id = event.GetId()
		# print("-------------")
		# print(str(self.start_index)+"---->"+str(self.end_index))
		# print("-------------")
		#如果下一张没到头，每点击一次按钮图片就切换到下一个
		if self.end_index != self.start_index+1:
			self.start_index += 1
			self.image.SetBitmap(self.bmps[self.start_index])

		# if self.eve % 2 == 0:
		# 	self.image.SetBitmap(self.bmps[1])
		#
		# else:
		# 	self.image.SetBitmap(self.bmps[0])
		self.eve = self.eve + 1
		self.panel.Layout()
		#   界面刷新


if __name__ == '__main__':
	app = wx.App()
	main = MyFrame(None)
	main.Show()
	app.MainLoop()
