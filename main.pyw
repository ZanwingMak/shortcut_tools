# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
#主界面
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
import os,sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

#服务器相关
class TcpClientSocket(QTcpSocket):
    def __init__(self,parent=None):
        super(TcpClientSocket,self).__init__(parent)
        self.connect(self,SIGNAL("readyRead()"),self.dataReceive)
        self.connect(self,SIGNAL("disconnected()"),self.slotDisconnected)
        self.length2 = 0
        self.msglist2 = QByteArray()

    def dataReceive(self):
        while self.bytesAvailable() > 0:
            length2 = self.bytesAvailable()
            msg = self.read(length2)
            self.emit(SIGNAL("updateClients(QString,int)"),msg,length2)

    def slotDisconnected(self):
        pass

class Server(QTcpServer):
    def __init__(self,parent=None,port2=12450):
        super(Server,self).__init__(parent)
        self.listen(QHostAddress.Any,port2)
        self.tcpClientSocketList = []

    def incomingConnection(self,socketDescriptor):
        tcpClientSocket = TcpClientSocket(self)
        self.connect(tcpClientSocket,SIGNAL("updateClients(QString,int)"),self.updateClients)
        self.connect(tcpClientSocket,SIGNAL("disconnetcted(int)"),self.slotDisconnected)
        tcpClientSocket.setSocketDescriptor(socketDescriptor)
        self.tcpClientSocketList.append(tcpClientSocket)

    def updateClients(self,msg,length2):
        self.emit(SIGNAL("updateServer(QString,int)"),msg,length2)
        for i in xrange(len(self.tcpClientSocketList)):
            item = self.tcpClientSocketList[i]
            length_msg = item.writeData(msg.toUtf8())
            if length_msg != msg.toUtf8().length():
                continue

    def slotDisconnected(self,descriptor):
        for i in xrange(len(self.tcpClientSocketList)):
            item = self.tcpClientSocketList[i]
            if item.socketDescriptor() == descriptor:
                self.tcpClientSocketList.remove[i]
                return
        return
####

####系统工具，线程
class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()
    def run(self):
        os.startfile('calc')
        self.trigger.emit()         #完毕后发出信号
class WorkThread2(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread2,self).__init__()
    def run(self):
        os.startfile('cleanmgr')
        self.trigger.emit()
class WorkThread3(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread3,self).__init__()
    def run(self):
        os.startfile('cmd')
        self.trigger.emit()
class WorkThread4(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread4,self).__init__()
    def run(self):
        os.startfile('regedit.exe')
        self.trigger.emit()
class WorkThread5(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread5,self).__init__()
    def run(self):
        os.startfile('mstsc')
        self.trigger.emit()
class WorkThread6(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread6,self).__init__()
    def run(self):
        os.startfile('notepad')
        self.trigger.emit()
class WorkThread7(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread7,self).__init__()
    def run(self):
        os.startfile('compmgmt.msc')
        self.trigger.emit()
class WorkThread8(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread8,self).__init__()
    def run(self):
        os.startfile('services.msc')
        self.trigger.emit()
class WorkThread9(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread9,self).__init__()
    def run(self):
        os.startfile('gpedit.msc')
        self.trigger.emit()
class WorkThread16(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread16,self).__init__()
    def run(self):
        os.startfile('control')
        self.trigger.emit()
class WorkThread17(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread17,self).__init__()
    def run(self):
        os.startfile('Taskmgr')
        self.trigger.emit()
class WorkThread18(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread18,self).__init__()
    def run(self):
        os.startfile('Magnify')
        self.trigger.emit()
class WorkThread19(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread19,self).__init__()
    def run(self):
        os.startfile('resmon')
        self.trigger.emit()
class WorkThread20(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread20,self).__init__()
    def run(self):
        os.startfile('UserAccountControlSettings')
        self.trigger.emit()
class WorkThread21(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread21,self).__init__()
    def run(self):
        os.startfile('dxdiag')
        self.trigger.emit()
class WorkThread22(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread22,self).__init__()
    def run(self):
        os.startfile('eventvwr')
        self.trigger.emit()
class WorkThread23(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread23,self).__init__()
    def run(self):
        os.startfile('odbcad32')
        self.trigger.emit()
class WorkThread24(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread24,self).__init__()
    def run(self):
        os.startfile('winver')
        self.trigger.emit()

###快递查询
class WorkThread10(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread10,self).__init__()
    def run(self):
        os.startfile('kuaidi.pyw')
        self.trigger.emit()

