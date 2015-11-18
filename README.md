# shortcut_tools
shortcut tools  多功能快捷工具箱
【EXE、源码打包】链接: http://pan.baidu.com/s/1kT3xI7t 密码: 2wd5

![image](http://a.hiphotos.baidu.com/image/pic/item/8cb1cb1349540923edee3d929458d109b2de4952.jpg)

本程序分4块：个人编写的小工具、系统自带程序快捷启动、个人推荐的小软件、聊天室。工具箱应该首先实现的是常用的一般性小工具，不弄鸡肋的功能，所以需要自己实现的功能有：快递查询、手机号码归属地查询、空间自动点赞工具、有道翻译、邮件远程指令功能、系统信息查看、截图、城市天气查询、智能应答机器人、二维码生成、网址安全检测、后台监听功能。

【功能介绍】

1、快递查询

![image](http://i13.tietuku.com/ec763ddb2cb029b8.png)

先选择快递公司然后输入运单号即可查询到快递的物流信息，使用的是快递100的API。在运单号输入框这里应该先把用户输入的运单号去掉前后的空格，因为有时候用户复制的时候经常会有个空格，这就会导致查询失败，甚至程序会因此崩溃。

API: http://wap.kuaidi100.com/wap_result.jsp?rand=20120517&id=快递公司&fromWeb=null&&postid=运单号

主要使用库：requests、BeautifulSoup、PyQt4

2、手机号码归属地查询

![image](http://i12.tietuku.com/63a279172027a3d5.png)

输入手机号号码就能查询到手机号码的运营商、省份、城市。使用的是拍拍网的API，因为很多购物网站都有充值功能，而且有识别手机号码归属地提示等功能，刚好我们可以利用一下。

API: http://virtual.paipai.com/extinfo/GetMobileProductInfo?mobile=手机&amount=10000

主要使用库：requests、PyQt4

3、QQ空间自动点赞

![image](http://i13.tietuku.com/d8f2e8ccc8bc58ac.png)

挺有意思的一个程序，程序一打开就会弹出二维码，用户只需使用手机的QQ安全中心扫描二维码就能登录，首先得感谢https://github.com/xqin/SmartQQ-for-Raspberry-Pi的代码提供，这种登录方法挺巧妙的，因为无需处理验证码的问题，而且智能手机的普及，挺方便的处理方法，虽然这程序用处并不大，但是挺有意思的，无聊可以用用，当个秒赞小王子，点赞的同时，目录下还会生成个日志文件，方便查看。

主要使用库：urllib2、cookielib、logging、PyQt4

4、有道翻译

![image](http://i12.tietuku.com/b66a3be41b7fbdd3.png)

和有道翻译的官网一样的功能，支持多种语言翻译，实现的原理是这样的，首先我们在有道翻译的网页版里，用开发者工具查看翻译的时候post了什么给服务器，然后我们可以看到当点击翻译按钮的时候，会发出请求，将一个json表格POST到服务器，然后再GET结果到浏览器里。所以我们只需模仿这个步骤就能实现到这个功能了。

![image](http://i12.tietuku.com/ec260e778dcb6298.png)

主要使用库：requests、json、PyQt4

5、邮件远程指令功能

![image](http://i5.tietuku.com/7f16b57d0a3b5a0b.png)

这个程序的灵感是来自开源中国网站上一位网友，因为现在手机那么普及，微信、QQ也可以发送邮件，那么我们可以把收发邮件的功能用来当作远程指令不就好了吗。

首先，程序会登录所填写的邮箱，然后读取最新一条邮件，如果邮件的标题是suoping、chongqi、guanji，那么就会执行指定的系统命令，并会发送反馈邮件到指令来源的邮箱里，让用户清楚电脑是否接收到指令，随后会删除带有指令标题的邮件，避免重复执行命令。
主要使用库：poplib、smtplib、ctypes、thread、email

6、系统信息查看

![image](http://i13.tietuku.com/5692e9353382852c.png)

这个没什么特别的，就是查看系统的CPU、内存、磁盘、网络以及进程的信息而已，不过还挺有用的，虽然只是调用了psutil库而已。

主要使用库：psutil、PyQt4

7、截图功能

![image](http://i13.tietuku.com/6ded4f3c0a58b414.png)

这么常用的功能怎么能少，本程序支持全屏截图、当前窗口截图、选择区域截图，并支持快捷键，方便实用。

抓取全屏只需要调用ImageGrab的grab函数即可，当前窗口抓取需要先获取当前窗口的句柄、然后获取当前窗口坐标、最后抓图、保存。然而抓取区域需要调用外部dll，但是后来发现运行缓慢和卡顿，只能无奈选择调用外部截图程序这个方法。

主要使用库：PIL、ctypes、win32gui、wx

8、城市天气查询

![image](http://i13.tietuku.com/f7f66455f7281ed4.png)

本程序是调用万年历（etouch.cn）的API，返回json格式，再转换成字典，最后调取信息即可。

API：http://wthrcdn.etouch.cn/weather_mini?city=城市名字

主要使用库：requests、json、urllib2、PyQt4

9、智能应答机器人

![image](http://i13.tietuku.com/29637850cc9fa119.png)

智能姬可以查询许多东西，比如说查询天气、查看今天的火车、飞机等信息、还可以帮你搜图和教你做菜
。
![image](http://i13.tietuku.com/29637850cc9fa119.png)

遇到链接的时候，只需要先点击一下链接，然后再点击右上角的“用浏览器打开”就能用浏览器打开相关链接。

API：http://www.tuling123.com/

主要使用库：json、webbrowser、urllib2、PyQt4

![image](http://i13.tietuku.com/f7deea2ec2eb44f1.png)

10、二维码生成

![image](http://i13.tietuku.com/2d8a0f07012f5e88.png)

同样也是使用了乐视的二维码API，需要注意把输入的内容需要转换一下编码。

API：http://apistore.baidu.com/apiworks/servicedetail/1017.html

主要使用库：json、urllib2、PyQt4

11、网址安全检测

![image](http://i12.tietuku.com/10c86a8029d92cc5.png)

在这个别人发给你一个链接都要三思而行的时代，这个程序或许能够帮到你，输入网址点击检测，百度网址安全中心就会提示相关信息。

API：http://apistore.baidu.com/apiworks/servicedetail/472.html

主要使用库：json、urllib2、PyQt4

12、后台监听

![image](http://i11.tietuku.com/93fd4d7c292beaec.jpg)

![image](http://i11.tietuku.com/d71315686007f141.jpg)

您是否遇到过，借用电脑给朋友使用，但是却不放心他会不会偷看你的私人文件的情况？只要在后台启用了该程序，便会监听记录键盘的按键信息和粘贴复制事件，同时会保存日志到程序目录下的Monitor文件夹里，而且还会在窗口焦点改变时，自动全屏截图并保存到Monitor目录下的img文件夹里。现在，你可以在后台运行此程序，把电脑借给朋友，测试一下他吧！

其实下一步可以将功能进一步提升，例如自动发送邮件到指定邮箱、或者将信息传输到服务器等。

主要使用库：ctypes、pythoncom、pyHook、win32api、win32con、win32gui、win32ui、Image、PyQt4

13、调用系统自带功能

![image](http://b.hiphotos.baidu.com/image/pic/item/7aec54e736d12f2ea8ccf08c49c2d56284356814.jpg)

方便了一些记不住Win+R的同学，轻松打开系统自带程序。

14、个人推荐程序

![image](http://e.hiphotos.baidu.com/image/pic/item/91ef76c6a7efce1b81d29626a951f3deb58f6564.jpg)

个人觉得挺好用的小工具，反正也不大，而且挺实用的。

15、聊天室

![image](http://g.hiphotos.baidu.com/image/pic/item/fd039245d688d43fd904cf1e7b1ed21b0ff43ba8.jpg)

一个小型且简陋的聊天室，使用的是PyQt里的QtNetwork库。

主要使用库：PyQt4

16、关于

![image](http://e.hiphotos.baidu.com/image/pic/item/a686c9177f3e670985c61b133dc79f3df9dc5513.jpg)
