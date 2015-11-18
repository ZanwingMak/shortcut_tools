# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
import urllib2, json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import webbrowser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()

    def render(self,msg):
        self.msg = str(msg).strip()
        self.start()

    def cutting(self,string,width):
        return [string[x:x+width] for x in range(0,len(string),width)]

    def run(self):
        key = '498f2a785c96aca4ef85bf63a6060c0e'
        url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+self.msg
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            content_dict = json.loads(content)
            code = content_dict.get('code')
            text = content_dict.get('text')
            if code == 100000:#文本类数据
                if u'天气' in self.msg:
                    try:
                        robot.ListWidgetContent.clear()
                        weather_list = text.split(':')
                        robot.update_msg(weather_list[0],True)
                        the_weather = weather_list[1].split(';')
                        for i in range(len(the_weather)):
                            robot.update_msg(the_weather[i],True)
                    except:
                        pass
                elif len(text) > 35:
                    robot.ListWidgetContent.clear()
                    cutting_string_list = self.cutting(text,26)
                    count = len(cutting_string_list)
                    for i in range(count):
                        robot.update_msg(cutting_string_list[i],False)
                else:
                    robot.update_msg(text,True)

            elif code == 305000:#列车
                train_list = content_dict.get('list')
                count = len(train_list)
                if count:
                    robot.ListWidgetContent.clear()
                    for i in range(count):
                        this_train = train_list[i]
                        robot.update_msg(u'列车号：'+this_train.get('trainnum'),False)
                        robot.update_msg(u'出发点：'+this_train.get('start')+u' ——> '+u'到达点：'+this_train.get('terminal'),False)
                        robot.update_msg(u'发车时间：'+this_train.get('starttime')+u' ——> '+u'到达时间：'+this_train.get('endtime'),False)
                        if i != count-1:
                            robot.update_msg(u'--------------------',False)
            elif code == 200000:#网址类数据
                robot.update_msg(text,True)
                robot.update_msg(u'[链接]'+content_dict.get('url'),True)
            elif code == 302000:#新闻
                news_list = content_dict.get('list')
                count = len(news_list)
                robot.ListWidgetContent.clear()
                for i in range(count):
                    this_news = news_list[i]
                    robot.update_msg(u'[标题]'+this_news.get('article'),False)
                    robot.update_msg(u'[详情]'+this_news.get('detailurl'),False)
                    if i != count-1:
                            robot.update_msg(u'--------------------',False)
            elif code == 308000:#菜谱、视频、小说
                food_list = content_dict.get('list')
                count = len(food_list)
                robot.ListWidgetContent.clear()
                for i in range(count):
                    this_food = food_list[i]
                    robot.update_msg(u'[名字]'+this_food.get('name'),False)
                    robot.update_msg(u'[图片]'+this_food.get('icon'),False)
                    robot.update_msg(u'[链接]'+this_food.get('detailurl'),False)
                    if i != count-1:
                            robot.update_msg(u'--------------------',False)
            elif code == 40001:
                robot.update_msg(u'[系统提示]key的长度错误（32位）',True)
            elif code == 40002:
                robot.update_msg(u'[系统提示]请求内容为空',True)
            elif code == 40003:
                robot.update_msg(u'[系统提示]key错误或帐号未激活',True)
            elif code == 40004:
                robot.update_msg(u'[系统提示]当天请求次数已用完',True)
            elif code == 40005:
                robot.update_msg(u'[系统提示]暂不支持该功能',True)
            elif code == 40006:
                robot.update_msg(u'[系统提示]服务器升级中',True)
            elif code == 40007:
                robot.update_msg(u'[系统提示]服务器数据格式异常',True)

class ROBOT(QDialog):
    def __init__(self,parent=None):
        super(ROBOT,self).__init__(parent)
        self.window_move() #窗口显示位置
        self.setWindowTitle(self.tr(u'智能姬 [不要请求过快QAQ会崩溃]'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        mainLayout=QGridLayout(self)

        hb1 = QHBoxLayout()
        self.lb1 = QLabel()
        self.lb1.setText(u'使用方法：交流"你好",查天气"深圳今天的天气",查火车"今天广州\n到北京的火车(飞机)",做菜"番茄炒蛋怎么做",搜图"周杰伦的图片"\n提示：选中带有网址的信息可点击"用浏览器打开"网页。')
        hb1.addWidget(self.lb1)

        hb2 = QHBoxLayout()
        self.msg = QLineEdit(self)
        self.btn_ok = QPushButton(self)
        self.btn_ok.setText(self.tr("确定"))
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_brower = QPushButton(self)
        self.btn_brower.setText(self.tr("用浏览器打开"))
        self.btn_brower.clicked.connect(self.btn_brower_Clicked)
        hb2.addWidget(self.msg)
        hb2.addWidget(self.btn_ok)
        hb2.addWidget(self.btn_brower)

        hb3 = QHBoxLayout()
        self.ListWidgetContent= QListWidget(self)
        hb3.addWidget(self.ListWidgetContent)

        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)
        mainLayout.addLayout(hb3,2,0)

    # 窗口显示位置
    def window_move(self):
        screen = QDesktopWidget().screenGeometry()
        #size = self.geometry()
        #print screen.width(),screen.height()
        #print size.width(),size.height()
        self.move( (screen.width()-360)/2 , (screen.height()-280)/2 )

    def btn_ok_Clicked(self):
        self.workThread1.render(self.msg.text())

    def btn_brower_Clicked(self):
        index = self.ListWidgetContent.currentRow()
        obj = self.ListWidgetContent.item(index)
        text = obj.text()
        if 'http' in text:
            url = text[4:]
            webbrowser.open_new_tab(url)
        else:
            pass

     #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def update_msg(self,msg,bool):
        self.ListWidgetContent.addItem(msg)#.decode('utf-8')
        if bool == True:
            self.ListWidgetContent.setCurrentRow(self.ListWidgetContent.count()-1)
        else:
            pass

    workThread1=WorkThread1()

app=QApplication(sys.argv)
robot=ROBOT()
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/robot.ico'), QIcon.Normal, QIcon.Off)
robot.setWindowIcon(icon)
robot.setFixedSize(380,280)
robot.show()
app.exec_()
