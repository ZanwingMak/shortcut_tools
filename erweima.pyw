# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
import urllib,os,time,urllib2, json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
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
        #if '\\' in self.msg: ##因为\\会转义成\
        #    xiegangzhuanyi = (self.msg).split('\\')
        #    self.msg = ''
        #    for i in range(len(xiegangzhuanyi)-1):
        #        xiegangzhuanyi[i] = xiegangzhuanyi[i] + '\\\\'
        #    for i in range(len(xiegangzhuanyi)):
        #       self.msg = self.msg + xiegangzhuanyi[i]
        if 'http://' in self.msg:  #用了这个发现上面的\不会转义了!?        
            del_head = (self.msg).split('http://')
            self.msg = ''
            for i in range(len(del_head)):
                self.msg = self.msg + del_head[i]
        #print self.msg
        self.start()
    def run(self):
        self.msg = urllib.quote(self.msg)
        #print self.msg
        url = 'http://apis.baidu.com/3023/qr/qrcode?size=8&qr=' + self.msg
        req = urllib2.Request(url)
        req.add_header("apikey", "9beeec0d48be29fdcbb4ebdb359a64ec")
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            content_dict = json.loads(content)
            erweima_img_url = content_dict.get('url')
            time_temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            a1 = str(time_temp)[0:4]
            a2 = str(time_temp)[5:7]
            a3 = str(time_temp)[8:10]
            a4 = str(time_temp)[11:13]
            a5 = str(time_temp)[14:16]
            a6 = str(time_temp)[17:19]
            now_time = (a1+a2+a3+a4+a5+a6)
            try:
                save_path = QFileDialog.getSaveFileName(None,self.tr("请选择二维码保存的位置"),"./"+now_time,"JPEG(*.jpg)")
                with open(save_path,'wb') as img:
                    urllib.urlretrieve(erweima_img_url,save_path)
                os.startfile(save_path)
            except:
                pass

class ERWEIMA(QDialog):
    def __init__(self,parent=None):
        super(ERWEIMA,self).__init__(parent)
        self.window_move() #窗口显示位置
        self.setWindowTitle(self.tr(u'二维码'))
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

        mainLayout=QGridLayout(self)

        hb1 = QHBoxLayout()
        self.lb1 = QLabel()
        self.lb1.setText(u'请输入要转换成二维码的信息:')
        self.btn_ok = QPushButton()
        self.btn_ok.setText(self.tr("马上生成"))
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        hb1.addWidget(self.lb1)
        hb1.addWidget(self.btn_ok)

        hb2 = QHBoxLayout()
        self.msg_edit = QLineEdit()
        hb2.addWidget(self.msg_edit)

        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)

        # 窗口显示位置
    def window_move(self):
        screen = QDesktopWidget().screenGeometry()
        #size = self.geometry()
        #print screen.width(),screen.height()
        #print size.width(),size.height()
        self.move( (screen.width()-300)/2 , (screen.height()-100)/2 )

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        self.workThread1.render(self.msg_edit.text())

    workThread1=WorkThread1()


app=QApplication(sys.argv)
erweima=ERWEIMA()
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/erweima.ico'), QIcon.Normal, QIcon.Off)
erweima.setWindowIcon(icon)
erweima.setFixedSize(300,100)
erweima.show()
app.exec_()
