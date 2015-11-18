# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, urllib, urllib2, json
reload(sys)
sys.setdefaultencoding('utf-8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

def check_url(check_url):
    #print check_url
    url = 'http://apis.baidu.com/bsb/bsb/lookup?ver=1.0&url=' + check_url
    req = urllib2.Request(url)
    req.add_header("apikey", "9beeec0d48be29fdcbb4ebdb359a64ec")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        #print(content)
        content_dict = json.loads(content)
        #print content_dict
        data = content_dict.get('result')[0]
        #print data
        the_url = data.get('url')
        the_result = int(data.get('main'))
        the_range  = int(data.get('range'))

        url_check.label3.setText(url_check.tr(the_url))

        if the_result == 0:
            url_check.label5.setText(url_check.tr(u'[未知]未检查过该网站，现已将此网址收录至检测系统等待检测。'))
        elif the_result == 1 or the_result == 2:
            url_check.label5.setText(url_check.tr(u'[安全]经检测未发现威胁，可以安全访问。'))
        elif the_result >= 3:
            url_check.label5.setText(url_check.tr(u'[危险]经检测发现威胁，建议不要访问。'))
        else:
            url_check.label5.setText(url_check.tr(u'[检测失败]未知错误...'))

        if the_range == 1:
            url_check.label7.setText(url_check.tr(u'site级别'))
        elif the_range == 2:
            url_check.label7.setText(url_check.tr(u'link级别'))
        elif the_range == 3:
            url_check.label7.setText(url_check.tr(u'domain级别'))
        else:
            url_check.label7.setText(url_check.tr(u'[检测失败]未知错误...'))

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()
    def run(self):
        check_url(str(url_check.edit.text()))
        self.trigger.emit()

class URL_CHECK(QDialog):
    def __init__(self,parent=None):
        super(URL_CHECK,self).__init__(parent)
        self.setWindowTitle(self.tr(u"网址安全检测"))

        mainLayout=QGridLayout(self)

        hb1 = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText(self.tr(u"请输入网址(无需填写http://)："))
        self.edit = QLineEdit(self)
        self.btn_ok = QPushButton(self)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_ok.setText(self.tr("检测"))
        hb1.addWidget(self.label1)
        hb1.addWidget(self.edit)
        hb1.addWidget(self.btn_ok)

        hb2 = QHBoxLayout()
        self.label2 = QLabel()
        self.label2.setText(self.tr(u"网址："))
        self.label3 = QLabel()
        hb2.addWidget(self.label2)
        hb2.addWidget(self.label3)

        hb3 = QHBoxLayout()
        self.label4 = QLabel()
        self.label4.setText(self.tr(u"安全属性："))
        self.label5 = QLabel()
        hb3.addWidget(self.label4)
        hb3.addWidget(self.label5)

        hb4 = QHBoxLayout()
        self.label6 = QLabel()
        self.label6.setText(self.tr(u"安全作用域："))
        self.label7 = QLabel()
        hb4.addWidget(self.label6)
        hb4.addWidget(self.label7)

        mainLayout.addLayout(hb1,1,0)
        mainLayout.addLayout(hb2,2,0)
        mainLayout.addLayout(hb3,3,0)
        mainLayout.addLayout(hb4,4,0)

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        self.workThread1.start()

    workThread1=WorkThread1()


app=QApplication(sys.argv)
url_check=URL_CHECK()
#url_check.setFixedSize(450,130)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/url_check.ico'), QIcon.Normal, QIcon.Off)
url_check.setWindowIcon(icon)
url_check.show()
app.exec_()


