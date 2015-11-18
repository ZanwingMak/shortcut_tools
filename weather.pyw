#coding:utf-8
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os,sys,urllib2,re,requests,json
reload(sys)
sys.setdefaultencoding('utf-8')

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


def get_weather_data(city_name):
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+str(city_name).strip()  #只需城市名
    #url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100' #使用城市代码来查询
    weather_data = requests.get(url1).text #.content
    weather_dict = json.loads(weather_data)
    if weather_dict.get('desc') == 'OK':
        weather.label4.setText(weather.tr(str(city_name).strip()))
        data = weather_dict.get('data')
        forecast = data.get('forecast')
        weather.label6.setText(weather.tr(forecast[0].get('date')))
        weather.label8.setText(weather.tr(data.get('wendu')+u'℃ ['+forecast[0].get('low')[3:]+u'～'+forecast[0].get('high')[3:]+u']'))
        weather.label10.setText(weather.tr(forecast[0].get('type')))
        weather.label12.setText(weather.tr(forecast[0].get('fengxiang')))
        weather.label14.setText(weather.tr(forecast[0].get('fengli')))
        weather.label16.setText(weather.tr(data.get('ganmao')))

        weather.label21.setText(weather.tr(forecast[1].get('date')))
        weather.label23.setText(weather.tr(forecast[2].get('date')))
        weather.label25.setText(weather.tr(forecast[3].get('date')))
        weather.label27.setText(weather.tr(forecast[4].get('date')))

        weather.label29.setText(weather.tr(forecast[1].get('low')[3:]+u'～'+forecast[1].get('high')[3:]))
        weather.label31.setText(weather.tr(forecast[2].get('low')[3:]+u'～'+forecast[2].get('high')[3:]))
        weather.label33.setText(weather.tr(forecast[3].get('low')[3:]+u'～'+forecast[3].get('high')[3:]))
        weather.label35.setText(weather.tr(forecast[4].get('low')[3:]+u'～'+forecast[4].get('high')[3:]))


        weather.label37.setText(weather.tr(forecast[1].get('type')))
        weather.label39.setText(weather.tr(forecast[2].get('type')))
        weather.label41.setText(weather.tr(forecast[3].get('type')))
        weather.label43.setText(weather.tr(forecast[4].get('type')))


        weather.label45.setText(weather.tr(forecast[1].get('fengxiang')))
        weather.label47.setText(weather.tr(forecast[2].get('fengxiang')))
        weather.label49.setText(weather.tr(forecast[3].get('fengxiang')))
        weather.label51.setText(weather.tr(forecast[4].get('fengxiang')))


        weather.label53.setText(weather.tr(forecast[1].get('fengli')))
        weather.label55.setText(weather.tr(forecast[2].get('fengli')))
        weather.label57.setText(weather.tr(forecast[3].get('fengli')))
        weather.label59.setText(weather.tr(forecast[4].get('fengli')))

        weather.label001.setText(weather.tr(u"         今天的天气(查询成功...)"))

    else:
        #QMessageBox.information(weather.tr(u"查询失败"),weather.tr(u'查询失败,注意:错别字和非中国大陆地区会无法查询...'))
        weather.label001.setText(weather.tr(u"         今天的天气(查询失败...)"))

def get_ip_physical_location(ip):
    for i in range(3): #重试三次
        try:
            url1 = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
            url2 = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=' + ip
            ip_data1 = requests.get(url1).text
            ip_dict1 = json.loads(ip_data1)
            if ip_dict1.get('code'):
                #print(u'查询失败,正在切换新的查询链接...')
                ip_data2 = requests.get(url2).text
                ip_dict2 = json.loads(ip_data2)
                if ip_dict2.get('ret') == 1:
                    #print u'查询成功...'
                    country = ip_dict2.get('country')
                    province = ip_dict2.get('province')
                    city = ip_dict2.get('city')
            else:
                data1 = ip_dict1.get('data')
                country = data1.get('country')
                province = data1.get('region')[0:-1] #因为会有个"省"字，另一个链接的城市又没有"省"字...
                city = data1.get('city')[0:-1] #因为会有个"市"字，另一个链接的城市又没有"市"字...
            weather.label4.setText(weather.tr(country + province + u"省" + city + u"市"))
            return city
        except Exception: #,e
            if i==2:
                weather.label4.setText(weather.tr('查询物理位置失败'))
            #print u'原因：\n%s' % e

