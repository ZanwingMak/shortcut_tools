# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import requests,re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()

    def render(self,phoneNum):
        self.phoneNum = phoneNum
        self.start()

    def run(self):
        url = 'http://virtual.paipai.com/extinfo/GetMobileProductInfo?mobile=%s&amount=10000'%self.phoneNum
        mobile_data = requests.get(url).text
        r = r'\'.*?\''  # 加?是为了使用懒惰模式,贪婪模式会直接匹配到最后的引号
        data = re.findall(r,mobile_data)
        #print data
        mobile_number = (data[0])[1:-1]
        isp = (data[2])[1:-1]
        province = (data[1])[1:-1]
        cityname = (data[7])[1:-1]
        phone_num_info_check.label3.setText(mobile_number)
        phone_num_info_check.label3.setAlignment(Qt.AlignCenter)#居中对齐
        phone_num_info_check.label5.setText(isp)
        phone_num_info_check.label5.setAlignment(Qt.AlignCenter)#居中对齐
        phone_num_info_check.label7.setText(province)
        phone_num_info_check.label7.setAlignment(Qt.AlignCenter)#居中对齐
        phone_num_info_check.label9.setText(cityname)
        phone_num_info_check.label9.setAlignment(Qt.AlignCenter)#居中对齐


class PHONE_NUM_INFO_CHECK(QDialog):
    def __init__(self,parent=None):
        super(PHONE_NUM_INFO_CHECK,self).__init__(parent)
        self.setWindowTitle(self.tr(u"手机号码归属地查询"))

        mainLayout=QGridLayout(self)

        hb1 = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText(self.tr(u"手机号："))
        self.edit = QLineEdit(self)
        self.btn_ok = QPushButton(self)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_ok.setText(self.tr("查询"))
        hb1.addWidget(self.label1)
        hb1.addWidget(self.edit)
        hb1.addWidget(self.btn_ok)

        hb2 = QHBoxLayout()
        self.label2 = QLabel()
        self.label2.setText(self.tr(u"手机号："))
        self.label3 = QLabel()
        hb2.addWidget(self.label2)
        hb2.addWidget(self.label3)

        hb3 = QHBoxLayout()
        self.label4 = QLabel()
        self.label4.setText(self.tr(u"运营商："))
        self.label5 = QLabel()
        hb3.addWidget(self.label4)
        hb3.addWidget(self.label5)

        hb4 = QHBoxLayout()
        self.label6 = QLabel()
        self.label6.setText(self.tr(u"省   份："))
        self.label7 = QLabel()
        hb4.addWidget(self.label6)
        hb4.addWidget(self.label7)

        hb5 = QHBoxLayout()
        self.label8 = QLabel()
        self.label8.setText(self.tr(u"城   市："))
        self.label9 = QLabel()
        hb5.addWidget(self.label8)
        hb5.addWidget(self.label9)

        mainLayout.addLayout(hb1,1,0)
        mainLayout.addLayout(hb2,2,0)
        mainLayout.addLayout(hb3,3,0)
        mainLayout.addLayout(hb4,4,0)
        mainLayout.addLayout(hb5,5,0)

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        phoneNum = (str(self.edit.text())).strip()
        if len(phoneNum) != 11:
            QMessageBox.information(self,u'错误',u'手机号码必须为11位！！！')
        elif phoneNum.isdigit() == False:
            QMessageBox.information(self,u'错误',u'手机号码必须为数字！！！')
        else:
            self.workThread1.render(phoneNum)

    workThread1=WorkThread1()


app=QApplication(sys.argv)
phone_num_info_check=PHONE_NUM_INFO_CHECK()
phone_num_info_check.setFixedSize(300,150)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/shoujiguishu.ico'), QIcon.Normal, QIcon.Off)
phone_num_info_check.setWindowIcon(icon)
phone_num_info_check.show()
app.exec_()
