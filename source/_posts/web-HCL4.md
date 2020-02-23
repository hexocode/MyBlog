---
title: DHCP配置(续)--DHCP中继
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.top
authorAbout: 一个好奇的人
authorDesc: 砥砺前行
comments: true
tags:
  - 华三
  - HCL
date: 2019-09-18 16:14:16
categories: "网络"
keywords: DHCP中继
description:
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---

> 实验目的：DHCP中继

> 配置：
拓扑如下：
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL4/pic1.jpg)
## 一、四个PC
打开DHCP，启用接口
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL4/pic2.jpg)

## 二、交换机S1

```
<H3C>sys
System View: return to User View with Ctrl+Z.
[H3C]sys S1
[S1]vlan 10
[S1-vlan10]vlan 20
[S1-vlan20]quit
[S1]int g1/0/1
[S1-GigabitEthernet1/0/1]no sh
[S1-GigabitEthernet1/0/1]port link-type access
[S1-GigabitEthernet1/0/1]port access vlan 10
[S1-GigabitEthernet1/0/1]quit
[S1]int g1/0/2
[S1-GigabitEthernet1/0/2]no sh
[S1-GigabitEthernet1/0/2]port link-t a
[S1-GigabitEthernet1/0/2]port a vlan 20
[S1-GigabitEthernet1/0/2]quit
[S1]int g1/0/3
[S1-GigabitEthernet1/0/3]no sh
[S1-GigabitEthernet1/0/3]port link-t t
[S1-GigabitEthernet1/0/3]port t p vlan all
[S1-GigabitEthernet1/0/3]quit
[S1]save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
Validating file. Please wait...
Saved the current configuration to mainboard device successfully.
```
## 三、交换机S2
```
[S2]vlan 30
[S2-vlan30]vlan 40
[S2-vlan40]int g1/0/1
[S2-GigabitEthernet1/0/1]no sh
[S2-GigabitEthernet1/0/1]port link-t a
[S2-GigabitEthernet1/0/1]port a vlan 30
[S2-GigabitEthernet1/0/1]int g1/0/2
[S2-GigabitEthernet1/0/2]no sh
[S2-GigabitEthernet1/0/2]port link-t a
[S2-GigabitEthernet1/0/2]port a vlan 40
[S2-GigabitEthernet1/0/2]int g1/0/3
[S2-GigabitEthernet1/0/3]no sh
[S2-GigabitEthernet1/0/3]port link-t t
[S2-GigabitEthernet1/0/3]port t p vlan all
[S2-GigabitEthernet1/0/3]quit
[S2]save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
Validating file. Please wait...
Saved the current configuration to mainboard device successfully.
```
## 四、交换机S3
```
[S0]vlan 10
[S0-vlan10]vlan 20
[S0-vlan20]vlan 30
[S0-vlan30]vlan 40
[S0-vlan40]vlan 50
[S0-vlan50]quit
[S0]int g1/0/1
[S0-GigabitEthernet1/0/1]no sh
[S0-GigabitEthernet1/0/1]port link-t t
[S0-GigabitEthernet1/0/1]port t p vlan all
[S0-GigabitEthernet1/0/1]int g1/0/2
[S0-GigabitEthernet1/0/2]no sh
[S0-GigabitEthernet1/0/2]port link-t t
[S0-GigabitEthernet1/0/2]port t p vlan all
[S0-GigabitEthernet1/0/2]int g1/0/3
[S0-GigabitEthernet1/0/3]no sh
[S0-GigabitEthernet1/0/3]port link-t a
[S0-GigabitEthernet1/0/3]port a vlan 50
[S0-GigabitEthernet1/0/3]quit
[S0]dhcp enable
[S0]int vlan 10
[S0-Vlan-interface10]%Sep 16 18:50:17:155 2019 S0 IFNET/3/PHY_UPDOWN: Physical state on the interface Vlan-interface10 changed to up.
%Sep 16 18:50:17:155 2019 S0 IFNET/5/LINK_UPDOWN: Line protocol state on the interface Vlan-interface10 changed to up.
ip add 192.168.10.1 255.255.255.0
[S0-Vlan-interface10]dhcp select relay
[S0-Vlan-interface10]dhcp relay server-address 192.168.50.2
[S0-Vlan-interface10]int vlan 20
[S0-Vlan-interface20]%Sep 16 18:52:05:444 2019 S0 IFNET/3/PHY_UPDOWN: Physical state on the interface Vlan-interface20 changed to up.
%Sep 16 18:52:05:444 2019 S0 IFNET/5/LINK_UPDOWN: Line protocol state on the interface Vlan-interface20 changed to up.
ip add 192.168.20.1 255.255.255.0
[S0-Vlan-interface20]dhcp select relay
[S0-Vlan-interface20]dhcp relay server-address 192.168.50.2
[S0-Vlan-interface20]int vlan 30
[S0-Vlan-interface30]%Sep 16 18:52:26:073 2019 S0 IFNET/3/PHY_UPDOWN: Physical state on the interface Vlan-interface30 changed to up.
%Sep 16 18:52:26:073 2019 S0 IFNET/5/LINK_UPDOWN: Line protocol state on the interface Vlan-interface30 changed to up.
ip add 192.168.30.1 255.255.255.0
[S0-Vlan-interface30]dhcp select relay
[S0-Vlan-interface30]dhcp relay server-address 192.168.50.2
[S0-Vlan-interface30]int vlan 40
[S0-Vlan-interface40]%Sep 16 18:52:47:327 2019 S0 IFNET/3/PHY_UPDOWN: Physical state on the interface Vlan-interface40 changed to up.
%Sep 16 18:52:47:327 2019 S0 IFNET/5/LINK_UPDOWN: Line protocol state on the interface Vlan-interface40 changed to up.
ip add 192.168.40.1 255.255.255.0
[S0-Vlan-interface40]dhcp select relay
[S0-Vlan-interface40]dhcp relay server-address 192.168.50.2
[S0-Vlan-interface40]int vlan 50
[S0-Vlan-interface50]%Sep 16 18:53:08:122 2019 S0 IFNET/3/PHY_UPDOWN: Physical state on the interface Vlan-interface50 changed to up.
%Sep 16 18:53:08:122 2019 S0 IFNET/5/LINK_UPDOWN: Line protocol state on the interface Vlan-interface50 changed to up.
ip add 192.168.50.1 255.255.255.0
[S0-Vlan-interface50]quit
[S0]save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
Validating file. Please wait...
Saved the current configuration to mainboard device successfully.
```
## 五、路由器R
```
[R]int g0/0
[R-GigabitEthernet0/0]no sh
[R-GigabitEthernet0/0]ip add 192.168.50.2 255.255.255.0
[R-GigabitEthernet0/0]quit
[R]dhcp en
[R]dhcp server ip-pool vlan10
[R-dhcp-pool-vlan10]network 192.168.10.1 mask 255.255.255.0
[R-dhcp-pool-vlan10]gateway-list 192.168.10.1
[R-dhcp-pool-vlan10]quit
[R]dhcp server ip-pool vlan20
[R-dhcp-pool-vlan20]network 192.168.20.1 mask 255.255.255.0
[R-dhcp-pool-vlan20]gateway-list 192.168.20.1
[R-dhcp-pool-vlan20]quit
[R]dhcp server ip-pool vlan30
[R-dhcp-pool-vlan30]network 192.168.30.1 mask 255.255.255.0
[R-dhcp-pool-vlan30]gateway-list 192.168.30.1
[R-dhcp-pool-vlan30]quit
[R]dhcp server ip-pool vlan40
[R-dhcp-pool-vlan40]network 192.168.40.1 mask 255.255.255.0
[R-dhcp-pool-vlan40]gateway-list 192.168.40.1
[R-dhcp-pool-vlan40]quit
[R]ip route-static 192.168.0.0 255.255.0.0 g0/0 192.168.50.1
[R]save
The current configuration will be written to the device. Are you sure? [Y/N]:y
Please input the file name(*.cfg)[flash:/startup.cfg]
(To leave the existing filename unchanged, press the enter key):
Validating file. Please wait...
Configuration is saved to device successfully.
```

> 测试
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL4/pic3.jpg)

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL4/pic4.jpg)







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

