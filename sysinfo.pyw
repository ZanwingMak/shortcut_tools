# -*- coding: utf-8 -*-
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import psutil
import datetime
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


def get_my_ip():
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
                return u'联网查询外网ip失败...'
                my_ip = 'None'
    if my_ip != 'None':
        return (u'您的外(公)网ip是:' + my_ip)
        #return my_ip

def process():
    all_process_pid = psutil.pids()
    text = u'-------------------------------当前进程列表-------------------------------\n\n'
    text = text + u'[PID]\t  [进程名]\t\t      [创建时间]\t\t[线程数]\n'
    text = text + '--------------------------------------------------------------------------\n'
    for i in range(len(all_process_pid)):
        p = psutil.Process(all_process_pid[i])
        text = text + u'%-10s%-28s%-20s\t%s\n' % (all_process_pid[i],p.name(),datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S"),p.num_threads())
    text = text + '--------------------------------------------------------------------------'

    sysinfo.label2.setText(sysinfo.tr(text))
def network():
    ip = get_my_ip()
    text = ip + '\n'
    text = text + '==================\n'
    total_network = psutil.net_io_counters()
    total_bytes_sent = '%.2f M' % (total_network[0]/1024.0/1024.0)
    total_bytes_recv = '%.2f M' % (total_network[1]/1024.0/1024.0)
    text = text + u"★总发送流量：%s  总接收流量：%s\n"%(total_bytes_sent,total_bytes_recv)
    text = text + u"★总发送数据包数：%s  总接收数据包数：%s\n"%(total_network[2],total_network[3])
    network = psutil.net_io_counters(pernic=True)
    network_keys = network.keys()
    print
    for i in range(len(network_keys)):
        this_network = network.get(network_keys[i])
        this_network_name = (network_keys[i]).decode('gbk')
        bytes_sent = this_network[0]
        bytes_recv = this_network[1]
        packets_sent = this_network[2]
        packets_recv = this_network[3]

        this_bytes_sent = '%.2f M' % (bytes_sent/1024.0/1024.0)
        this_bytes_recv = '%.2f M' % (bytes_recv/1024.0/1024.0)
        this_packets_sent = '%d' % (packets_sent)
        this_packets_recv = '%d' % (packets_recv)
        text = text + '==================\n'
        text = text +u'网卡：'+ this_network_name +'\n'
        text = text + u"发送流量：%s  接收流量：%s\n"%(this_bytes_sent,this_bytes_recv)
        text = text + u"发送数据包数：%s  接收数据包数：%s\n"%(this_packets_sent,this_packets_recv)


    sysinfo.label2.setText(sysinfo.tr(text))
def disk():
    disk_partitions = psutil.disk_partitions()
    disk_len = len(disk_partitions)
    text = u'[当前磁盘有%d个分区]\n' % disk_len
    for i in range(disk_len):
        text = text + (u'盘符：%s 挂载点：%s 文件系统：%s 属性：%s\n' % ((disk_partitions[i][0])[0:1],(disk_partitions[i][1])[0:1],disk_partitions[i][2],(disk_partitions[i][3])))
    disk_io_counters = psutil.disk_io_counters(perdisk=False)
    text = text + (u'磁盘读取IO个数：%d\n' % disk_io_counters.read_count)
    text = text + (u'磁盘写入IO个数：%d\n' % disk_io_counters.write_count)
    text = text + (u'磁盘读取IO字节数：%d B\n' % disk_io_counters.read_bytes)
    text = text + (u'磁盘写入IO字节数：%d B\n' % disk_io_counters.write_bytes)
    text = text + (u'磁盘读取时间：%s\n' % disk_io_counters.read_time)
    text = text + (u'磁盘写入时间：%s\n' % disk_io_counters.write_time)
    disk = psutil.disk_usage('/')
    text = text + (u'磁盘分区(不包括系统盘)总容量：%.2fG\n' % (disk.total/1024.0/1024.0/1024.0))
    text = text + (u'磁盘分区(不包括系统盘)已用空间：%.2fG\n' % (disk.used/1024.0/1024.0/1024.0))
    text = text + (u'磁盘分区(不包括系统盘)可用空间：%.2fG\n' % (disk.free/1024.0/1024.0/1024.0))
    text = text + (u'磁盘分区(不包括系统盘)空间占用率：%s%%' % disk.percent)

    sysinfo.label2.setText(sysinfo.tr(text))
def memory():
    memory = psutil.virtual_memory()
    text = u'总内存：%.2fM\n' % (memory.total/1024.0/1024.0)
    text = text + (u'已使用内存：%.2fM\n' % (memory.used/1024.0/1024.0))
    text = text + (u'内存占用率：%s%%\n' % memory.percent)
    text = text + (u'可用内存：%.2fM\n' % (memory.available/1024.0/1024.0))
    text = text + (u'空闲内存：%.2fM' % (memory.free/1024.0/1024.0))

    sysinfo.label2.setText(sysinfo.tr(text))
def cpu():
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_times = psutil.cpu_times()
    text = u"CPU逻辑个数：%d\n" % psutil.cpu_count()
    text = text + (u"CPU物理个数：%d\n" % psutil.cpu_count(logical=False))
    text = text + (u'CPU时间比：[用户进程:%s  内核进程:%s  空闲(IDLE):%s]\n' % (cpu_times.user,cpu_times.system,cpu_times.idle))
    text = text + (u'CPU当前使用率：[用户进程:%s%%  内核进程:%s%%  空闲(IDLE):%s%%]\n' % (cpu_times_percent.user,cpu_times_percent.system,cpu_times_percent.idle))
    text = text + (u'CPU当前总使用率：%s%%' % psutil.cpu_percent())

    sysinfo.label2.setText(sysinfo.tr(text))
class WorkThread1(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread1,self).__init__()

    def render(self,select):
        self.select = select
        self.start()

    def run(self):
        if self.select == '1':
            cpu()
        elif self.select == '2':
            memory()
        elif self.select == '3':
            disk()
        elif self.select == '4':
            network()
        elif self.select == '5':
            process()



class SYSINFO(QDialog):
    def __init__(self,parent=None):
        super(SYSINFO,self).__init__(parent)
        self.setWindowTitle(self.tr(u"系统信息查看"))

        mainLayout=QGridLayout(self)
        hb1 = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText(self.tr(u'%s用户,您好!请选择需要查看的系统信息：' % (psutil.users()[0][0])))
        hb1.addWidget(self.label1)

        hb2 = QHBoxLayout()
        self.radio1 = QRadioButton(u'CPU')
        self.radio2 = QRadioButton(u'内存')
        self.radio3 = QRadioButton(u'磁盘')
        self.radio4 = QRadioButton(u'网络')
        self.radio5 = QRadioButton(u'当前进程列表')
        self.btn_ok = QPushButton(self)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_ok.setText(self.tr("查看"))
        hb2.addWidget(self.radio1)
        hb2.addWidget(self.radio2)
        hb2.addWidget(self.radio3)
        hb2.addWidget(self.radio4)
        hb2.addWidget(self.radio5)
        hb2.addWidget(self.btn_ok)


        scroll = QScrollArea()
        self.label2 = QLabel()
        scroll.setBackgroundRole(QPalette.Dark)
        scroll.setWidget(self.label2)
        scroll.setWidgetResizable(True)
        hb3 = QHBoxLayout(self)
        hb3.addWidget(scroll)

        mainLayout.addLayout(hb1,0,0)
        mainLayout.addLayout(hb2,1,0)
        mainLayout.addLayout(hb3,2,0)

    #退出事件
    def closeEvent(self, event):
            event.accept()
            sys.exit(0)

    def btn_ok_Clicked(self):
        if self.radio1.isChecked():
            select = '1'
        elif self.radio2.isChecked():
            select = '2'
        elif self.radio3.isChecked():
            select = '3'
        elif self.radio4.isChecked():
            select = '4'
        elif self.radio5.isChecked():
            select = '5'
        else:
            QMessageBox.information(self,u'错误',u'请先选择需要查看的信息！')
            return -1
        self.workThread1.render(select)

    workThread1=WorkThread1()

app=QApplication(sys.argv)
sysinfo=SYSINFO()
sysinfo.setFixedSize(520,260)
icon = QIcon()
icon.addPixmap(QPixmap('./icon/myTools_icon/system_info.ico'), QIcon.Normal, QIcon.Off)
sysinfo.setWindowIcon(icon)
sysinfo.show()
app.exec_()
