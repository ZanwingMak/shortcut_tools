# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ctypes import *
import poplib
from email.parser import Parser
from email.header import decode_header
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import threading
import thread
import smtplib
import time
import os
import sys
import random
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
reload(sys)
sys.setdefaultencoding('utf-8')

class YuanCheng(QDialog):
    def __init__(self,parent=None):
        super(YuanCheng,self).__init__(parent)
        self.setWindowTitle(self.tr("远程指令(锁屏、关机、重启)"))
        self.thread = Worker() ###

        mainLayout=QGridLayout(self)
        #hb1 = QHBoxLayout()
        hb1 = QVBoxLayout()
        self.shuoming_biaoti = QLabel(self)
        self.shuoming_biaoti.setText(self.tr("【说明】"))
        self.shuomingtext = QLabel(self)
        self.shuomingtext.setText(self.tr("本远程指令程序的原理是通过本地登录邮箱,检测是否接收到指令邮件,因此需要准备1个或2个邮箱账号并开启POP3、SMTP服务\n否则将无法外部操作邮箱并正常使用此程序!地址可以自动识别并帮您填写,如不正确请自行填写!"))
        self.zhilingtextlist = QLabel(self)
        self.zhilingtextlist.setText(self.tr("【支持的指令有：suoping、guanji、chongqi ,任意邮箱在邮件标题输入指令并发送到下面的邮箱即可,自己发给自己也可以】"))

        hb1.addWidget(self.shuoming_biaoti)
        hb1.addWidget(self.shuomingtext)
        hb1.addWidget(self.zhilingtextlist)

        hb2 = QHBoxLayout()
        self.zhilingjieshou_mail_label = QLabel(self)
        self.zhilingjieshou_mail_label.setText(self.tr("用来接收指令的邮箱地址："))
        self.zhilingjieshou_mail_edit = QLineEdit()
        self.zhilingjieshoupassword_mail_label = QLabel(self)
        self.zhilingjieshoupassword_mail_label.setText(self.tr("密码："))

        self.zhilingjieshoupassword_mail_edit = QLineEdit()
        self.zhilingjieshoupassword_mail_edit.setEchoMode(QLineEdit.Password) #密文密码
        #self.zhilingjieshoupassword_mail_edit.setValidator(QRegExpValidator(Qt.QRegExp("[A-Za-z0-9]+"),self))

        hb2.addWidget(self.zhilingjieshou_mail_label)
        hb2.addWidget(self.zhilingjieshou_mail_edit)
        hb2.addWidget(self.zhilingjieshoupassword_mail_label)
        hb2.addWidget(self.zhilingjieshoupassword_mail_edit)

        hb3 = QHBoxLayout()
        self.zhilingjieshou_smtpaddr_label = QLabel(self)
        self.zhilingjieshou_smtpaddr_label.setText(self.tr("SMTP服务器地址:"))
        self.zhilingjieshou_smtpaddr_edit = QLineEdit()
        self.zhilingjieshou_popaddr_label = QLabel(self)
        self.zhilingjieshou_popaddr_label.setText(self.tr("POP服务器地址:"))
        self.zhilingjieshou_popaddr_edit = QLineEdit()
        self.auto_btn = QPushButton(self)
        self.auto_btn.setText(self.tr("自动识别"))
        self.auto_btn.clicked.connect(self.auto_btn_Clicked)

        hb3.addWidget(self.zhilingjieshou_smtpaddr_label)
        hb3.addWidget(self.zhilingjieshou_smtpaddr_edit)
        hb3.addWidget(self.zhilingjieshou_popaddr_label)
        hb3.addWidget(self.zhilingjieshou_popaddr_edit)
        hb3.addWidget(self.auto_btn)

        hb4 = QHBoxLayout()
        self.isSSL_checkbox = QCheckBox(u"使用SSL加密安全传输功能")
        self.isSSL_checkbox.setChecked(True)
        self.ok_btn = QPushButton(self)
        self.ok_btn.setText(self.tr("启动"))
        self.ok_btn.clicked.connect(self.ok_btn_Clicked)
        self.clear_ListWidgetContent_btn = QPushButton(self)
        self.clear_ListWidgetContent_btn.setText(self.tr("清屏"))
        self.clear_ListWidgetContent_btn.clicked.connect(self.clear_ListWidgetContent_btn_Clicked)
        self.clear_btn = QPushButton(self)
        self.clear_btn.setText(self.tr("重置"))
        self.clear_btn.clicked.connect(self.clear_btn_Clicked)

        hb4.addWidget(self.isSSL_checkbox)
        hb4.addWidget(self.ok_btn)
        hb4.addWidget(self.clear_ListWidgetContent_btn)
        hb4.addWidget(self.clear_btn)

        hb5=QVBoxLayout()
        self.ListWidgetContent1 = QListWidget(self)
        hb5.addWidget(self.ListWidgetContent1)

        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)
        mainLayout.addLayout(hb3,2,0)
        mainLayout.addLayout(hb4,3,0)
        mainLayout.addLayout(hb5,4,0)

    def auto_btn_Clicked(self):
        mail_check = (self.zhilingjieshou_mail_edit.text().split('@'))[-1].split('.')[0]
        self.zhilingjieshou_smtpaddr_edit.setText('smtp.%s.com' % mail_check)
        self.zhilingjieshou_popaddr_edit.setText('pop.%s.com' % mail_check)

    def ok_btn_Clicked(self):
        self.ok_btn.setDisabled(True)
        pc_address = str(self.zhilingjieshou_mail_edit.text())
        password = str(self.zhilingjieshoupassword_mail_edit.text())
        smtp_server = str(self.zhilingjieshou_smtpaddr_edit.text())
        pop_server = str(self.zhilingjieshou_popaddr_edit.text())
        if self.isSSL_checkbox.isChecked():
            ifusessl = 'yes'
        else:
            ifusessl = 'no'

        self.ListWidgetContent1.addItem(u'服务正在开启...')
        self.ListWidgetContent1.setCurrentRow(yuancheng.ListWidgetContent1.count()-1)
        self.thread.render(pc_address,password,smtp_server,pop_server,ifusessl)

    def clear_ListWidgetContent_btn_Clicked(self):
        self.ListWidgetContent1.clear()

    def clear_btn_Clicked(self):
        self.zhilingjieshou_mail_edit.setText('')
        self.zhilingjieshoupassword_mail_edit.setText('')
        self.zhilingjieshou_smtpaddr_edit.setText('')
        self.zhilingjieshou_popaddr_edit.setText('')
        self.isSSL_checkbox.setChecked(False)

    def update_msg_list(self,msg):
        self.ListWidgetContent1.addItem(msg)#.decode('utf-8')
        self.ListWidgetContent1.setCurrentRow(yuancheng.ListWidgetContent1.count()-1)

    #退出确认
    def closeEvent(self, event):
        rely = QMessageBox.question(self,u'退出',u'确定要关闭吗?',QMessageBox.Yes,QMessageBox.No)
        if rely == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

