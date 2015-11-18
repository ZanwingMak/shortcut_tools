# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import requests
import sys
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
reload(sys)
sys.setdefaultencoding('utf-8')

class YouDao(QDialog):
    def __init__(self,parent=None):
        super(YouDao,self).__init__(parent)
        self.setWindowTitle(self.tr("有道词典"))

        mainLayout=QGridLayout(self)
        
        hb1 = QHBoxLayout()
        self.text1 = QTextEdit(self)
        #self.text1.setFontFamily('Microsoft Yahei')
        #self.text1.setFontPointSize(16)

        hb1.addWidget(self.text1)
        
        hb2 = QHBoxLayout()
        self.label1 = QLabel(self)
        self.label1.setText(self.tr("请选择语言:"))
        self.combobox1 = QComboBox(self)
        language_list = [u'自动检测语言', u'中文 >> 英语', u'中文 >> 日语', u'中文 >> 韩语'\
               , u'中文 >> 法语', u'中文 >> 俄语', u'中文 >> 西班牙语', u'英语 >> 中文',\
                u'日语 >> 中文', u'韩语 >> 中文', u'法语 >> 中文', u'俄语 >> 中文', u'西班牙语 >> 中文']

        self.combobox1.addItems(language_list)
        self.btn1 = QPushButton(self)
        self.btn1.setText(self.tr("翻译"))
        self.btn1.clicked.connect(self.btn1_Clicked)
        hb2.addWidget(self.label1)
        hb2.addWidget(self.combobox1)
        hb2.addWidget(self.btn1)

        hb3 = QHBoxLayout()
        self.text2 = QTextEdit(self)
        self.text2.setFontFamily('Microsoft Yahei')
        self.text2.setFontPointSize(18)
        hb3.addWidget(self.text2)
        
        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)
        mainLayout.addLayout(hb3,2,0)


    def translate(self,language_code,sentence):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
        #print language_code,sentence
        data = {
            'type':language_code,
            'i':sentence,
            'doctype':'json',
            'xmlVersion':'1.8',
            'keyfrom':'fanyi.web',
            'ue':'UTF-8',
            'action':'FY_BY_CLICKBUTTON',
            'typoResult':'true'
        }
        content = requests.post(url,data).content
        #print content
        mydict = json.loads(content)
        #print mydict
        return mydict.get('translateResult')[0][0].get('tgt')

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn1_Clicked(self):
        language_code_list = ['AUTO',\
                              'ZH_CN2EN','ZH_CN2JA','ZH_CN2KR','ZH_CN2FR','ZH_CN2RU','ZH_CN2SP',\
                              'CN2EN_ZH','CN2JA_ZH','CN2KR_ZH','CN2FR_ZH','CN2RU_ZH','CN2SP_ZH']
        #返回Item数目
        #count = self.combobox1.count()
        #返回当前选择索引，从0开始
        pos = self.combobox1.currentIndex()
        #返回当前选择内容
        #text = self.combobox1.currentText()
        #print count,pos,text
        language_code = language_code_list[pos]
        #文本框内容
        sentence = str(self.text1.toPlainText())#要str强制类型转换才行，不然后只传第一个字符...
        translate_return = self.translate(language_code,sentence)
        self.text2.setText(translate_return)
                  
app=QApplication(sys.argv)  
youdao=YouDao()
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/youdao.ico'), QIcon.Normal, QIcon.Off)
youdao.setWindowIcon(icon)
youdao.show()
app.exec_()  
