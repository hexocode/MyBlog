---
title: HCL配置(三)–-DHCP配置
tags:
    - HCL
    - 华三
    - 实验
    - 配置
categories:
    - 网络
    - 华三
date: 2019-09-12 15:42:43
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: 愿你走过半生，归来仍是少年
comments: true
keywords: DHCP配置
description: 
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---



# <font color = "red">HCL配置(三)–-DHCP配置</font>

## 一、任务

> 在实验二的基础上(VLAN10、20、30、40内的主机之间互ping成功)实现用DHCP给各vlan内主机自动分配地址

## 二、配置

由于在上一个实验的基础上，因此只需要配置四个PC和最上面的交换机S0即可

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL3/pic1.png)

### 1、四个PC

使用DHCP，启用接口

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL3/pic2.png)

### 2、最上面的交换机S0

> <font color = "blue">配置DHCP</font>
```
<LwS0>sys
System View: return to User View with Ctrl+Z.
[LwS0]dhcp enable
[LwS0]dhcp server ip-pool vlan10
[LwS0-dhcp-pool-vlan10]network 192.168.10.1 mask 255.255.255.0
[LwS0-dhcp-pool-vlan10]gateway-list 192.168.10.1
[LwS0-dhcp-pool-vlan10]qui
[LwS0]dhcp server ip-pool vlan20
[LwS0-dhcp-pool-vlan20]network 192.168.20.1 mask 255.255.255.0
[LwS0-dhcp-pool-vlan20]gateway-list 192.168.20.1
[LwS0-dhcp-pool-vlan20]quit
[LwS0]dhcp server ip-pool vlan30
[LwS0-dhcp-pool-vlan30]network 192.168.30.1 mask 255.255.255.0
[LwS0-dhcp-pool-vlan30]gateway-list 192.168.30.1
[LwS0-dhcp-pool-vlan30]quit
[LwS0]dhcp server ip-pool vlan40
[LwS0-dhcp-pool-vlan40]network 192.168.40.1 mask 255.255.255.0
[LwS0-dhcp-pool-vlan40]gateway-list 192.168.40.1
[LwS0-dhcp-pool-vlan40]quit
```

> <font color = "blue">保存配置</font>
```
[LwS0]quit
<LwS0>save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
flash:/startup.cfg exists, overwrite? [Y/N]:y
Validating file. Please wait...
Saved the current configuration to mainboard device successfully.
```

## 三、测试

查看各个PC的ip

然后ping另一台PC，能ping通即可





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