class Worker(QThread):
    def __int__(self, parent = None):
        QThread.__init__(self, parent)
    def render(self,pc_address,password,smtp_server,pop_server,ifusessl):
        self.pc_address = pc_address
        self.password = password
        self.smtp_server = smtp_server
        self.pop_server = pop_server
        self.ifusessl = ifusessl
        self.start()

    def sendMsg(self,msg):
        yuancheng.update_msg_list(msg)

    def run(self):
            def guess_charset(msg):
                # 先从msg对象获取编码:
                charset = msg.get_charset()
                # 如果获取不到，再从Content-Type字段获取:
                if charset is None:
                    content_type = msg.get('Content-Type', '').lower()
                    pos = content_type.find('charset=')
                    if pos >= 0:
                        charset = content_type[pos + 8:].strip()
                return charset

            #邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
            def decode_str(s):
                value, charset = decode_header(s)[0]
                if charset:
                    value = value.decode(charset)
                return value

            def get_info(msg):
                    for header in ['From','Subject']:
                            value = msg.get(header, '')
                            if value:
                                if header=='Subject':
                                    subject = decode_str(value)
                                else:
                                    hdr, from_email = parseaddr(value)
                    return from_email,subject

            def reply(text,zhilingduan_email,pc_address):
                    def format_address(s):
                        name,address = parseaddr(s)
                        return formataddr((Header(name,'utf-8').encode(),\
                                   address.encode('utf-8') if isinstance(address,unicode) else address))

                    msg = MIMEText(text,'plain','utf-8')
                    msg['From'] = format_address(u'指令接收端 <%s>'% pc_address)
                    msg['To'] = format_address(u'指令来源 <%s>' % zhilingduan_email)
                    msg['Subject'] = Header(u'电脑发来远程指令信息反馈','utf-8').encode()

                    serve_smtp = smtplib.SMTP(self.smtp_server,25)
                    serve_smtp.set_debuglevel(1)
                    serve_smtp.login(pc_address,self.password)
                    serve_smtp.sendmail(pc_address,[zhilingduan_email],msg.as_string())
                    serve_smtp.quit()

            def play(from_email,subject,pc_address,length):
                if from_email == pc_address:
                    count = length
                else:
                    count = length
                if subject == 'suoping':
                    text = u'已收到远程指令：锁屏...'
                    fankui = u'正在发送反馈邮件...'
                    self.sendMsg(fankui)
                    reply(text,from_email,pc_address)
                    self.sendMsg(text)
                    #print text
                    time.sleep(2)
                    try:
                            text = u'正在执行远程锁屏指令...'
                            fankui = u'正在发送反馈邮件...'
                            self.sendMsg(fankui)
                            reply(text,from_email,pc_address)
                            self.sendMsg(text)
                            time.sleep(2)
                            user32 = windll.LoadLibrary('user32.dll')
                            user32.LockWorkStation()
                    except:
                            text = u'远程指令执行失败，请重试...'
                            fankui = u'正在发送反馈邮件...'
                            self.sendMsg(fankui)
                            reply(text,from_email,pc_address)
                            self.sendMsg(text)
                            time.sleep(2)
                    return('ok',count)
                elif subject == 'guanji':                    
                         text = u'已收到远程指令：关机...'
                         fankui = u'正在发送反馈邮件...'
                         self.sendMsg(fankui)
                         reply(text,from_email,pc_address)
                         self.sendMsg(text)
                         time.sleep(2)
                         try:
                                text = u'正在执行远程关机指令...'
                                fankui = u'正在发送反馈邮件...'
                                self.sendMsg(fankui)
                                reply(text,from_email,pc_address)
                                self.sendMsg(text)
                                time.sleep(2)
                                os.system('shutdown -f -s -t 10 -c Closing...')
                         except:
                                text = u'远程指令执行失败，请重试...'                                
                                fankui = u'正在发送反馈邮件...'
                                self.sendMsg(fankui)
                                reply(text,from_email,pc_address)
                                self.sendMsg(text)
                                time.sleep(2)
                        
                         return('ok',count)
                elif subject == 'chongqi':
                        text = u'已收到远程指令：重启...'                        
                        fankui = u'正在发送反馈邮件...'
                        self.sendMsg(fankui)
                        reply(text,from_email,pc_address)
                        self.sendMsg(text)
                        time.sleep(2)
                        try:
                                text = u'正在执行远程重启指令...'                                
                                fankui = u'正在发送反馈邮件...'
                                self.sendMsg(fankui)
                                reply(text,from_email,pc_address)
                                self.sendMsg(text)
                                time.sleep(2)
                                os.system('shutdown -f -r -t 10 -c Rstarting...')
                        except:
                                text = u'远程指令执行失败，请重试...'
                                fankui = u'正在发送反馈邮件...'
                                self.sendMsg(fankui)
                                self.sendMsg(text)
                                reply(text,from_email,pc_address)
                                time.sleep(2)
                        return('ok',count)
                else:
                    return('no',count)                

            while True:
                try:
                    # 连接到POP服务器:
                    self.sendMsg(u'正在连接POP服务器...')
                    try:
                        if self.ifusessl == 'yes':
                            server = poplib.POP3_SSL(self.pop_server)
                            self.sendMsg(u'正在使用SSL安全加密服务...')
                        else:
                            server = poplib.POP3(self.pop_server)
                    except:
                        pass
                    # 身份认证:
                    self.sendMsg(u'正在认证身份...')
                    server.user(self.pc_address)
                    server.pass_(self.password)
                    self.sendMsg(u'身份认证成功...')
                    # list()返回所有邮件的编号:
                    resp, mails, octets = server.list()
                    #print resp,mails,octets
                    self.sendMsg(u'正在获取邮件...')
                    # 获取最新一封邮件, 注意索引号从1开始:
                    length = len(mails)
                    resp, lines, octets = server.retr(length)#而len(mails)则相反方向开始,由最大长度开始，即从最新开始数
                    #print resp, lines, octets
                    self.sendMsg(u'正在解析邮件...')
                    # 解析邮件:
                    #print lines
                    msg = Parser().parsestr('\r\n'.join(lines))
                    # 获取邮件信息:
                    self.sendMsg(u'正在获取邮件信息...')
                    from_email,subject = get_info(msg)
                    #执行远程命令
                    #self.sendMsg(u'准备执行远程指令...')
                    tf,count = play(from_email,subject,self.pc_address,length)
                    print tf,count
                    if tf == 'ok':
                        server.dele(count) #删除邮件
                    else:
                        pass
                    # 关闭连接:
                    self.sendMsg(u'正在本次关闭连接...')
                    server.quit()
                    self.sendMsg(u'连接已关闭,正在等候下次连接(30~60s)...')
                    time.sleep(30+random.randint(0,30))
                except Exception as e:
                    if 'Syntax' not in str(e) and 'EOF' not in str(e):
                        self.sendMsg(str(e).decode('gbk'))
                    self.sendMsg(u'正在重试,需等候下次连接(60~120s)...')
                    time.sleep(60+random.randint(0,60)) #60+n秒检测一次，最好设置成5分钟！


app=QApplication(sys.argv)
yuancheng=YuanCheng()
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/yuancheng.ico'), QIcon.Normal, QIcon.Off)
yuancheng.setWindowIcon(icon)
yuancheng.show()
app.exec_()






