---
title: 使用eNSP搭建企业网络
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
authorAbout: 一个好奇的人
authorDesc: 一个好奇的人
comments: true
tags:
  - eNSP
  - 企业网
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner8.jpg'
date: 2019-09-30 07:58:17
categories:
  - 网络
keywords: 搭建企业网
description:
---

局域网内的具体技术：如利用vlan进行业务隔离；通过stp技术来防止环路，保证冗余链路的正常通信；学会使用VRRP技术来实现负载分担以及防止单点故障；利用OSPF协议使得总部和分布的网络能够正常通信；以及运用ACL和NAT对数据流进行控制和去外网通信。

## 实验拓扑图

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic1.png) 

## 实验配置

### (1)vlan间路由

**接入层交换机LSW4**

**创建VLAN**

[LSW4]vlan 10

[LSW4-vlan10]vlan 20

[LSW4-vlan20]quit



配置与主机相连的接口为Access并绑定VLAN

**[LSW4]int e0/0/1**

**[LSW4-Ethernet0/0/1]un sh**

**Info: Interface Ethernet0/0/1 is not shutdown.**

**[LSW4-Ethernet0/0/1]port link-t a**

**[LSW4-Ethernet0/0/1]port de vlan 10**

**[LSW4-Ethernet0/0/1]int e0/0/2**

**[LSW4-Ethernet0/0/2]port link-t a**

**[LSW4-Ethernet0/0/2]port de vlan 20**



**配置与交换机相连的接口为Trunk并允许所有VLAN通过**

**[LSW4-Ethernet0/0/2]int e0/0/3**

**[LSW4-Ethernet0/0/3]port link-t t**

**[LSW4-Ethernet0/0/3]port t allow vlan all**

**[LSW4-Ethernet0/0/3]int e0/0/4**

**[LSW4-Ethernet0/0/4]port link-t t**

**[LSW4-Ethernet0/0/4]port t allow vlan all**

**[LSW4-Ethernet0/0/4]quit**

**l** **接入层交换机LSW5**

**与LSW4类似，创建VLAN，设置接口即可**

**[LSW5]vlan 30**

**[LSW5-vlan30]vlan 40**

**[LSW5-vlan40]quit**

**[LSW5]int e0/0/1**

**[LSW5-Ethernet0/0/1]port link-t a**

**[LSW5-Ethernet0/0/1]port de vlan 30**

**[LSW5-Ethernet0/0/1]int e0/0/2**

**[LSW5-Ethernet0/0/2]port link-t a**

**[LSW5-Ethernet0/0/2]port de vlan 40**

**[LSW5-Ethernet0/0/2]int e0/0/3**

**[LSW5-Ethernet0/0/3]port link-t t**

**[LSW5-Ethernet0/0/3]port t allow vlan all**

**[LSW5-Ethernet0/0/3]int e0/0/4**

**[LSW5-Ethernet0/0/4]port link-t t**

**[LSW5-Ethernet0/0/4]port t allow vlan all**

**[LSW5-Ethernet0/0/4]quit**

**核心层交换机LSW1**

**创建VLAN**

**[LSW1]vlan 10**

**[LSW1-vlan10]vlan 20**

**[LSW1-vlan20]vlan 30**

**[LSW1-vlan30]vlan 40**

**[LSW1-vlan40]vlan 50**

**[LSW1-vlan50]quit**

**与交换机相连接口设为Trunk并允许所有VLAN通过**

**[LSW1]int g0/0/1**

**[LSW1-GigabitEthernet0/0/1]port link-t t**

**[LSW1-GigabitEthernet0/0/1]port t allow vlan all**

**[LSW1-GigabitEthernet0/0/1]int g0/0/3**

**[LSW1-GigabitEthernet0/0/3]port link-t t**

**[LSW1-GigabitEthernet0/0/3]port t allow vlan all**

**[LSW1-GigabitEthernet0/0/3]int g0/0/2**

**[LSW1-GigabitEthernet0/0/2]port link-t t**

**[LSW1-GigabitEthernet0/0/2]port t allow vlan all**

**服务器接入VLAN50，将将与服务器相连的接口设为Access口并绑定VLAN50**

**[LSW1-GigabitEthernet0/0/2]int g0/0/5**

**[LSW1-GigabitEthernet0/0/5]port link-t a**

**[LSW1-GigabitEthernet0/0/5]port de vlan 50**

**[LSW1-GigabitEthernet0/0/5]quit**

**给连接路由器的接口绑定VLAN*60，方便配置地址**

**[LSW1]vlan 60**

**[LSW1-vlan60]int g0/0/4**