def get_my_ip():
    #print u'正在查询您的ip地址...'
    url1 = 'http://ip.chinaz.com/'
    url2 = 'http://ip.dnsexit.com/'
    url3 = 'http://www.whereismyip.com/'
    my_ip = ''
    try:
        opener = urllib2.urlopen(url1,timeout=8)
        if url1 == opener.geturl():
            html = opener.read()
            my_ip = re.search('\d+\.\d+\.\d+\.\d+',html).group(0)
    except:
        try:
            opener = urllib2.urlopen(url2,timeout=10)
            if url2 == opener.geturl():
                html = opener.read()
                my_ip = re.search('\d+\.\d+\.\d+\.\d+',html).group(0)
        except:
            try:
                opener = urllib2.urlopen(url2,timeout=15)
                if url3 == opener.geturl():
                    html = opener.read()
                    my_ip = re.search('\d+\.\d+\.\d+\.\d+',html).group(0)
            except:
                weather.label2.setText(weather.tr(u'查询外网ip失败'))
                my_ip = 'None'
    if my_ip != 'None':
        weather.label2.setText(weather.tr(my_ip))
        return my_ip

class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()
    def run(self):
        get_weather_data(get_ip_physical_location(get_my_ip()))
        self.trigger.emit()

class WorkThread2(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread2,self).__init__()
    def run(self):
        weather.label001.setText(weather.tr(u"         今天的天气(正在查询...)"))
        weather.label2.setText(weather.tr(get_my_ip()))
        get_weather_data(weather.edit.text())
        self.trigger.emit()

