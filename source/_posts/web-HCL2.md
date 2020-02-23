---
title: HCL配置(二)--VLAN间通信
tags:
  - HCL
  - 华三
  - 实验
  - 配置
categories:
  - 网络
  - 华三
date: 2019-09-11 18:06:05
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
comments: true
keywords: VLAN间通信
description: 
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---

# <font color="red">HCL配置(二)--VLAN间通信</font>

## <font color="orange">一、任务</font>

> Vlan间通信：
VLAN10、20、30、40内的主机之间互ping成功

## <font color="orange">二、配置</font>

### <font color="pink">(一)通过三层交换机使用SVI实现通信</font>

拓扑图如下：

![拓扑](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL2/pic1.png)

主机IP：
- `PC1：　192.168.10.100/24`
- `PC2：　192.168.20.100/24`
- `PC3：　192.168.30.100/24`
- `PC4：　192.168.40.100/24`

VLANIP规划：
- `VLAN10：　192.168.10.1/24`
- `VLAN20：　192.168.20.1/24`
- `VLAN30：　192.168.30.1/24`
- `VLAN40：　192.168.40.1/24`

#### 1、配置PC
配置好IP地址，掩码，网关（网关是VLAN的IP）

#### 2、最上面的交换机S0
> 命名
```
<H3C>sys
System View: return to User View with Ctrl+Z.
[H3C]sys LWS0
```
>创建四个vlan
```
[LWS0]vlan 10
[LWS0-vlan10]quit
[LWS0]vlan 20
[LWS0-vlan20]vlan 30
[LWS0-vlan30]vlan 40
[LWS0-vlan40]quit
```
> 给vlan分配IP
```
[LWS0]int vlan 10
[LWS0-Vlan-interface10]ip add 192.168.10.1 255.255.255.0
[LWS0-Vlan-interface10]quit
[LWS0]int vlan 20
[LWS0-Vlan-interface20]ip add 192.168.20.1 255.255.255.0
[LWS0-Vlan-interface20]int vlan 30
[LWS0-Vlan-interface30]ip add 192.168.30.1 255.255.255.0
[LWS0-Vlan-interface30]int vlan 40
[LWS0-Vlan-interface40]ip add 192.168.40.1 255.255.255.0
[LWS0-Vlan-interface40]quit
```
>接口设为trunk并允许所有vlan通过
```
[LWS0]int g1/0/1
[LWS0-GigabitEthernet1/0/1]port link-type trunk
[LWS0-GigabitEthernet1/0/1]port trunk permit vlan all
[LWS0-GigabitEthernet1/0/1]no sh
[LWS0-GigabitEthernet1/0/1]int g1/0/2
[LWS0-GigabitEthernet1/0/2]no sh
[LWS0-GigabitEthernet1/0/2]port link-ty t
[LWS0-GigabitEthernet1/0/2]port t p vlan all
```

#### 3、左边交换机S1
> 命名
```
<H3C>sys
System View: return to User View with Ctrl+Z.
[H3C]sys LWS1
创建vlan
[LWS1]vlan 10
[LWS1-vlan10]vlan 20
[LWS1-vlan20]quit
```
> 与交换机相连的接口设为trunk，允许所有vlan通过
```
[LWS1-GigabitEthernet1/0/1]no sh
[LWS1-GigabitEthernet1/0/1]port link-ty t
[LWS1-GigabitEthernet1/0/1]port t p vlan all
[LWS1-GigabitEthernet1/0/1]quit
```
>下面两个接口设为access
```
[LWS1]int g1/0/2
[LWS1-GigabitEthernet1/0/2]port link-ty a
[LWS1-GigabitEthernet1/0/2]port a vlan 10
[LWS1-GigabitEthernet1/0/2]int g1/0/3
[LWS1-GigabitEthernet1/0/3]no sh
[LWS1-GigabitEthernet1/0/3]port link-ty a
[LWS1-GigabitEthernet1/0/3]port a vlan 20
[LWS1-GigabitEthernet1/0/3]quit
```

#### 4、右边交换机S2
```
[LWS2]vlan 30
[LWS2-vlan30]vlan 40
[LWS2-vlan40]quit
[LWS2]int g1/0/1
[LWS2-GigabitEthernet1/0/1]port link-ty t
[LWS2-GigabitEthernet1/0/1]port t p vlan all
[LWS2-GigabitEthernet1/0/1]quit
[LWS2]int g1/0/2
[LWS2-GigabitEthernet1/0/2]port link-ty a
[LWS2-GigabitEthernet1/0/2]port a vlan 30
[LWS2-GigabitEthernet1/0/2]int g1/0/3
[LWS2-GigabitEthernet1/0/3]port link-ty a
[LWS2-GigabitEthernet1/0/3]port a vlan 40
[LWS2-GigabitEthernet1/0/3]quit
```

#### 5、测试
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL2/pic2.png)


### <font color="pink">(二)其他方法</font>

其他的网上有详细的配置，因此只给出方法

1、如果只有两个VLAN，那么可以在交换机端口设置trunk的本征VLAN，自行去标签

多个VLAN的话设成Hybrid口，用untag撕去标签

2、通过路由接口

3、通过单臂路由







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