**[LSW1-GigabitEthernet0/0/4]port link-t a**

**[LSW1-GigabitEthernet0/0/4]port de vlan 60**

**[LSW1-GigabitEthernet0/0/4]quit**

　**给VLAN分配IP地址（配置真实网关）**

**[LSW1]int vlan 10**

**[LSW1-Vlanif10]ip add 192.168.10.1 24**

**[LSW1-Vlanif10]int vlan 20**

**[LSW1-Vlanif20]ip add 192.168.20.1 24**

**[LSW1-Vlanif20]int vlan 30**

**[LSW1-Vlanif30]ip add 192.168.30.1 24**

**[LSW1-Vlanif30]int vlan 40**

**[LSW1-Vlanif40]ip add 192.168.40.1 24**

**[LSW1-Vlanif40]int vlan 50**

**[LSW1-Vlanif50]ip add 192.168.50.1 24**

**[LSW1-Vlanif50]int vlan 60**

**[LSW1-Vlanif60]ip add 192.168.60.1 24**

**[LSW1-Vlanif60]quit**

**l** **核心层交换机LSW２**

**与LSW１类似，创建VLAN、配置好接口、设置真实网关（与S１地址不同）**

**[LSW2]vlan 10**

**[LSW2-vlan10]vlan 20**

**[LSW2-vlan20]vlan 30**

**[LSW2-vlan30]vlan 40**

**[LSW2-vlan40]quit**

**[LSW2]int g0/0/1**

**[LSW2-GigabitEthernet0/0/1]port link-t t**

**[LSW2-GigabitEthernet0/0/1]port t allow vlan all**

**[LSW2-GigabitEthernet0/0/1]int g0/0/2**

**[LSW2-GigabitEthernet0/0/2]port link-t t**

**[LSW2-GigabitEthernet0/0/2]port t allow vlan all**

**[LSW2-GigabitEthernet0/0/2]int g0/0/3**

**[LSW2-GigabitEthernet0/0/3]port link-t t**

**[LSW2-GigabitEthernet0/0/3]port t allow vlan all**

**[LSW2-GigabitEthernet0/0/3]quit**

**[LSW2]vlan 70**

**[LSW2-vlan70]int g0/0/4**

**[LSW2-GigabitEthernet0/0/4]port link-t a**

**[LSW2-GigabitEthernet0/0/4]port de vlan 70**

**[LSW2-GigabitEthernet0/0/4]quit**

**[LSW2]int vlan 10**

**[LSW2-Vlanif10]ip add 192.168.10.2 24**

**[LSW2-Vlanif10]int vlan 20**

**[LSW2-Vlanif20]ip add 192.168.20.2 24**

**[LSW2-Vlanif20]int vlan 30**

**[LSW2-Vlanif30]ip add 192.168.30.2 24**

**[LSW2-Vlanif30]int vlan 40**

**[LSW2-Vlanif40]ip add 192.168.40.2 24**

**[LSW2-Vlanif40]int vlan 70**

**[LSW2-Vlanif70]ip add 192.168.70.2 24**

**[LSW2-Vlanif70]quit**

### (2)DHCP的搭建

**l** **客户端开启DHCP**

**l** **交换机LSW１和LSW２上配置DHCP服务**

**开启DHCP服务**

**[SW1]dhcp en**

**Info: The operation may take a few seconds. Please wait for a moment.done.**

**创建地址池vlan10、vlan20、vlan30、vlan40，其中＄代表１~４，网关使用之后配置的虚拟网关**

**[LSW1]ip pool vlan＄0**

**Info:It's successful to create an IP address pool.**

**[LSW1-ip-pool-vlan$0]gateway-list 192.168.10.254**

**[LSW1-ip-pool-vlan$0]network 192.168.＄0.0 mask 255.255.255.0**

**[LSW1-ip-pool-vlan$0]quit**

**VLAN绑定地址池**

**[LSW1]int vlan** **＄0**

**[LSW1-Vlanif$0]dhcp select global** 

**[LSW1-Vlanif$0]quit**

**LSW１排除地址**

**[LSW1-ip-pool-vlan$0]excluded-ip-address 192.168.＄0.1 192.168.＄0.127**

**LSW２排除地址**

**[LSW2-ip-pool-vlan$0]ex 192.168.＄0.128 192.168.＄0.253**



### (3) STP+VRRP的配置

**l** **汇聚层交换机LSW４、LSW５只需要开启STP即可**

[LSW4]stp mode stp

Info: This operation may take a few seconds. Please wait for a moment...done.

[LSW5]stp mode stp

Info: This operation may take a few seconds. Please wait for a moment...done.

**l** **核心层LSW１配置**