class Weather(QDialog):
    def __init__(self,parent=None):
        super(Weather,self).__init__(parent)
        self.setWindowTitle(self.tr(u"天气查询"))

        mainLayout=QGridLayout(self)

        hb00 = QHBoxLayout()
        self.label000 = QLabel()
        self.label000.setText(self.tr(u"请输入您要查询天气的中国大陆城市："))
        self.edit = QLineEdit(self)
        self.btn_ok = QPushButton(self)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_ok.setText(self.tr("查询"))
        hb00.addWidget(self.label000)
        hb00.addWidget(self.edit)
        hb00.addWidget(self.btn_ok)

        hb0 = QVBoxLayout()
        self.label100 = QLabel(self)
        self.label100.setText(self.tr(u"============================"))
        self.label001 = QLabel(self)
        self.label001.setText(self.tr(u"         今天的天气(自动查询当地天气状况[重试3次]...)         "))
        self.label002 = QLabel(self)
        self.label002.setText(self.tr(u"============================"))
        hb0.addWidget(self.label100)
        hb0.addWidget(self.label001)
        hb0.addWidget(self.label002)

        hb1 = QHBoxLayout()
        self.label1 = QLabel(self)
        self.label1.setText(self.tr(u"您的外(公)网ip是："))
        self.label2 = QLabel(self)
        self.label2.setText(self.tr(u"请稍候"))
        self.label3 = QLabel(self)
        self.label3.setText(self.tr(u"  城市："))
        self.label4 = QLabel(self)
        self.label4.setText(self.tr(u"请稍候"))
        self.label5 = QLabel(self)
        self.label5.setText(self.tr(u"  日期："))
        self.label6 = QLabel(self)
        self.label6.setText(self.tr(u"请稍候"))
        hb1.addWidget(self.label1)
        hb1.addWidget(self.label2)
        hb1.addWidget(self.label3)
        hb1.addWidget(self.label4)
        hb1.addWidget(self.label5)
        hb1.addWidget(self.label6)

        hb2 = QHBoxLayout()
        self.label7 = QLabel(self)
        self.label7.setText(self.tr(u"温度："))
        self.label8 = QLabel(self)
        self.label8.setText(self.tr(u"请稍候"))
        self.label9 = QLabel(self)
        self.label9.setText(self.tr(u"   天气："))
        self.label10 = QLabel(self)
        self.label10.setText(self.tr(u"请稍候"))
        self.label11 = QLabel(self)
        self.label11.setText(self.tr(u"风向："))
        self.label12 = QLabel(self)
        self.label12.setText(self.tr(u"请稍候"))
        self.label13 = QLabel(self)
        self.label13.setText(self.tr(u"  风级："))
        self.label14 = QLabel(self)
        self.label14.setText(self.tr(u"请稍候"))
        hb2.addWidget(self.label7)
        hb2.addWidget(self.label8)
        hb2.addWidget(self.label9)
        hb2.addWidget(self.label10)
        hb2.addWidget(self.label11)
        hb2.addWidget(self.label12)
        hb2.addWidget(self.label13)
        hb2.addWidget(self.label14)

        hb3 = QHBoxLayout()
        self.label15 = QLabel(self)
        self.label15.setText(self.tr(u"提醒："))
        self.label16 = QLabel(self)
        self.label16.setText(self.tr(u"请稍候"))
        hb3.addWidget(self.label15)
        hb3.addWidget(self.label16)

        hb4 = QVBoxLayout()
        self.label17 = QLabel(self)
        self.label17.setText(self.tr(u"============================"))
        self.label18 = QLabel(self)
        self.label18.setText(self.tr(u"       未来四天的天气       "))
        self.label19 = QLabel(self)
        self.label19.setText(self.tr(u"============================"))
        hb4.addWidget(self.label17)
        hb4.addWidget(self.label18)
        hb4.addWidget(self.label19)

        hb5 = QHBoxLayout()
        self.label20 = QLabel(self)
        self.label20.setText(self.tr(u"日期："))
        self.label21 = QLabel(self)
        self.label21.setText(self.tr(u"请稍候"))
        self.label22 = QLabel(self)
        self.label22.setText(self.tr(u"  日期："))
        self.label23 = QLabel(self)
        self.label23.setText(self.tr(u"请稍候"))
        self.label24 = QLabel(self)
        self.label24.setText(self.tr(u"  日期："))
        self.label25 = QLabel(self)
        self.label25.setText(self.tr(u"请稍候"))
        self.label26 = QLabel(self)
        self.label26.setText(self.tr(u"  日期："))
        self.label27 = QLabel(self)
        self.label27.setText(self.tr(u"请稍候"))

        hb5.addWidget(self.label20)
        hb5.addWidget(self.label21)
        hb5.addWidget(self.label22)
        hb5.addWidget(self.label23)
        hb5.addWidget(self.label24)
        hb5.addWidget(self.label25)
        hb5.addWidget(self.label26)
        hb5.addWidget(self.label27)

        hb6 = QHBoxLayout()
        self.label28 = QLabel(self)
        self.label28.setText(self.tr(u"温度："))
        self.label29 = QLabel(self)
        self.label29.setText(self.tr(u"请稍候"))
        self.label30 = QLabel(self)
        self.label30.setText(self.tr(u"  温度："))
        self.label31 = QLabel(self)
        self.label31.setText(self.tr(u"请稍候"))
        self.label32 = QLabel(self)
        self.label32.setText(self.tr(u"  温度："))
        self.label33 = QLabel(self)
        self.label33.setText(self.tr(u"请稍候"))
        self.label34 = QLabel(self)
        self.label34.setText(self.tr(u"  温度："))
        self.label35 = QLabel(self)
        self.label35.setText(self.tr(u"请稍候"))
        hb6.addWidget(self.label28)
        hb6.addWidget(self.label29)
        hb6.addWidget(self.label30)
        hb6.addWidget(self.label31)
        hb6.addWidget(self.label32)
        hb6.addWidget(self.label33)
        hb6.addWidget(self.label34)
        hb6.addWidget(self.label35)

        hb7 = QHBoxLayout()
        self.label36 = QLabel(self)
        self.label36.setText(self.tr(u"天气："))
        self.label37 = QLabel(self)
        self.label37.setText(self.tr(u"请稍候"))
        self.label38 = QLabel(self)
        self.label38.setText(self.tr(u"  天气："))
        self.label39 = QLabel(self)
        self.label39.setText(self.tr(u"请稍候"))
        self.label40 = QLabel(self)
        self.label40.setText(self.tr(u"  天气："))
        self.label41 = QLabel(self)
        self.label41.setText(self.tr(u"请稍候"))
        self.label42 = QLabel(self)
        self.label42.setText(self.tr(u"  天气："))
        self.label43 = QLabel(self)
        self.label43.setText(self.tr(u"请稍候"))
        hb7.addWidget(self.label36)
        hb7.addWidget(self.label37)
        hb7.addWidget(self.label38)
        hb7.addWidget(self.label39)
        hb7.addWidget(self.label40)
        hb7.addWidget(self.label41)
        hb7.addWidget(self.label42)
        hb7.addWidget(self.label43)

        hb8 = QHBoxLayout()
        self.label44 = QLabel(self)
        self.label44.setText(self.tr(u"风向："))
        self.label45 = QLabel(self)
        self.label45.setText(self.tr(u"请稍候"))
        self.label46 = QLabel(self)
        self.label46.setText(self.tr(u"  风向："))
        self.label47 = QLabel(self)
        self.label47.setText(self.tr(u"请稍候"))
        self.label48 = QLabel(self)
        self.label48.setText(self.tr(u"  风向："))
        self.label49 = QLabel(self)
        self.label49.setText(self.tr(u"请稍候"))
        self.label50 = QLabel(self)
        self.label50.setText(self.tr(u"  风向："))
        self.label51 = QLabel(self)
        self.label51.setText(self.tr(u"请稍候"))
        hb8.addWidget(self.label44)
        hb8.addWidget(self.label45)
        hb8.addWidget(self.label46)
        hb8.addWidget(self.label47)
        hb8.addWidget(self.label48)
        hb8.addWidget(self.label49)
        hb8.addWidget(self.label50)
        hb8.addWidget(self.label51)

        hb9 = QHBoxLayout()
        self.label52 = QLabel(self)
        self.label52.setText(self.tr(u"风级："))
        self.label53 = QLabel(self)
        self.label53.setText(self.tr(u"请稍候"))
        self.label54 = QLabel(self)
        self.label54.setText(self.tr(u"  风级："))
        self.label55 = QLabel(self)
        self.label55.setText(self.tr(u"请稍候"))
        self.label56 = QLabel(self)
        self.label56.setText(self.tr(u"  风级："))
        self.label57 = QLabel(self)
        self.label57.setText(self.tr(u"请稍候"))
        self.label58 = QLabel(self)
        self.label58.setText(self.tr(u"  风级："))
        self.label59 = QLabel(self)
        self.label59.setText(self.tr(u"请稍候"))
        hb9.addWidget(self.label52)
        hb9.addWidget(self.label53)
        hb9.addWidget(self.label54)
        hb9.addWidget(self.label55)
        hb9.addWidget(self.label56)
        hb9.addWidget(self.label57)
        hb9.addWidget(self.label58)
        hb9.addWidget(self.label59)

        mainLayout.addLayout(hb00,0,0)
        mainLayout.addLayout(hb0,1,0)
        mainLayout.addLayout(hb1,2,0)
        mainLayout.addLayout(hb2,3,0)
        mainLayout.addLayout(hb3,4,0)
        mainLayout.addLayout(hb4,5,0)
        mainLayout.addLayout(hb5,6,0)
        mainLayout.addLayout(hb6,7,0)
        mainLayout.addLayout(hb7,8,0)
        mainLayout.addLayout(hb8,9,0)
        mainLayout.addLayout(hb9,10,0)

        self.workThread1.start()

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        self.workThread2.start()

    workThread1=WorkThread1()
    workThread2=WorkThread2()


app=QApplication(sys.argv)
weather=Weather()
#weather.setFixedSize(400,200)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/weather.ico'), QIcon.Normal, QIcon.Off)
weather.setWindowIcon(icon)
weather.show()
app.exec_()
