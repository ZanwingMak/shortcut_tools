#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
import os
import sys
import datetime
import time
import logging
import urllib
import cookielib
import urllib2
reload(sys)
sys.setdefaultencoding("utf-8")
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class HttpClient:
    __cookie = cookielib.CookieJar()
    __req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
    __req.addheaders = [
        ('Accept', 'application/javascript, */*;q=0.8'),
        ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
    ]
    urllib2.install_opener(__req)

    def Get(self, url, refer=None):
        try:
            req = urllib2.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req).read()
        except urllib2.HTTPError, e:
            return e.read()

    def Post(self, url, data, refer=None):
        try:
            req = urllib2.Request(url, urllib.urlencode(data))
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req).read()
        except urllib2.HTTPError, e:
            return e.read()

    def Download(self, url, file):
        output = open(file, 'wb')
        output.write(urllib2.urlopen(url).read())
        output.close()

#   def urlencode(self, data):
#       return urllib.quote(data)

    def getCookie(self, key):
        for c in self.__cookie:
            if c.name == key:
                return c.value
        return ''

    def setCookie(self, key, val, domain):
        ck = cookielib.Cookie(version=0, name=key, value=val, port=None, port_specified=False, domain=domain, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
        self.__cookie.set_cookie(ck)
#self.__cookie.clear() clean cookie
# vim : tabstop=2 shiftwidth=2 softtabstop=2 expandtab

# CONFIGURATION FIELD
checkFrequency = 180
#check every k seconds
# STOP EDITING HERE
HttpClient_Ist = HttpClient()
UIN = 0
skey = ''
Referer = 'http://user.qzone.qq.com/'
QzoneLoginUrl = 'http://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=http%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&pt_qzone_sig=1&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=http%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=http%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html'

initTime = time.time()

logging.basicConfig(filename='QQkongjian_log.log', level=logging.DEBUG, format='%(asctime)s  %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

def getAbstime():
    return int(time.time())

def date_to_millis(d):
    return int(time.mktime(d.timetuple())) * 1000

def getReValue(html, rex, er, ex):
    v = re.search(rex, html)

    if v is None:
        logging.error(er)

        if ex:
            raise Exception, er
        return ''

    return v.group(1)

# -----------------
# 登陆
# -----------------
class Login(HttpClient):
    MaxTryTime = 5

    def __init__(self, vpath, qq=0):
        global UIN, Referer, skey
        self.VPath = vpath  # QRCode保存路径
        AdminQQ = int(qq)
        qqkongjian.update_msg(u'正在获取登录页面...')
        logging.critical("正在获取登录页面")
        self.setCookie('_qz_referrer','qzone.qq.com','qq.com')
        self.Get(QzoneLoginUrl,'http://qzone.qq.com/')
        StarTime = date_to_millis(datetime.datetime.utcnow())
        T = 0
        while True:
            T = T + 1
            self.Download('http://ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&daid=5', self.VPath)
            LoginSig = self.getCookie('pt_login_sig')
            qqkongjian.update_msg(u'[{0}] 获取二维码成功...'.format(T))
            logging.info('[{0}] 获取二维码成功...'.format(T))
            qqkongjian.update_msg(u'[{0}] 请打开手机QQ安全中心扫描屏幕上的二维码或本目录下的v.png的二维码进行登录...'.format(T))
            logging.info('[{0}] 请打开手机QQ安全中心扫描屏幕上的二维码或本目录下的v.png的二维码进行登录...'.format(T))
            #img = Image.open("v.png")#图像路径
            #img.show()
            os.startfile('v.png')
            #qqkongjian.show_erweima()
            #qqkongjian.lb2.setPixmap(QPixmap("./v.png"))
            while True:
                html = self.Get('http://ptlogin2.qq.com/ptqrlogin?u1=http%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-{0}&js_ver=10131&js_type=1&login_sig={1}&pt_uistyle=32&aid=549000912&daid=5&pt_qzone_sig=1'.format(date_to_millis(datetime.datetime.utcnow()) - StarTime, LoginSig), QzoneLoginUrl)
                # logging.info(html)
                ret = html.split("'")
                if ret[1] == '65' or ret[1] == '0':  # 65: QRCode 失效, 0: 验证成功, 66: 未失效, 67: 验证中
                    break
                time.sleep(2)
            if ret[1] == '0' or T > self.MaxTryTime:
                break

        if ret[1] != '0':
            raise ValueError, "RetCode = "+ret['retcode']
            return
        qqkongjian.update_msg(u'二维码已扫描，正在登录...')
        logging.critical("二维码已扫描，正在登录")

        # 删除QRCode文件
        if os.path.exists(self.VPath):
            os.remove(self.VPath)

        # 记录登陆账号的昵称
        tmpUserName = ret[11]

        self.Get(ret[5])
        UIN = getReValue(ret[5], r'uin=([0-9]+?)&', 'Fail to get QQ number', 1)
        Referer = Referer+str(UIN)
        skey = self.getCookie('skey')
        qqkongjian.update_msg(u"登录成功,用户名: "+str(tmpUserName))
        logging.critical("登录成功,用户名: "+str(tmpUserName))
        qqkongjian.update_msg(u'正在自动点赞,请不要关闭程序,可以把该程序最小化哦...[检测时间间隔为3分钟]')

# -----------------
# 计算g_tk
# -----------------
def utf8_unicode(c):
    if len(c)==1:
        return ord(c)
    elif len(c)==2:
        n = (ord(c[0]) & 0x3f) << 6
        n += ord(c[1]) & 0x3f
        return n
    elif len(c)==3:
        n = (ord(c[0]) & 0x1f) << 12
        n += (ord(c[1]) & 0x3f) << 6
        n += ord(c[2]) & 0x3f
        return n
    else:
        n = (ord(c[0]) & 0x0f) << 18
        n += (ord(c[1]) & 0x3f) << 12
        n += (ord(c[2]) & 0x3f) << 6
        n += ord(c[3]) & 0x3f
        return n

def getGTK(skey):
    hash = 5381
    for i in range(0,len(skey)):
        hash += (hash << 5) + utf8_unicode(skey[i])
    return hash & 0x7fffffff
# -----------------
# LIKE
# -----------------
def like(unikey,curkey,dataid,time):
    reqURL = 'http://w.qzone.qq.com/cgi-bin/likes/internal_dolike_app?g_tk='+str(getGTK(skey))
    data = (
            ('qzreferrer', Referer),
            ('opuin', UIN),
            ('unikey', str(unikey)),
            ('curkey', str(curkey)),
            ('from', '1'),
            ('appid', '311'),
            ('typeid', '0'),
            ('abstime', str(time)),
            ('fid', str(dataid)),
            ('active', '0'),
            ('fupdate', '1')
        )
    rsp = HttpClient_Ist.Post(reqURL, data, Referer)
    getReValue(rsp, r'"code":(0)', 'Fail to like unikey='+str(unikey)+';curkey='+str(curkey)+';fid='+str(dataid), 0)

# -----------------
# 主函数
# -----------------
def MsgHandler():
    html=HttpClient_Ist.Get(Referer,Referer)
    fkey=re.findall(r'<div class="f-item f-s-i" id=".*?" data-feedsflag=.*?" data-iswupfeed=".*?" data-key="(.*?)" data-specialtype=.*?" data-extend-info=".*?">',html)
    if not fkey:
        raise Exception, 'Fail to find any feeds'
    split_string=re.split(r'<div class="f-item f-s-i" id=".*?" data-feedsflag=.*?" data-iswupfeed=".*?" data-key=".*?" data-specialtype=.*?" data-extend-info=".*?">',html)
    for i in range (0,len(fkey)):
        try:
            btn_string = re.search(r'<a class="item qz_like_btn_v3" data-islike="0" data-likecnt=".*?" data-showcount=".*?" data-unikey="(.*?)" data-curkey="(.*?)" data-clicklog="like" href="javascript:;">', split_string[i+1])
            if btn_string is None:
                continue
            abstime = re.search(r'data-abstime="(\d*?)"',split_string[i+1])
            if abstime is None:
                continue
            like(btn_string.group(1),btn_string.group(2),fkey[i],abstime.group(1))
            qqkongjian.update_msg(u'【点赞成功】'+btn_string.group(2))
            logging.info('【点赞成功】'+btn_string.group(2))
        except Exception, e:
            qqkongjian.update_msg(u'【发生异常】'+str(e))
            logging.error(str(e))

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()

    def run(self):
        # -----------------
        # 主程序
        # -----------------
        if __name__ == "__main__":
            if os.path.exists('./v.png'):
                os.remove('./v.png')
            else:
                pass
            #time.sleep(5)
            vpath = './v.png'
            qq = 0
            if len(sys.argv) > 1:
                vpath = sys.argv[1]
            if len(sys.argv) > 2:
                qq = sys.argv[2]

            try:
                qqLogin = Login(vpath, qq)
            except Exception, e:
                qqkongjian.update_msg(u'【发生异常】'+str(e))
                logging.critical(u'【发生异常】'+str(e))
                os._exit(1)
            errtime=0
            while True:
                try:
                    if errtime > 5:
                        break
                    MsgHandler()
                    time.sleep(checkFrequency)
                    errtime = 0
                except Exception, e:
                    qqkongjian.update_msg(u'【发生异常】'+str(e))
                    logging.error(u'【发生异常】'+str(e))
                    errtime = errtime + 1

class QQKONGJIAN(QDialog):
    def __init__(self,parent=None):
        super(QQKONGJIAN,self).__init__(parent)
        self.window_move() #窗口显示位置
        self.setWindowTitle(self.tr(u'QQ空间自动点赞机'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        mainLayout=QGridLayout(self)

        hb1 = QVBoxLayout()
        self.lb1 = QLabel()
        self.lb1.setText(u'说明：本程序需要使用手机QQ安全中心APP的扫描二维码进行登录。')
        #self.lb2 = QLabel()
        #self.lb2.setPixmap(QPixmap(""))
        hb1.addWidget(self.lb1)
        #hb1.addWidget(self.lb2)

        hb2 = QVBoxLayout()
        self.ListWidgetContent= QListWidget(self)
        hb2.addWidget(self.ListWidgetContent)

        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)

        self.workThread1.start()

    workThread1=WorkThread1()

    # 窗口显示位置
    def window_move(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move( screen.width()-size.width()+105 , screen.height()/2-(screen.height()/2-size.height())-98 )

    #退出确认
    def closeEvent(self, event):
        rely = QMessageBox.question(self,u'退出',u'确定要关闭吗?',QMessageBox.Yes,QMessageBox.No)
        if rely == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

    def update_msg(self,msg):
        self.ListWidgetContent.addItem(msg)#.decode('utf-8')
        self.ListWidgetContent.setCurrentRow(self.ListWidgetContent.count()-1)

    #def show_erweima(self):
    #    self.lb2.setPixmap(QPixmap("./v.png"))

app=QApplication(sys.argv)
qqkongjian=QQKONGJIAN()
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/qqkongjian.ico'), QIcon.Normal, QIcon.Off)
qqkongjian.setWindowIcon(icon)
qqkongjian.setFixedSize(520,250)
qqkongjian.show()
app.exec_()