开启STP

[LSW1]stp mode stp

Info: This operation may take a few seconds. Please wait for a moment...done.

设置LSW1为根桥

[LSW1]stp priority 0

配置VRRP，LSW1是VLAN10、VLAN20的Master，当上层接口错误时，自动降低优先级，让LSW2成为Master

[LSW1]int vlan 10

[LSW1-Vlanif10]vrrp vrid 10 vi 192.168.10.254

[LSW1-Vlanif10]vrrp vrid 10 prio 120

[LSW1-Vlanif10]vrrp vrid 10 track int g0/0/4 reduce 30

[LSW1-Vlanif10]int vlan 20

[LSW1-Vlanif20]vrrp vrid 20 vi 192.168.20.254

[LSW1-Vlanif20]vrrp vrid 20 prio 120

[LSW1-Vlanif20]vrrp vrid 20 track int g0/0/4 re 30

[LSW1-Vlanif20]int vlan 30

[LSW1-Vlanif30]vrrp vrid 30 vi 192.168.30.254

[LSW1-Vlanif30]int vlan 40

[LSW1-Vlanif40]vrrp vrid 40 vi 192.168.40.254

[LSW1-Vlanif40]quit

**l** **核心层LSW２配置**

开启STP，并将优先级设为4096

[LSW2]stp mode stp

Info: This operation may take a few seconds. Please wait for a moment...done.

[LSW2]stp prio 4096

配置VRRP，LSW2是VLAN30、VLAN40的Master，当上层接口错误时，自动降低优先级，让LSW1成为Master

[LSW2]int vlan 10

[LSW2-Vlanif10]vrrp vrid 10 vi 192.168.10.254

[LSW2-Vlanif10]int vlan 20

[LSW2-Vlanif20]vrrp vrid 20 vi 192.168.20.254

[LSW2-Vlanif20]int vlan 30

[LSW2-Vlanif30]vrrp vrid 30 vi 192.168.30.254

[LSW2-Vlanif30]vrrp vrid 30 prio 120

[LSW2-Vlanif30]vrrp vrid 30 track int g0/0/4 re 30

[LSW2-Vlanif30]int vlan 40

[LSW2-Vlanif40]vrrp vrid 40 vi 192.168.40.254

[LSW2-Vlanif40]vrrp vrid 40 prio 120

[LSW2-Vlanif40]vrrp vrid 40 track int g0/0/4 re 30

[LSW2-Vlanif40]quit



### (4)OSPF的搭建



**l** **LSW１OSPF配置**

**查看接口IP**

**[LSW1]dis ip int br**

**Interface                         IP Address/Mask      Physical   Protocol**  

**MEth0/0/1                         unassigned           down       down**      

**NULL0                             unassigned           up         up(s)**     

**Vlanif1                           unassigned           up         down**      

**Vlanif10                          192.168.10.1/24      up         up**        

**Vlanif20                          192.168.20.1/24      up         up**        

**Vlanif30                          192.168.30.1/24      up         up**        

**Vlanif40                          192.168.40.1/24      up         up**        

**Vlanif50                          192.168.50.1/24      up         up**        

**Vlanif60                          192.168.60.1/24      up         up**        

**根据所有IP宣告相应网段**

**[LSW1]ospf 1**

**[LSW1-ospf-1]area 0.0.0.0**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.10.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.20.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.30.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.40.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.50.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]net 192.168.60.0 0.0.0.255**

**[LSW1-ospf-1-area-0.0.0.0]quit**

**[LSW1-ospf-1]qu**

**l** **LSW２OSPF配置**

**与LSW1类似**

**[LSW2]dis ip int br**

**Interface                         IP Address/Mask      Physical   Protocol**  

**MEth0/0/1                         unassigned           down       down**      

**NULL0                             unassigned           up         up(s)**     

**Vlanif1                           unassigned           up         down**      

**Vlanif10                          192.168.10.2/24      up         up**        

**Vlanif20                          192.168.20.2/24      up         up**        

**Vlanif30                          192.168.30.2/24      up         up**        

**Vlanif40                          192.168.40.2/24      up         up**        

**Vlanif70                          192.168.70.2/24      up         up**        

**[LSW2]ospf 1**

**[LSW2-ospf-1]area 0.0.0.0**

**[LSW2-ospf-1-area-0.0.0.0]net 192.168.10.0 0.0.0.255**

**[LSW2-ospf-1-area-0.0.0.0]net 192.168.20.0 0.0.0.255**

**[LSW2-ospf-1-area-0.0.0.0]net 192.168.30.0 0.0.0.255**

**[LSW2-ospf-1-area-0.0.0.0]net 192.168.40.0 0.0.0.255**

