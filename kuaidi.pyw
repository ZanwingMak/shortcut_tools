# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()

    def render(self,express,yundanhao):
        self.express = express
        self.yundanhao = yundanhao
        self.start()

    def run(self):
        kuaidi.text.clear()
        kuaidi.update_msg(u'正在查询...')
        url = 'http://wap.kuaidi100.com/wap_result.jsp?rand=20120517&id=%s&fromWeb=null&&postid=%s'%(self.express,self.yundanhao)
        try:
            html = requests.get(url,timeout=25).text
            soup = BeautifulSoup(html,'lxml')
            kuaidi.text.clear()
            text = str(soup.find_all('p')[3:-1])
            #print text
            if '\u6b64\u5355\u53f7\u6682\u65e0\u7269\u6d41\u4fe1\u606f\uff0c\u8bf7\u7a0d\u540e\u518d\u67e5\u3002' in text:
                kuaidi.update_msg(u'此单号暂无物流信息，请稍后再查询。')
            elif '\u5355\u53f7\u975e\u6cd5' in text:
                kuaidi.update_msg(u'单号非法,不足5位或者超出20位。')
            elif '\u5355\u53f7\u4e0d\u6b63\u786e' in text:
                kuaidi.update_msg(u'单号不正确,单号由12-14位数字字母组成。')
            else:
                for each in soup.find_all('p')[3:-1]:
                    each = str(each)
                    each = each.replace('<p>','')
                    each = each.replace('<strong>','')
                    each = each.replace('</strong>','')
                    each = each.replace('<br/>','')
                    each = each.replace('</p>','')
                    each = each.replace('·','●')
                    #print each
                    kuaidi.update_msg(each.decode('utf-8'))
        except Exception as e:
            QMessageBox.information(None,u'发生异常',str(e))


class KUAIDI(QDialog):
    def __init__(self,parent=None):
        super(KUAIDI,self).__init__(parent)
        self.setWindowTitle(self.tr(u"快递物流信息查询"))

        mainLayout=QGridLayout(self)

        hb233 = QGridLayout()
        hb1 = QVBoxLayout()
        self.label1 = QLabel()
        self.label1.setText(self.tr(u"快递公司："))
        self.radio1 = QRadioButton(u'顺丰快递') # 创建单选框
        self.radio2 = QRadioButton(u'申通快递')
        self.radio3 = QRadioButton(u'韵达快递')
        self.radio4 = QRadioButton(u'中通快递')
        self.radio5 = QRadioButton(u'圆通快递')
        self.radio6 = QRadioButton(u'天天快递')
        self.radio7 = QRadioButton(u'百世汇通')
        self.radio8 = QRadioButton(u'宅急送')
        self.radio9 = QRadioButton(u'EMS')
        hb1.addWidget(self.label1)
        hb1.addWidget(self.radio1)
        hb1.addWidget(self.radio2)
        hb1.addWidget(self.radio3)
        hb1.addWidget(self.radio4)
        hb1.addWidget(self.radio5)
        hb1.addWidget(self.radio6)
        hb1.addWidget(self.radio7)
        hb1.addWidget(self.radio8)
        hb1.addWidget(self.radio9)

        hb2 = QVBoxLayout()
        self.label2 = QLabel()
        self.label2.setText(self.tr(u"快递物流信息："))
        self.text = QListWidget()
        hb2.addWidget(self.label2)
        hb2.addWidget(self.text)

        hb233.addLayout(hb1,0,0)
        hb233.addLayout(hb2,0,1)

        hb3 = QHBoxLayout()
        self.label3 = QLabel()
        self.label3.setText(self.tr(u"请输入物流快递的运单号："))
        self.yundanhao_edit = QLineEdit()
        self.btn_ok = QPushButton(self)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_ok.setText(self.tr("查询"))
        hb3.addWidget(self.label3)
        hb3.addWidget(self.yundanhao_edit)
        hb3.addWidget(self.btn_ok)

        mainLayout.addLayout(hb1,1,0)
        mainLayout.addLayout(hb233,2,0)
        mainLayout.addLayout(hb3,3,0)

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        yundanhao = (str(self.yundanhao_edit.text())).strip()
        if yundanhao.isdigit() == False:
            QMessageBox.information(self,u'错误',u'运单号必须为数字！')
        else:
            if self.radio1.isChecked():
                express = 'shunfeng'
            elif self.radio2.isChecked():
                express = 'shentong'
            elif self.radio3.isChecked():
                express = 'yunda'
            elif self.radio4.isChecked():
                express = 'zhongtong'
            elif self.radio5.isChecked():
                express = 'yuantong'
            elif self.radio6.isChecked():
                express = 'tiantian'
            elif self.radio7.isChecked():
                express = 'huitongkuaidi'
            elif self.radio8.isChecked():
                express = 'zhaijisong'
            elif self.radio9.isChecked():
                express = 'ems'
            else:
                QMessageBox.information(self,u'错误',u'请先选择快递公司！')
                return -1

            self.workThread1.render(express,yundanhao)
    def update_msg(self,msg):
        self.text.addItem(msg)#.decode('utf-8')
        self.text.setCurrentRow(self.text.count()-1)
    workThread1=WorkThread1()


app=QApplication(sys.argv)
kuaidi=KUAIDI()
kuaidi.setFixedSize(550,250)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/kuaidi.ico'), QIcon.Normal, QIcon.Off)
kuaidi.setWindowIcon(icon)
kuaidi.show()
app.exec_()
