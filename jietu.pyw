#coding=gb2312

import pyhk
import wx
import os
import sys
from PIL import ImageGrab
import ctypes
import win32gui
import ctypes.wintypes
import time

def capture_fullscreen():
    '''
    Function:全屏抓图
    '''
    #抓图
    pic = ImageGrab.grab()
    #保存图片
    save_pic(pic)

def capture_current_windows():
    '''
    Function:抓取当前窗口
    '''
    #窗口结构
    class RECT(ctypes.Structure):
        _fields_ = [('left',ctypes.c_long),('top',ctypes.c_long),('right',ctypes.c_long),('bottom',ctypes.c_long)]

        def __str__(self):
            return str((self.left,self.top,self.right,self.bottom))

    rect = RECT()

    #获取当前窗口的句柄
    HWND = win32gui.GetForegroundWindow()
    #获取当前窗口坐标
    ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
    #调整坐标
    rangle = (rect.left+2,rect.top-2,rect.right-2,rect.bottom-2)
    #抓图
    pic = ImageGrab.grab(rangle)
    #保存
    save_pic(pic)

def capture_choose_windows():
    '''
    Function:抓取选择的区域，没有自己写这个，借用别人的抓图功能
    '''
    #try:
    #     #加载抓图用的dll
    #     dll_handle = ctypes.cdll.LoadLibrary('CameraDll.dll')
    #except Exception:
    #         try:
    #             #如果dll加载失败，则换种方法使用，直接运行，如果还失败，退出
    #             os.startfile("Rundll32.exe CameraDll.dll, CameraSubArea")
    #         except Exception:
    #             return
    #else:
    #     try:
    #         #加载dll成功，则调用抓图函数，注:没有分析清楚这个函数带的参数个数
    #         #及类型，所以此语句执行后会报参数缺少4个字节，但不影响抓图功能，所
    #         #以直接忽略了些异常
    #         dll_handle.CameraSubArea(0)
    #     except Exception:
    #         return
    os.startfile('SNAPSHOT.EXE')#调用被人的自由截图功能


def save_pic(pic):
    '''
    Function:使用文件对话框，保存图片
    '''
    #cc=time.gmtime()  
    #filename=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.png'
    time_temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    a1 = str(time_temp)[0:4]
    a2 = str(time_temp)[5:7]
    a3 = str(time_temp)[8:10]
    a4 = str(time_temp)[11:13]
    a5 = str(time_temp)[14:16]
    a6 = str(time_temp)[17:19]
    now_time = (a1+a2+a3+a4+a5+a6)
    filename = now_time + '.png'
    app = wx.PySimpleApp()
    wildcard = 'PNG(*.png)|*.png'
    dialog = wx.FileDialog(None,'请选择保存路径',os.getcwd(),filename,wildcard,wx.SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        pic.save(dialog.GetPath().encode('gb2312'))
    else:
        pass
    dialog.Destroy()

def close():
    wx.Exit()
    sys.exit(0)

def main():
    '''
    Function:主函数，注册快捷键
    '''
    #创建hotkey句柄
    hot_handle = pyhk.pyhk()
    #注册抓取全屏快捷键Ctrl+Alt+F2
    hot_handle.addHotkey(['Ctrl','Alt','F2'],capture_fullscreen)
    #注册抓取当前窗口快捷键Ctrl+Alt+F3
    hot_handle.addHotkey(['Ctrl','Alt','F3'],capture_current_windows)
    #注册抓取所选区域快捷键Ctrl+Alt+F5
    hot_handle.addHotkey(['Ctrl','Alt','F5'],capture_choose_windows)
    #退出截图工具快捷键Ctrl+Alt+F12
    hot_handle.addHotkey(['Ctrl','Alt','F12'],close)

    #开始运行
    hot_handle.start()

if __name__ == '__main__':
    main()
