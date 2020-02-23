---
title: HCL配置(一)--ping通及Telnet
tags:
  - HCL
  - 华三
  - 实验
  - 配置
categories:
  - 网络
  - 华三
date: 2019-09-09 21:54:19
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
comments: true
keywords: 简单主机间通信及Telnet
description: 
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---

# <font color="red">HCL配置(一)--PCping通路由器及HostTelnet路由器</font>

## <font color="orange">一、任务</font>
> * 命名R、2S为自己姓名首字母
> * 给设备配置时间
> * PC能够Ping通R
> * Host能telnet路由器


## <font color="orange">二、配置</font>

### 1、新建工程并添加设备
单机图示图标，新建工程，自己命名选择路径保存

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic1.png)

从左边选择设备，拖入操作区，使用GE线缆将设备连接起来，连接Host的时候注意选择有线网卡
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic2.png)

### 2、查看Host的IP并配好PC、Host相关参数
在真机环境中打开命令提示符，输入`ipconfig`获得刚刚新建的网卡IP
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic3.png)
图示显示169...未分配地址，打开网络管理界面，右击Vbox...网卡
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic4.png)
属性--找到Internet协议版本4(TCP/IPv4)，双击后配置静态IP
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic5.png)
禁用－启用该网卡，再次输入`ipconfig`查看IP地址
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic6.png)
启动所有设备
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic7.png)
右击PC，选择配置，输入相关参数，启用接口
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic8.png)




### 3、路由器配置
<kbd>Ctrl</kbd>+<kbd>C</kbd>退出自动配置，按<kbd>enter</kbd>继续
#### (1)修改名称
```
<H3C>system-view
System View: return to User View with Ctrl+Z.
[H3C]sysname LWR
```
#### (2)配置接口
![](web-HCL1/pic9.png)
- G0/0 192.168.11.1     
- G0/1 192.168.10.1

```
[LWR]int g0/0
[LWR-GigabitEthernet0/0]ip add 192.168.11.1 255.255.255.0
[LWR-GigabitEthernet0/0]quit
[LWR]int g0/1
[LWR-GigabitEthernet0/1]ip add 192.168.10.1 255.255.255.0
[LWR-GigabitEthernet0/1]quit
[LWR]dis cur
。。。
#
interface GigabitEthernet0/0
 port link-mode route
 combo enable copper
 ip address 192.168.11.1 255.255.255.0
#
interface GigabitEthernet0/1
 port link-mode route
 combo enable copper
 ip address 192.168.10.1 255.255.255.0
```

#### (3)开启telnet服务
```
[LWR]telnet server enable
[LWR]user-interface vty 0 4
[LWR-line-vty0-4]authentication-mode none
[LWR-line-vty0-4]user level-5
```

真机到控制面板中选择程序，启用服务，勾选Telnet Client，确定，开启telnet功能
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic10.png)




### 4、交换机配置
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic11.png)

S1：
<kbd>Ctrl</kbd>+<kbd>C</kbd>   <kbd>enter</kbd>
```
<H3C>sys
System View: return to User View with Ctrl+Z.
[H3C]sys LWS1
[LWS1]int g1/0/1
[LWS1-GigabitEthernet1/0/1]no sh
[LWS1-GigabitEthernet1/0/1]quit
[LWS1]int g1/0/2
[LWS1-GigabitEthernet1/0/2]no sh
[LWS1-GigabitEthernet1/0/2]quit
```
S2：
<kbd>Ctrl</kbd>+<kbd>C</kbd>   <kbd>enter</kbd>
```
<H3C>sys
System View: return to User View with Ctrl+Z.
[H3C]sys LWS2
[LWS2]int g1/0/1
[LWS2-GigabitEthernet1/0/1]no sh
[LWS2-GigabitEthernet1/0/1]quit
[LWS2]int g1/0/2
[LWS2-GigabitEthernet1/0/2]no sh
[LWS2-GigabitEthernet1/0/2]quit
```
### 5、测试
#### (1)PCping路由器地址

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic12.png)


#### (2)Host(真机)pingR并telnet
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic13.png)
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL1/pic14.png)


### 6、时间配置
<LWR>sys
System View: return to User View with Ctrl+Z.
[LWR]clock p
[LWR]clock protocol none
[LWR]quit
<LWR>clock datetime 21:53:50 2019/09/09

7、保存
<LWR>save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
Validating file. Please wait...
Configuration is saved to device successfully.





------

 **文章汇总：**

<table><tr><td bgcolor=#FFFF00> HCL的安装和使用</td></tr></table>

<kbd>[go->](/2019/09/09/web-HCL0/index.html)</kbd>

<table><tr><td bgcolor=#D1EEEE>ping通及Telnet</td></tr></table>

<kbd>[go->](/2019/09/09/web-HCL1/index.html)</kbd>

<table><tr><td bgcolor=#C0FF3E>VLAN间通信</td></tr></table>

<kbd>[go->](/2019/09/11/web-HCL2/index.html)</kbd>

<table><tr><td bgcolor=#54FF9F>DHCP配置</td></tr></table>

<kbd>[go->](/2019/09/12/web-HCL3/index.html)</kbd>

<table><tr><td bgcolor=#EFFF00> DHCP中继</td></tr></table>

<kbd>[go->](/2019/09/18/web-HCL4/index.html)</kbd>

<table><tr><td bgcolor=#DFEEEE>STP及VRRP配置</td></tr></table>

<kbd>[go->](/2019/09/18/web-HCL5/index.html)</kbd>

<table><tr><td bgcolor=#C0FFFE>RIP配置</td></tr></table>

<kbd>[go->](/2019/09/19/web-HCL6/index.html)</kbd>

<table><tr><td bgcolor=#54FFEF>OSPF配置</td></tr></table>

<kbd>[go->](/2019/09/27/web-HCL7/index.html)</kbd>

<table><tr><td bgcolor=#0FFF00>ACL+NAT配置</td></tr></table>

<kbd>[go->](/2019/09/27/web-HCL8/index.html)</kbd>

<table><tr><td bgcolor=#F1EEEE>使用eNSP搭建企业网络</td></tr></table>

<kbd>[go->](/2019/09/30/web-HCL9/index.html)</kbd>

------