**[LSW2-ospf-1-area-0.0.0.0]net 192.168.70.0 0.0.0.255**

**[LSW2-ospf-1-area-0.0.0.0]quit**

**[LSW2-ospf-1]quit**



### (5)ACL+NAT



**l** **AR１上ACL+NAT配置**

**Easy IP：**

**配置基本ACL并添加规则，允许VLAN10、VLAN30、VLAN50访问外网，VLAN20、40不能访问**

**[AR1]acl number 2000**

**[AR1-acl-basic-2000]rule 0 per source 192.168.10.0 0.0.0.255**

**[AR1-acl-basic-2000]rule 5 per source 192.168.30.0 0.0.0.255**

**[AR1-acl-basic-2000]rule 10 per source 192.168.50.0 0.0.0.255**

**[AR1-acl-basic-2000]quit**

**绑定规则到外网端口**

**[AR1]int g0/0/2**

**[AR1-GigabitEthernet0/0/2]nat outbound 2000**

**静态NAT，将服务器内网地址转为一个专门的公有IP**

**[AR1-GigabitEthernet0/0/2]nat static global 200.200.200.10 inside 192.168.50.253**

**[AR1-GigabitEthernet0/0/2]quit**



### (6)路由器OSPF协议的配置

**l** **AR１OSPF配置**

**配置接口IP**

**[AR1]int g0/0/0**

**[AR1-GigabitEthernet0/0/0]ip add 192.168.60.100 24**

**Sep 26 2019 09:54:53-08:00 AR1 %%01IFNET/4/LINK_STATE(l)[0]:The line protocol IP**

 **on the interface GigabitEthernet0/0/0 has entered the UP state.** 

**[AR1-GigabitEthernet0/0/0]int g0/0/1**

**[AR1-GigabitEthernet0/0/1]ip add 192.168.70.100 24**

**Sep 26 2019 09:55:16-08:00 AR1 %%01IFNET/4/LINK_STATE(l)[1]:The line protocol IP**

 **on the interface GigabitEthernet0/0/1 has entered the UP state.** 

**[AR1-GigabitEthernet0/0/1]int g0/0/2**

**[AR1-GigabitEthernet0/0/2]ip add 200.200.200.1 24**

**Sep 26 2019 09:56:09-08:00 AR1 %%01IFNET/4/LINK_STATE(l)[2]:The line protocol IP**

 **on the interface GigabitEthernet0/0/2 has entered the UP state.** 

**[AR1-GigabitEthernet0/0/2]quit**

**查看接口地址**

**[AR1]dis ip int br**

**Interface                         IP Address/Mask      Physical   Protocol**  

**GigabitEthernet0/0/0              192.168.60.100/24    up         up**        

**GigabitEthernet0/0/1              192.168.70.100/24    up         up**        

**GigabitEthernet0/0/2              200.200.200.1/24     up         up**        

**NULL0                             unassigned           up         up(s)**     

**宣告地址段**

**[AR1]ospf 1**

**[AR1-ospf-1]area 0.0.0.0**

**[AR1-ospf-1-area-0.0.0.0]net 192.168.60.0 0.0.0.255**

**[AR1-ospf-1-area-0.0.0.0]net 192.168.70.0 0.0.0.255**

**[AR1-ospf-1-area-0.0.0.0]net 200.200.200.0 0.0.0.255**

**[AR1-ospf-1-area-0.0.0.0]quit**

**[AR1-ospf-1]quit**

**配置到外网的默认路由，并加入到OSPF中**

**[AR1]ip route-static 0.0.0.0 0.0.0.0 200.200.200.100**

**[AR1]ospf 1**

**[AR1-ospf-1]default-route-advertise** 

**[AR1-ospf-1]quit**



### (7)路由器ＡＲ２的配置

**[AR2]int g0/0/0**

**[AR2-GigabitEthernet0/0/0]ip add 200.200.200.100 24**

**[AR2-GigabitEthernet0/0/0]int g0/0/1**

**[AR2-GigabitEthernet0/0/1]ip add 200.200.201.1 24**

**[AR2-GigabitEthernet0/0/1]quit**





## 结果测试



### 1、内网电脑之间进行通信：



![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic3.png) 

PC1能够ping通其他四个VLAN内的主机

### 2、内网主机动态获取IP地址：

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic2.png) 

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic4.png) 

PC配置DHCP能够自动获取IP

### 3、内网主机访问外网：

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic5.png) 

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic6.png) 

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL9/pic7.png) 

PC１、PC３和Server1能够ping通外网的主机，PC2和PC4ping通



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

