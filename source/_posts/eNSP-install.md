---
title: 安装华为模拟器eNSP
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
tags:
	- HCNA
	- eNSP
categories:
	- 网络
	- HCNA
comments: true
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/cover/(00).jpg'
date: 2020-02-22 21:39:56
keywords: 
---






## 1、根据自己电脑系统选择适合版本下载

本来eNSP在华为官网是可以下载的，但因为安全问题，现只提供给客户下载

因此我将在下面放出下载链接

由于win10和eNSP之间存在兼容性问题，因此需要重点注意，而win7则没有这种顾虑：

 

Win7：随便哪个版本，只需要在安装的时候注意防火墙即可

Win10：这个就有严格的版本要求了

按照网上的以及我自己的测试，eNSP500+vBox5.1.26是没有问题的

·Win10

·eNSP V100R002C00B500 Setup

·VirtualBox-5.1.26-117224-Win

这两个软件我都放在我搭的网盘上了

[链接地址](http://106.54.101.97:34567/A:/official%20accounts/20-02-22eNSP)

密码：wallleap

当然了，直接这样下载可能会有点慢

可以先下载多线程下载工具，比如ADM/IDM等

然后调好线程等设置再下载这两个软件

这些在网盘中都可以找到

## 2、win10安装注意事项

首先安装eNSP，前面的只有一个按钮选项，点击就行

到这步，点击“我愿意接受此协议”，接着点“下一步”

![img](https://mmbiz.qpic.cn/mmbiz_png/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygUx74eZH1j1PmHLCb7fFIoqaU5tJAkSCflxYBIQZBDAmrFGhgPL4bCw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



安装位置的话，直接修改成磁盘根目录/eNSP、

![img](https://mmbiz.qpic.cn/mmbiz_png/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygvBbElvl4kJk4lJAL2Dzq6a7eUSyozF2sCbSTBTuBmwicGEoqKVYvewA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



在到这里需要注意下，取消勾选“安装VirtualBox 5.0.16”前的复选框，接着点击“下一步”

![img](https://mmbiz.qpic.cn/mmbiz_png/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygSZ9ia5lHqlFsg24HTdJH6gRp3ZJCtTe54zPHiaFBs3ywQqZJUVsp0IEw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



接着按提示安装完eNSP、WinPcap、Wirehark即可

基本上这些都可以默认的，直接点下一步、next、Install、Finish即可

注意，安装完成之后不要立即打开eNSP，也就是在这一步取消复选框再点完成

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygQ0rStFxylujU1IoMnJpZ9RhpfLkdOONU7XoYfPZHptPkeH5pLa695Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygMFOp6XEn7jINxaDXghXqGxEfG1UriaGsh9HfiaC3n1cFZZwan7mvg3wA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



接下来就可以安装VBox了

好吧，在安装VBox之前，部分电脑还需要进入BIOS开启虚拟化功能

给一个参考链接，https://jingyan.baidu.com/article/574c52195b675c6c8d9dc138.html

如果和这个不同自行百度

开启虚拟化后，进入系统，双击VBox安装包进行安装

同理，更改下目录，当然，这里用默认的目录也可以

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygRmBAzA5POI547Lp5iaZ28Ux0Nia1A26rwNVN4fYG4CEicGxxvuTatIpnw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



如果安装过程中弹窗，请点击“是”

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygmLeDibAvGYQaY5vpXsx5YkGbUf2EUOiajAfiaWfLw5hutFea0TCN6GXlQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



第一次安装，可能会弹出下面这个界面，咱点击“安装”

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygF6KqE1nQQZCmmMZSQia1Bo61LAbDYia3nHOHJA0cbjUQQJ8WibAbNnGSQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

到这个界面，VBox也安装完成了

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygehuBsgiaEDFGS6gwnUl8uhqfnhAezjVc3YprNtE6VIl0tmq0egGSzicw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 3、其他设置

### 防火墙

我们使用eNSP中的设备需要在防火墙中运行eNSP相关服务访问

当然，我们可以直接关掉系统的防火墙，毕竟我们会安装安全防护软件，这里推荐使用火绒

首先进入控制面板

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygd2PyEibFy7lu5tmC2mqWcibsbrF2A1HAqBHg5Vvl3FIXxznc4gMiadC8w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



按照下图，点击进入这个位置

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygglqXObQ1HIrich96UKf6G7qUyjKOCPAzKLj4guuvzHTOmnRqzNibjdJw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



点击左边的“高级设置”

再点击“属性”，把这三项都设置为关闭

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygAUesaYoImmj9ib25CAKvmdDHeXVjG0wPBWOsvxbxeRwdzGGeWcMKvmQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



看到这个就是关闭成功了

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfyg8l1TqRUCPBqGh0mqqPPN4J8cdPepHstIMNlzaS2Nx04l3icr59qZNIA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



### 注册设备

现在我们进入VBox，这里没有设备，我们需要进入eNSP设置

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygXwL2geG7C7rB8BAicficLdsIibibYnjf2hxKI5DtaPuBKxuYCbbqUble0w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



进入eNSP，点击左上角，新建一个空白的拓扑

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygdp63yCKqxBZFY5zbWgiaENxXrEE286g3s78BhVSLYPbNeiasJSJ24Izg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



再点击右上方的菜单-工具-注册设备

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfyguHZHIysY69p47Yrp3VDichU63ccIK1gsV8UIk5ISicIeicvZ0r6mT5ibkw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



勾选三个复选框，点击注册

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfyg9OjvsWuynHD7NLW2toiaPPRhWK6fLAAlpJBg6p39WNgPWtHRp1Llm1w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



好吧，弄完之后VBox还是看不到设备

我们在拓扑上添加上设备测试一下，路由器选择AR3260(基本上这个能用其他的都OK了)，交换机选择S3700

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygvQWddX0Lt2JRdJF4kQMwvse0da1Ze8cLicxVAlON1Mpvzy9FAFJK21A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



启动一下所有的设备，没有弹出错误，等待一会变成绿色，点进设备，没有######

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygibPuZJib0FprT3YJNXK0099ahPIekBibBSWKKImGv4V0zicxFyjLQKdz8A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/bQicJnZn4LHSXHk7JH3ngB3gl2s7SLfygIe3jQQA9JITv1VFHVbjCMlPlDicqicuXEiaONWHnxrfVykwWk0Y2UBtdg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



一般这样就OK了

## 补充

按照上面的肯定就不会有错了，但是，出现的一般错误还是要说下的

 **显示“错误代码40”** 

这个可以直接点击解决方案，按照那上面的一个个解决

**一直输出#号**

就是系统防火墙的问题，关掉就行

 











**☆ END ☆**