###手机归属地查询
class WorkThread11(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread11,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('shoujiguishudi.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###QQ空间点赞机
class WorkThread12(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread12,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('qqkongjian.pyw') 
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###有道翻译
class WorkThread13(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread13,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('youdao.pyw') 
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###远程指令
class WorkThread14(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread14,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('yuancheng.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###系统信息
class WorkThread15(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread15,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('sysinfo.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###截图工具
class WorkThread25(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread25,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('jietu.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###天气查询
class WorkThread26(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread26,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('weather.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###智能应答机器人
class WorkThread27(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread27,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('robot.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###生成二维码
class WorkThread37(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread37,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('erweima.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###网址安全检查
class WorkThread38(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread38,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('urlcheck.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()

###后台监听
class WorkThread39(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread39,self).__init__()
    def run(self):
        ##打包成exe的时候记得把pyw改成exe
        os.startfile('monitor.pyw')
        ##打包成exe的时候记得把pyw改成exe
        self.trigger.emit()


###推荐工具
class WorkThread28(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread28,self).__init__()
    def run(self):
        os.startfile('.\other_tools\wifi.exe')
        self.trigger.emit()

class WorkThread29(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread29,self).__init__()
    def run(self):
        os.startfile('.\other_tools\process.exe')
        self.trigger.emit()

class WorkThread30(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread30,self).__init__()
    def run(self):
        os.startfile('.\other_tools\qyzngj\qyzngj.exe')
        self.trigger.emit()

class WorkThread31(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread31,self).__init__()
    def run(self):
        os.startfile('.\other_tools\md5.exe')
        self.trigger.emit()

class WorkThread32(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread32,self).__init__()
    def run(self):
        os.startfile('.\other_tools\DiskGenius.exe')
        self.trigger.emit()

class WorkThread33(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread33,self).__init__()
    def run(self):
        os.startfile('.\other_tools\color.exe')
        self.trigger.emit()

class WorkThread34(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread34,self).__init__()
    def run(self):
        os.startfile('.\other_tools\\net_tv.exe')
        self.trigger.emit()

class WorkThread35(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread35,self).__init__()
    def run(self):
        os.startfile('.\other_tools\RenameMany.exe')
        self.trigger.emit()

class WorkThread36(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread36,self).__init__()
    def run(self):
        os.startfile('.\other_tools\cpuz_x32.exe')
        self.trigger.emit()
#主界面
class MyTools(QTabWidget):
    def __init__(self,parent=None):
        super(MyTools,self).__init__(parent)
        self.window_move() #窗口显示位置
        ########设置窗口风格
        #self.setWindowFlags(Qt.Tool)  #提示窗口，窗口无边框化，无任务栏窗口
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  #窗口始终处于顶层位置
        # PyQT禁止窗口最大化按钮：
        #self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        #透明度
        self.setWindowOpacity(0.95)

        toolButton_kuaidi=QToolButton()
        toolButton_kuaidi.setText(self.tr(u"快递查询"))
        toolButton_kuaidi.setIcon(QIcon(u"./icon/myTools_icon/kuaidi.png"))
        toolButton_kuaidi.setIconSize(QSize(65,65))
        toolButton_kuaidi.setAutoRaise(True)
        #toolButton_kuaidi.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) #文本在按钮右边
        toolButton_kuaidi.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) #文本在按钮下方
        toolButton_kuaidi.clicked.connect(self.toolButton_kuaidi_Clicked)

        toolButton_shoujiguishudi=QToolButton()
        toolButton_shoujiguishudi.setText(self.tr(u"手机归属"))
        toolButton_shoujiguishudi.setIcon(QIcon(u"./icon/myTools_icon/shoujiguishu.png"))
        toolButton_shoujiguishudi.setIconSize(QSize(65,65))
        toolButton_shoujiguishudi.setAutoRaise(True)
        toolButton_shoujiguishudi.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_shoujiguishudi.clicked.connect(self.toolButton_shoujiguishudi_Clicked)

        toolButton_qqkongjian=QToolButton()
        toolButton_qqkongjian.setText(self.tr(u"空间点赞"))
        toolButton_qqkongjian.setIcon(QIcon(u"./icon/myTools_icon/qqkongjian.png"))
        toolButton_qqkongjian.setIconSize(QSize(65,65))
        toolButton_qqkongjian.setAutoRaise(True)
        toolButton_qqkongjian.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_qqkongjian.clicked.connect(self.toolButton_qqkongjian_Clicked)

        toolButton_youdao=QToolButton()
        toolButton_youdao.setText(self.tr(u"有道翻译"))
        toolButton_youdao.setIcon(QIcon(u"./icon/myTools_icon/youdao.png"))
        toolButton_youdao.setIconSize(QSize(65,65))
        toolButton_youdao.setAutoRaise(True)
        toolButton_youdao.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_youdao.clicked.connect(self.toolButton_youdao_Clicked)

        toolButton_yuancheng=QToolButton()
        toolButton_yuancheng.setText(self.tr(u"远程指令"))
        toolButton_yuancheng.setIcon(QIcon(u"./icon/myTools_icon/yuancheng.png"))
        toolButton_yuancheng.setIconSize(QSize(65,65))
        toolButton_yuancheng.setAutoRaise(True)
        toolButton_yuancheng.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_yuancheng.clicked.connect(self.toolButton_yuancheng_Clicked)

        toolButton_systeminfo=QToolButton()
        toolButton_systeminfo.setText(self.tr(u"系统信息"))
        toolButton_systeminfo.setIcon(QIcon(u"./icon/myTools_icon/system_info.png"))
        toolButton_systeminfo.setIconSize(QSize(65,65))
        toolButton_systeminfo.setAutoRaise(True)
        toolButton_systeminfo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_systeminfo.clicked.connect(self.toolButton_systeminfo_Clicked)

        toolButton_jietu=QToolButton()
        #toolButton_jietu.setCheckable(True) ###设置按钮可以按下和抬起
        toolButton_jietu.setText(self.tr(u"截图"))
        #toolButton_jietu.setStyleSheet('Microsoft Yahei')
        toolButton_jietu.setIcon(QIcon(u"./icon/myTools_icon/jietu.png"))
        toolButton_jietu.setIconSize(QSize(65,65))
        toolButton_jietu.setAutoRaise(True)
        toolButton_jietu.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_jietu.clicked.connect(self.toolButton_jietu_Clicked)

        toolButton_weather=QToolButton()
        toolButton_weather.setText(self.tr(u"天气"))
        toolButton_weather.setIcon(QIcon(u"./icon/myTools_icon/weather.png"))
        toolButton_weather.setIconSize(QSize(65,65))
        toolButton_weather.setAutoRaise(True)
        toolButton_weather.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_weather.clicked.connect(self.toolButton_weather_Clicked)

        toolButton_robot=QToolButton()
        toolButton_robot.setText(self.tr(u"智能姬"))
        toolButton_robot.setIcon(QIcon(u"./icon/myTools_icon/robot.png"))
        toolButton_robot.setIconSize(QSize(65,65))
        toolButton_robot.setAutoRaise(True)
        toolButton_robot.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_robot.clicked.connect(self.toolButton_robot_Clicked)

        toolButton_erweima=QToolButton()
        toolButton_erweima.setText(self.tr(u"二维码"))
        toolButton_erweima.setIcon(QIcon(u"./icon/myTools_icon/erweima.png"))
        toolButton_erweima.setIconSize(QSize(65,65))
        toolButton_erweima.setAutoRaise(True)
        toolButton_erweima.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_erweima.clicked.connect(self.toolButton_erweima_Clicked)

        toolButton_urlcheck=QToolButton()
        toolButton_urlcheck.setText(self.tr(u"网址检测"))
        toolButton_urlcheck.setIcon(QIcon(u"./icon/myTools_icon/url_check.png"))
        toolButton_urlcheck.setIconSize(QSize(65,65))
        toolButton_urlcheck.setAutoRaise(True)
        toolButton_urlcheck.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_urlcheck.clicked.connect(self.toolButton_urlcheck_Clicked)

        toolButton_monitor=QToolButton()
        toolButton_monitor.setText(self.tr(u"后台监听"))
        toolButton_monitor.setIcon(QIcon(u"./icon/myTools_icon/monitor.png"))
        toolButton_monitor.setIconSize(QSize(65,65))
        toolButton_monitor.setAutoRaise(True)
        toolButton_monitor.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_monitor.clicked.connect(self.toolButton_monitor_Clicked)

####系统工具按钮
        toolButton_calc=QToolButton()
        toolButton_calc.setText(self.tr(u"计算器"))
        toolButton_calc.setIcon(QIcon(u"./icon/systemTools_icon/calc.png"))
        toolButton_calc.setIconSize(QSize(65,65))
        toolButton_calc.setAutoRaise(True)
        toolButton_calc.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_calc.clicked.connect(self.toolButton_calc_Clicked)

        toolButton_cleanmgr=QToolButton()
        toolButton_cleanmgr.setText(self.tr(u"垃圾整理"))
        toolButton_cleanmgr.setIcon(QIcon(u"./icon/systemTools_icon/cleanmgr.png"))
        toolButton_cleanmgr.setIconSize(QSize(65,65))
        toolButton_cleanmgr.setAutoRaise(True)
        toolButton_cleanmgr.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_cleanmgr.clicked.connect(self.toolButton_cleanmgr_Clicked)

        toolButton_cmd=QToolButton()
        toolButton_cmd.setText(self.tr(u"命令行"))
        toolButton_cmd.setIcon(QIcon(u"./icon/systemTools_icon/cmd.png"))
        toolButton_cmd.setIconSize(QSize(65,65))
        toolButton_cmd.setAutoRaise(True)
        toolButton_cmd.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_cmd.clicked.connect(self.toolButton_cmd_Clicked)

        toolButton_regedit=QToolButton()
        toolButton_regedit.setText(self.tr(u"注册表"))
        toolButton_regedit.setIcon(QIcon(u"./icon/systemTools_icon/regedit.png"))
        toolButton_regedit.setIconSize(QSize(65,65))
        toolButton_regedit.setAutoRaise(True)
        toolButton_regedit.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_regedit.clicked.connect(self.toolButton_regedit_Clicked)

        toolButton_mstsc=QToolButton()
        toolButton_mstsc.setText(self.tr(u"远程"))
        toolButton_mstsc.setIcon(QIcon(u"./icon/systemTools_icon/mstsc.png"))
        toolButton_mstsc.setIconSize(QSize(65,65))
        toolButton_mstsc.setAutoRaise(True)
        toolButton_mstsc.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_mstsc.clicked.connect(self.toolButton_mstsc_Clicked)

        toolButton_notepad=QToolButton()
        toolButton_notepad.setText(self.tr(u"记事本"))
        toolButton_notepad.setIcon(QIcon(u"./icon/systemTools_icon/notepad.png"))
        toolButton_notepad.setIconSize(QSize(65,65))
        toolButton_notepad.setAutoRaise(True)
        toolButton_notepad.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_notepad.clicked.connect(self.toolButton_notepad_Clicked)

        toolButton_compmgmt=QToolButton()
        toolButton_compmgmt.setText(self.tr(u"管理"))
        toolButton_compmgmt.setIcon(QIcon(u"./icon/systemTools_icon/compmgmt.png"))
        toolButton_compmgmt.setIconSize(QSize(65,65))
        toolButton_compmgmt.setAutoRaise(True)
        toolButton_compmgmt.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_compmgmt.clicked.connect(self.toolButton_compmgmt_Clicked)

        toolButton_services=QToolButton()
        toolButton_services.setText(self.tr(u"服务"))
        toolButton_services.setIcon(QIcon(u"./icon/systemTools_icon/services.png"))
        toolButton_services.setIconSize(QSize(65,65))
        toolButton_services.setAutoRaise(True)
        toolButton_services.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_services.clicked.connect(self.toolButton_services_Clicked)

        toolButton_control=QToolButton()
        toolButton_control.setText(self.tr(u"控制面板"))
        toolButton_control.setIcon(QIcon(u"./icon/systemTools_icon/control.png"))
        toolButton_control.setIconSize(QSize(65,65))
        toolButton_control.setAutoRaise(True)
        toolButton_control.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_control.clicked.connect(self.toolButton_control_Clicked)

        toolButton_gpedit=QToolButton()
        toolButton_gpedit.setText(self.tr(u"组策略"))
        toolButton_gpedit.setIcon(QIcon(u"./icon/systemTools_icon/gpedit.png"))
        toolButton_gpedit.setIconSize(QSize(65,65))
        toolButton_gpedit.setAutoRaise(True)
        toolButton_gpedit.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_gpedit.clicked.connect(self.toolButton_gpedit_Clicked)

        toolButton_taskmgr=QToolButton()
        toolButton_taskmgr.setText(self.tr(u"任务管理"))
        toolButton_taskmgr.setIcon(QIcon(u"./icon/systemTools_icon/taskmgr.png"))
        toolButton_taskmgr.setIconSize(QSize(65,65))
        toolButton_taskmgr.setAutoRaise(True)
        toolButton_taskmgr.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_taskmgr.clicked.connect(self.toolButton_taskmgr_Clicked)

        toolButton_magnify=QToolButton()
        toolButton_magnify.setText(self.tr(u"放大镜"))
        toolButton_magnify.setIcon(QIcon(u"./icon/systemTools_icon/magnify.png"))
        toolButton_magnify.setIconSize(QSize(65,65))
        toolButton_magnify.setAutoRaise(True)
        toolButton_magnify.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_magnify.clicked.connect(self.toolButton_magnify_Clicked)

        toolButton_resmon=QToolButton()
        toolButton_resmon.setText(self.tr(u"资源监视"))
        toolButton_resmon.setIcon(QIcon(u"./icon/systemTools_icon/resmon.png"))
        toolButton_resmon.setIconSize(QSize(65,65))
        toolButton_resmon.setAutoRaise(True)
        toolButton_resmon.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_resmon.clicked.connect(self.toolButton_resmon_Clicked)

        toolButton_UAC=QToolButton()
        toolButton_UAC.setText(self.tr(u"UAC"))
        toolButton_UAC.setIcon(QIcon(u"./icon/systemTools_icon/uac.png"))
        toolButton_UAC.setIconSize(QSize(65,65))
        toolButton_UAC.setAutoRaise(True)
        toolButton_UAC.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_UAC.clicked.connect(self.toolButton_UAC_Clicked)

        toolButton_dxdiag=QToolButton()
        toolButton_dxdiag.setText(self.tr(u"DirectX"))
        toolButton_dxdiag.setIcon(QIcon(u"./icon/systemTools_icon/dxdiag.png"))
        toolButton_dxdiag.setIconSize(QSize(65,65))
        toolButton_dxdiag.setAutoRaise(True)
        toolButton_dxdiag.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_dxdiag.clicked.connect(self.toolButton_dxdiag_Clicked)

        toolButton_eventvwr=QToolButton()
        toolButton_eventvwr.setText(self.tr(u"事件"))
        toolButton_eventvwr.setIcon(QIcon(u"./icon/systemTools_icon/eventvwr.png"))
        toolButton_eventvwr.setIconSize(QSize(65,65))
        toolButton_eventvwr.setAutoRaise(True)
        toolButton_eventvwr.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_eventvwr.clicked.connect(self.toolButton_eventvwr_Clicked)

        toolButton_odbcad32=QToolButton()
        toolButton_odbcad32.setText(self.tr(u"ODBC"))
        toolButton_odbcad32.setIcon(QIcon(u"./icon/systemTools_icon/odbcad32.png"))
        toolButton_odbcad32.setIconSize(QSize(65,65))
        toolButton_odbcad32.setAutoRaise(True)
        toolButton_odbcad32.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_odbcad32.clicked.connect(self.toolButton_odbcad32_Clicked)

        toolButton_winver=QToolButton()
        toolButton_winver.setText(self.tr(u"关于Win"))
        toolButton_winver.setIcon(QIcon(u"./icon/systemTools_icon/winver.png"))
        toolButton_winver.setIconSize(QSize(65,65))
        toolButton_winver.setAutoRaise(True)
        toolButton_winver.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_winver.clicked.connect(self.toolButton_winver_Clicked)

#推荐工具
        toolButton_wifi=QToolButton()
        toolButton_wifi.setText(self.tr(u"wifi共享"))
        toolButton_wifi.setIcon(QIcon(u"./icon/otherTools_icon/wifi.png"))
        toolButton_wifi.setIconSize(QSize(65,65))
        toolButton_wifi.setAutoRaise(True)
        toolButton_wifi.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_wifi.clicked.connect(self.toolButton_wifi_Clicked)

        toolButton_process=QToolButton()
        toolButton_process.setText(self.tr(u"进程黑客"))
        toolButton_process.setIcon(QIcon(u"./icon/otherTools_icon/process.png"))
        toolButton_process.setIconSize(QSize(65,65))
        toolButton_process.setAutoRaise(True)
        toolButton_process.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_process.clicked.connect(self.toolButton_process_Clicked)

        toolButton_qyzngj=QToolButton()
        toolButton_qyzngj.setText(self.tr(u"智能关机"))
        toolButton_qyzngj.setIcon(QIcon(u"./icon/otherTools_icon/qyzngj.png"))
        toolButton_qyzngj.setIconSize(QSize(65,65))
        toolButton_qyzngj.setAutoRaise(True)
        toolButton_qyzngj.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_qyzngj.clicked.connect(self.toolButton_qyzngj_Clicked)

        toolButton_md5=QToolButton()
        toolButton_md5.setText(self.tr(u"MD5检验"))
        toolButton_md5.setIcon(QIcon(u"./icon/otherTools_icon/md5.png"))
        toolButton_md5.setIconSize(QSize(65,65))
        toolButton_md5.setAutoRaise(True)
        toolButton_md5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_md5.clicked.connect(self.toolButton_md5_Clicked)

        toolButton_DiskGenius=QToolButton()
        toolButton_DiskGenius.setText(self.tr(u"磁盘工具"))
        toolButton_DiskGenius.setIcon(QIcon(u"./icon/otherTools_icon/DiskGenius.png"))
        toolButton_DiskGenius.setIconSize(QSize(65,65))
        toolButton_DiskGenius.setAutoRaise(True)
        toolButton_DiskGenius.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_DiskGenius.clicked.connect(self.toolButton_DiskGenius_Clicked)

        toolButton_color=QToolButton()
        toolButton_color.setText(self.tr(u"取色器"))
        toolButton_color.setIcon(QIcon(u"./icon/otherTools_icon/color.png"))
        toolButton_color.setIconSize(QSize(65,65))
        toolButton_color.setAutoRaise(True)
        toolButton_color.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_color.clicked.connect(self.toolButton_color_Clicked)

        toolButton_net_tv=QToolButton()
        toolButton_net_tv.setText(self.tr(u"网络电视"))
        toolButton_net_tv.setIcon(QIcon(u"./icon/otherTools_icon/net_tv.png"))
        toolButton_net_tv.setIconSize(QSize(65,65))
        toolButton_net_tv.setAutoRaise(True)
        toolButton_net_tv.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_net_tv.clicked.connect(self.toolButton_net_tv_Clicked)

        toolButton_RenameMany=QToolButton()
        toolButton_RenameMany.setText(self.tr(u"批量改名"))
        toolButton_RenameMany.setIcon(QIcon(u"./icon/otherTools_icon/RenameMany.png"))
        toolButton_RenameMany.setIconSize(QSize(65,65))
        toolButton_RenameMany.setAutoRaise(True)
        toolButton_RenameMany.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_RenameMany.clicked.connect(self.toolButton_RenameMany_Clicked)

        toolButton_cpuz=QToolButton()
        toolButton_cpuz.setText(self.tr(u"硬件信息"))
        toolButton_cpuz.setIcon(QIcon(u"./icon/otherTools_icon/cpuz.png"))
        toolButton_cpuz.setIconSize(QSize(65,65))
        toolButton_cpuz.setAutoRaise(True)
        toolButton_cpuz.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolButton_cpuz.clicked.connect(self.toolButton_cpuz_Clicked)


        groupbox1=QGroupBox()
        vlayout1=QGridLayout(groupbox1)
        vlayout1.setMargin(10)
        #vlayout1.setAlignment(Qt.AlignCenter)
        vlayout1.addWidget(toolButton_kuaidi,0,0)
        vlayout1.addWidget(toolButton_shoujiguishudi,0,1)
        vlayout1.addWidget(toolButton_qqkongjian,0,2)
        vlayout1.addWidget(toolButton_youdao,1,0)
        vlayout1.addWidget(toolButton_yuancheng,1,1)
        vlayout1.addWidget(toolButton_systeminfo,1,2)
        vlayout1.addWidget(toolButton_jietu,2,0)
        vlayout1.addWidget(toolButton_weather,2,1)
        vlayout1.addWidget(toolButton_robot,2,2)
        vlayout1.addWidget(toolButton_erweima,3,0)
        vlayout1.addWidget(toolButton_urlcheck,3,1)
        vlayout1.addWidget(toolButton_monitor,3,2)
        #vlayout1.addStretch() #自动往中心靠

        groupbox2=QGroupBox()
        vlayout2=QGridLayout(groupbox2)
        vlayout2.setMargin(10)
        #vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton_calc,0,0)
        vlayout2.addWidget(toolButton_cleanmgr,0,1)
        vlayout2.addWidget(toolButton_cmd,0,2)
        vlayout2.addWidget(toolButton_regedit,1,0)
        vlayout2.addWidget(toolButton_mstsc,1,1)
        vlayout2.addWidget(toolButton_notepad,1,2)
        vlayout2.addWidget(toolButton_compmgmt,2,0)
        vlayout2.addWidget(toolButton_services,2,1)
        vlayout2.addWidget(toolButton_control,2,2)
        vlayout2.addWidget(toolButton_gpedit,3,0)
        vlayout2.addWidget(toolButton_taskmgr,3,1)
        vlayout2.addWidget(toolButton_magnify,3,2)
        vlayout2.addWidget(toolButton_resmon,4,0)
        vlayout2.addWidget(toolButton_UAC,4,1)
        vlayout2.addWidget(toolButton_dxdiag,4,2)
        vlayout2.addWidget(toolButton_eventvwr,5,0)
        vlayout2.addWidget(toolButton_odbcad32,5,1)
        vlayout2.addWidget(toolButton_winver,5,2)
        #vlayout2.addStretch()

        groupbox3=QGroupBox()
        vlayout3=QGridLayout(groupbox3)
        vlayout3.setMargin(10)
        vlayout3.addWidget(toolButton_wifi,0,0)
        vlayout3.addWidget(toolButton_process,0,1)
        vlayout3.addWidget(toolButton_qyzngj,0,2)
        vlayout3.addWidget(toolButton_md5,1,0)
        vlayout3.addWidget(toolButton_DiskGenius,1,1)
        vlayout3.addWidget(toolButton_color,1,2)
        vlayout3.addWidget(toolButton_net_tv,2,0)
        vlayout3.addWidget(toolButton_RenameMany,2,1)
        vlayout3.addWidget(toolButton_cpuz,2,2)

        toolbox1 = QToolBox()
        toolbox1.addItem(groupbox1,self.tr(u"我的工具"))
        toolbox1.addItem(groupbox2,self.tr(u"系统工具"))
        toolbox1.addItem(groupbox3,self.tr(u"推荐工具"))

        self.addTab(toolbox1, u"工具箱")

###聊天室部分
        groupbox4=QGroupBox()
        vlayout4=QVBoxLayout(groupbox4)
        qlabel4 = QLabel(u'你好,欢迎使用聊天室功能!\n\n请在下方选择客户端或服务端!\n\n并请先设置好相应参数!\n\n[客户端]\n输入服务器端ip即可登录聊天室\n\n[服务器端]\n点击开启服务器即可创建聊天室房间'+u'\n'*15+u'↓'*7+u'点击选择'+u'↓'*7)
        qlabel4.setMargin(10)
        qlabel4.setAlignment(Qt.AlignCenter)
        vlayout4.addWidget(qlabel4)
        vlayout4.addStretch()

        groupbox5=QGroupBox()
        self.status = False
        self.serverIP = QHostAddress()
        self.port1 = 12450
        self.msglist1 = QByteArray()

        vlayout5=QVBoxLayout(groupbox5)
        self.ListWidgetContent1 = QListWidget(self)

        vlayout5.addWidget(self.ListWidgetContent1)

        hb = QHBoxLayout()
        self.LineEditMessage = QLineEdit(self)
        hb.addWidget(self.LineEditMessage)
        self.PushButtonSend = QPushButton(self)
        self.PushButtonSend.setText(self.tr("发送"))
        self.PushButtonSend.setEnabled(False)
        hb.addWidget(self.PushButtonSend)
        self.connect(self.PushButtonSend,SIGNAL("clicked()"),self.slotSend)

        hb1 = QHBoxLayout()
        LabelName = QLabel(self)
        LabelName.setText(self.tr("用户名:"))
        self.LineEditUser = QLineEdit(self)
        hb1.addWidget(LabelName)
        hb1.addWidget(self.LineEditUser)

        hb2 = QHBoxLayout()
        LabelServerIP = QLabel(self)
        LabelServerIP.setText(self.tr("服务器地址:"))
        self.LineEditIP = QLineEdit(self)
        hb2.addWidget(LabelServerIP)
        hb2.addWidget(self.LineEditIP)

        hb3 = QHBoxLayout()
        LabelPort1 = QLabel(self)
        LabelPort1.setText(self.tr("端口:"))

        self.LineEditPort1 = QLineEdit(self)
        self.LineEditPort1.setText(QString.number(self.port1))
        self.LineEditPort1.setDisabled(True)
        hb3.addWidget(LabelPort1)
        hb3.addWidget(self.LineEditPort1)


        vlayout5.addLayout(hb)
        vlayout5.addLayout(hb1)
        vlayout5.addLayout(hb2)
        vlayout5.addLayout(hb3)

        self.PushButtonLeave = QPushButton(self)
        self.PushButtonLeave.setText(self.tr("进入聊天室"))
        vlayout5.addWidget(self.PushButtonLeave)

        self.connect(self.PushButtonLeave,SIGNAL("clicked()"),self.slotEnter)

        vlayout5.addStretch()


        groupbox6=QGroupBox()
        vlayout6 = QVBoxLayout(groupbox6)
        self.ListWidgetContent2 = QListWidget(self)
        vlayout6.addWidget(self.ListWidgetContent2)

        hb4 = QHBoxLayout()
        LabelPort2 = QLabel(self)
        LabelPort2.setText(self.tr(u"端口:"))
        hb4.addWidget(LabelPort2)

        LineEditPort2 = QLineEdit(self)
        LineEditPort2.setDisabled(True)
        hb4.addWidget(LineEditPort2)

        vlayout6.addLayout(hb4)

        self.PushButtonCreate = QPushButton(self)
        self.PushButtonCreate.setText(self.tr("开启服务器"))

        vlayout6.addWidget(self.PushButtonCreate)

        self.connect(self.PushButtonCreate,SIGNAL("clicked()"),self.slotCreateServer)
        self.port2  = 12450
        LineEditPort2.setText(QString.number(self.port2))


        toolbox2 = QToolBox()
        toolbox2.addItem(groupbox4,self.tr(u"说明"))
        toolbox2.addItem(groupbox5,self.tr(u"客户端"))
        toolbox2.addItem(groupbox6,self.tr(u"服务端"))

        self.addTab(toolbox2, u"聊天室")

        groupbox7=QGroupBox()
        vlayout_about=QVBoxLayout(groupbox7)
        qlabel_about = QLabel(u'您好,欢迎使用多功能快捷工具箱!!!\n\n[我的工具]自行编写或改造的工具\n\n[系统工具]调用系统自带的工具\n\n[其它工具]调用外部非本人的工具\n\n[声明]\n本程序代码全部公开在个人博客和GitHub上\n\n个人博客：m9kun.com  QQ：728038259\n\nGithub：github.com/maizhenying09\n\n新浪微博：weibo.com/maizhenying\n\n邮箱：maizhenying09@gmail.com\n\n\n\n\nPS：再也不用Python写GUI了!!!!\n我都要哭了~~')
        qlabel_about.setMargin(10)
        qlabel_about.setAlignment(Qt.AlignCenter)
        vlayout_about.addWidget(qlabel_about)
        vlayout_about.addStretch()

        self.addTab(groupbox7, u"关于")

        #显示托盘图标
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("./icon/tuopan.png"))
        self.trayIcon.show()
        self.trayIcon.showMessage(u"泥壕!~",u"我在这里哦!你可以随时双击呼唤我哒!",icon=1)
        #双击托盘信号槽
        self.trayIcon.activated.connect(self.trayClick)
        #激活右键托盘菜单
        self.trayMenu()

####我的工具按钮Click事件
    def toolButton_kuaidi_Clicked(self):
        self.workThread10.start()
    def toolButton_shoujiguishudi_Clicked(self):
        self.workThread11.start()
    def toolButton_qqkongjian_Clicked(self):
        self.workThread12.start()
    def toolButton_youdao_Clicked(self):
        self.workThread13.start()
    def toolButton_yuancheng_Clicked(self):
        self.workThread14.start()
    def toolButton_systeminfo_Clicked(self):
        self.workThread15.start()
    def toolButton_jietu_Clicked(self):
        QMessageBox.information(self,self.tr(u"正在运行,快捷键如下："),self.tr(u'抓取全屏：Ctrl+Alt+F2\n抓取当前窗口：Ctrl+Alt+F3\n抓取所选区域：Ctrl+Alt+F5\n关闭截图工具：Ctrl+Alt+F12'))
        self.workThread25.start()
    def toolButton_weather_Clicked(self):
        self.workThread26.start()
    def toolButton_robot_Clicked(self):
        self.workThread27.start()
    def toolButton_erweima_Clicked(self):
        self.workThread37.start()
    def toolButton_urlcheck_Clicked(self):
        self.workThread38.start()
    def toolButton_monitor_Clicked(self):
        QMessageBox.information(self,self.tr(u"监听程序正在后台运行"),self.tr(u'【功能】\n1.监听键盘按键信息,日志文件保存在\n本目录下的Monitor文件夹里。\n2.窗口焦点切换自动全屏截图,截图保\n存在Monitor文件夹里的img目录下。\nPS：若要退出，关闭monitor.exe进程即可。'))
        self.workThread39.start()

####系统工具按钮Click事件
    def toolButton_calc_Clicked(self):
        self.workThread1.start()
    def toolButton_cleanmgr_Clicked(self):
        self.workThread2.start()
    def toolButton_cmd_Clicked(self):
        self.workThread3.start()
    def toolButton_regedit_Clicked(self):
        self.workThread4.start()
    def toolButton_mstsc_Clicked(self):
        self.workThread5.start()
    def toolButton_notepad_Clicked(self):
        self.workThread6.start()
    def toolButton_compmgmt_Clicked(self):
        self.workThread7.start()
    def toolButton_services_Clicked(self):
        self.workThread8.start()
    def toolButton_control_Clicked(self):
        self.workThread16.start()
    def toolButton_gpedit_Clicked(self):
        self.workThread9.start()
    def toolButton_taskmgr_Clicked(self):
        self.workThread17.start()
    def toolButton_magnify_Clicked(self):
        self.workThread18.start()
    def toolButton_resmon_Clicked(self):
        self.workThread19.start()
    def toolButton_UAC_Clicked(self):
        self.workThread20.start()
    def toolButton_dxdiag_Clicked(self):
        self.workThread21.start()
    def toolButton_eventvwr_Clicked(self):
        self.workThread22.start()
    def toolButton_odbcad32_Clicked(self):
        self.workThread23.start()
    def toolButton_winver_Clicked(self):
        self.workThread24.start()

#推荐工具
    def toolButton_wifi_Clicked(self):
        self.workThread28.start()
    def toolButton_process_Clicked(self):
        self.workThread29.start()
    def toolButton_qyzngj_Clicked(self):
        self.workThread30.start()
    def toolButton_md5_Clicked(self):
        self.workThread31.start()
    def toolButton_DiskGenius_Clicked(self):
        self.workThread32.start()
    def toolButton_color_Clicked(self):
        self.workThread33.start()
    def toolButton_net_tv_Clicked(self):
        self.workThread34.start()
    def toolButton_RenameMany_Clicked(self):
        self.workThread35.start()
    def toolButton_cpuz_Clicked(self):
        self.workThread36.start()


########
    #def changeEvent(self,event):
        '''改变事件'''
        # 判断是否为最小化事件
    #    if event.type() == QEvent.WindowStateChange and self.isMinimized():
            # 设置隐藏
    #        self.setVisible(False)
            # 设置窗口标记(取消在左下角显示)
            #self.setWindowFlags(Qt.Tool)

###退出确认'''
    def closeEvent(self, event):
        rely = QMessageBox.question(self,u'退出',u'确定要关闭吗?',QMessageBox.Yes,QMessageBox.No)
        if rely == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

    #def keyPressEvent(self, event): #按下ESC键时程序最小化
    #    if event.key() == Qt.Key_Escape:
    #        self.setVisible(False)
    #        self.showMinimized()

####
    def trayClick(self,reason):
       if reason==QSystemTrayIcon.DoubleClick:
           self.showNormal()
       else:
           pass

    #创建右击托盘菜单
    def trayMenu(self):
        #托盘提示信息
        self.trayIcon.setToolTip(u"多功能快捷工具箱")
        #菜单项1
        img_open = QIcon("./icon/open.png")
        self.restoreAction = QAction(img_open,u"打开主窗口", self)
        self.restoreAction.triggered.connect(self.showNormal)
        #菜单项2
        img_exit = QIcon("./icon/exit.png")
        self.quitAction = QAction(img_exit,u"退出", self)
        from PyQt4 import QtGui
        self.quitAction.triggered.connect(QtGui.qApp.quit)
        #菜单项3
        #self.aboutAction = QAction(u"关于", self)
        #self.aboutAction.triggered.connect(self.about)

        #创建托盘目录
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()#添加分隔线
        #self.trayIconMenu.addAction(self.aboutAction)
        #self.trayIconMenu.addSeparator()#添加分隔线
        self.trayIconMenu.addAction(self.quitAction)
        #设置目录为创建的目录
        self.trayIcon.setContextMenu(self.trayIconMenu)

##### 窗口显示位置
    def window_move(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.move( ( screen.width()-size.width() )/2 , ( screen.height()-size.height() )/2 )  #居中???
        self.move( screen.width()-(size.width()/2) , ( screen.height()-size.height() )/2 ) #靠右边

##### 服务端相关
    def slotCreateServer(self):
        server = Server(self,self.port2)
        self.connect(server,SIGNAL("updateServer(QString,int)"),self.updateServer)
        self.PushButtonCreate.setEnabled(False)

    def updateServer(self,msg,length2):
        self.ListWidgetContent2.addItem(msg.fromUtf8(msg))
        self.ListWidgetContent2.setCurrentRow(self.ListWidgetContent2.count()-1)


##### 客户端相关

    def slotSend(self):
        msg = self.userName + ":" + self.LineEditMessage.text()
        length1 = self.tcpSocket.writeData(msg.toUtf8())
        self.LineEditMessage.clear()
        if length1 != msg.toUtf8().length():
            return

    def slotEnter(self):
        if not self.status:
            ip = self.LineEditIP.text()
            if not self.serverIP.setAddress(ip):
                QMessageBox.information(self,self.tr(u"出错啦!"),self.tr(u"服务器ip地址错误!"))
                return
            if self.LineEditUser.text() == "":
                QMessageBox.information(self,self.tr(u"出错啦!"),self.tr(u"用户名错误!"))
                return
            self.userName = self.LineEditUser.text()
            self.tcpSocket = QTcpSocket(self)
            try:
                self.connect(self.tcpSocket,SIGNAL("connected()"),self.slotConnected)
                self.connect(self.tcpSocket,SIGNAL("disconnected()"),self.slotDisconnected)
                self.connect(self.tcpSocket,SIGNAL("readyRead()"),self.dataReceived)
                self.tcpSocket.connectToHost(self.serverIP.toString(),12450)
                #self.tcpSocket.connectToHost(self.serverIP.toString(),int(self.LineEditPort1.text()))
                self.status = True
            except:
                self.status = False
                #return
        else:
            msg = self.userName + ":" + self.tr("离开聊天室")
            length1 = self.tcpSocket.writeData(msg.toUtf8())
            if length1 != msg.toUtf8().length():
                return
            self.tcpSocket.disconnectFromHost()
            self.status = False

    def slotConnected(self):
        self.PushButtonSend.setEnabled(True)
        self.PushButtonLeave.setText(self.tr("离开聊天室"))

        msg = self.userName + ":" + self.tr("进入聊天室")
        length1 = self.tcpSocket.writeData(msg.toUtf8())
        if length1 != msg.toUtf8().length():
            return

    def slotDisconnected(self):
        self.PushButtonSend.setEnabled(False)
        self.PushButtonLeave.setText(self.tr("进入聊天室"))
    def dataReceived(self):
        while self.tcpSocket.bytesAvailable() > 0:
            length1 = self.tcpSocket.bytesAvailable()
            msg = QString(self.tcpSocket.read(length1))
            msg = msg.fromUtf8(msg)
            self.ListWidgetContent1.addItem(msg.fromUtf8(msg))
            self.ListWidgetContent1.setCurrentRow(self.ListWidgetContent1.count()-1)

#我的工具线程
    workThread10=WorkThread10()
    workThread11=WorkThread11()
    workThread12=WorkThread12()
    workThread13=WorkThread13()
    workThread14=WorkThread14()
    workThread15=WorkThread15()
    workThread25=WorkThread25()
    workThread26=WorkThread26()
    workThread27=WorkThread27()
    workThread37=WorkThread37()
    workThread38=WorkThread38()
    workThread39=WorkThread39()

###系统工具线程
    workThread1=WorkThread1()
    workThread2=WorkThread2()
    workThread3=WorkThread3()
    workThread4=WorkThread4()
    workThread5=WorkThread5()
    workThread6=WorkThread6()
    workThread7=WorkThread7()
    workThread8=WorkThread8()
    workThread9=WorkThread9()
    workThread16=WorkThread16()
    workThread17=WorkThread17()
    workThread18=WorkThread18()
    workThread19=WorkThread19()
    workThread20=WorkThread20()
    workThread21=WorkThread21()
    workThread22=WorkThread22()
    workThread23=WorkThread23()
    workThread24=WorkThread24()

###推荐工具
    workThread28=WorkThread28()
    workThread29=WorkThread29()
    workThread30=WorkThread30()
    workThread31=WorkThread31()
    workThread32=WorkThread32()
    workThread33=WorkThread33()
    workThread34=WorkThread34()
    workThread35=WorkThread35()
    workThread36=WorkThread36()


app=QApplication(sys.argv)
mytools=MyTools()
# PyQT禁止调整窗口大小:
mytools.setFixedSize(280,490)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/main.ico'), QIcon.Normal, QIcon.Off)
mytools.setWindowIcon(icon)
mytools.setWindowTitle(u"多功能快捷工具箱")
mytools.show()
sys.stdout.flush()
app.exec_()
