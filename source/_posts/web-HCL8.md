---
title: ACL+NAT配置
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.top
authorAbout: 一个好奇的人
authorDesc: 一个好奇的人
comments: true
tags:
  - eNSP
  - ACL
  - NAT
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner7.jpg'
date: 2019-09-27 07:58:17
categories:
  - 网络
keywords: NAT配置
description:
---

## 实验目的

让VLAN10、30内的主机能够访问外网，Server1拥有一个公网IP，以便外网主机能够直接访问Server1

拓扑：

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/pic1.png)

## 配置

### PC

开启DHCP，点应用
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/pic2.png)



### Server1

配置静态私网IP，方便转换公网
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/pic3.png)

### S2：

```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LSW2
[LSW2]vlan 10
[LSW2-vlan10]vlan 20
[LSW2-vlan20]quit
[LSW2]int e0/0/1
[LSW2-Ethernet0/0/1]port link-t t
[LSW2-Ethernet0/0/1]port t allow vlan all
[LSW2-Ethernet0/0/1]int e0/0/2
[LSW2-Ethernet0/0/2]port link-t a
[LSW2-Ethernet0/0/2]port de vlan 10
[LSW2-Ethernet0/0/2]int e0/0/3
[LSW2-Ethernet0/0/3]port link-t a
[LSW2-Ethernet0/0/3]port de vlan 20
[LSW2-Ethernet0/0/3]quit
[LSW2]qu
<LSW2>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```

### S3：

```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS3
[LWS3]vlan 30
[LWS3-vlan30]vlan 40
[LWS3-vlan40]quit
[LWS3]int e0/0/2
[LWS3-Ethernet0/0/2]port link-t a
[LWS3-Ethernet0/0/2]port de vlan 30
[LWS3-Ethernet0/0/2]int e0/0/3
[LWS3-Ethernet0/0/3]port link-t a
[LWS3-Ethernet0/0/3]port de vlan 40
[LWS3-Ethernet0/0/3]int e0/0/1
[LWS3-Ethernet0/0/1]port link-t t
[LWS3-Ethernet0/0/1]port t allow vlan all
[LWS3-Ethernet0/0/1]quit
[LWS3]quit
<LWS3>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```


### S1

```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS1
[LWS1]vlan 10
[LWS1-vlan10]vlan 20
[LWS1-vlan20]vlan 30
[LWS1-vlan30]vlan 40
[LWS1-vlan40]vlan 50
[LWS1-vlan50]vlan 60
[LWS1-vlan60]quit
[LWS1]int g0/0/2
[LWS1-GigabitEthernet0/0/2]port link-t 
[LWS1-port-group-link-t]quit
[LWS1]int g0/0/2
[LWS1-GigabitEthernet0/0/2]port link-t t
[LWS1-GigabitEthernet0/0/2]port t allow vlan all
[LWS1-GigabitEthernet0/0/2]int g0/0/3
[LWS1-GigabitEthernet0/0/3]port link-t t
[LWS1-GigabitEthernet0/0/3]port t allow vlan all
[LWS1-GigabitEthernet0/0/3]int g0/0/4
[LWS1-GigabitEthernet0/0/4]port link-t a
 [LWS1-GigabitEthernet0/0/4]port de vlan 50
[LWS1-GigabitEthernet0/0/4]int g0/0/1
[LWS1-GigabitEthernet0/0/1]port link-t a
 [LWS1-GigabitEthernet0/0/1]port de vlan 60
[LWS1-GigabitEthernet0/0/1]quit
[LWS1]dhcp en
Info: The operation may take a few seconds. Please wait for a moment.done.
[LWS1]ip pool vlan10
Info:It's successful to create an IP address pool.
[LWS1-ip-pool-vlan10]gateway-list 192.168.10.1
[LWS1-ip-pool-vlan10]net 192.168.10.0 mask 255.255.255.0
[LWS1-ip-pool-vlan10]qu
[LWS1]ip pool vlan20
Info:It's successful to create an IP address pool.
[LWS1-ip-pool-vlan20]gateway-list 192.168.20.1
[LWS1-ip-pool-vlan20]net 192.168.20.0 mask 255.255.255.0
[LWS1-ip-pool-vlan20]qu
[LWS1]ip pool vlan30
Info:It's successful to create an IP address pool.
[LWS1-ip-pool-vlan30]gateway-list 192.168.30.1
[LWS1-ip-pool-vlan30]net 192.168.30.0 mask 255.255.255.0
[LWS1-ip-pool-vlan30]qu
[LWS1]ip pool vlan40
Info:It's successful to create an IP address pool.
[LWS1-ip-pool-vlan40]gateway-list 192.168.40.1
[LWS1-ip-pool-vlan40]net 192.168.40.0 mask 255.255.255.0
[LWS1-ip-pool-vlan40]quit
[LWS1]int vlan 10
[LWS1-Vlanif10]ip add 192.168.10.1 24
[LWS1-Vlanif10]dhcp select global
[LWS1-Vlanif10]int vlan 20
[LWS1-Vlanif20]ip add 192.168.20.1 24
[LWS1-Vlanif20]dhcp select global
[LWS1-Vlanif20]int vlan 30
[LWS1-Vlanif30]ip add 192.168.30.1 24
[LWS1-Vlanif30]dhcp select global
[LWS1-Vlanif30]int vlan 40
[LWS1-Vlanif40]ip add 192.168.40.1 24
[LWS1-Vlanif40]dhcp select global
[LWS1-Vlanif40]quit
[LWS1]int vlan 50
[LWS1-Vlanif50]ip add 192.168.50.1 24
[LWS1-Vlanif50]in vlan 60
[LWS1-Vlanif60]ip add 192.168.60.1 24
[LWS1-Vlanif60]quit
[LWS1]qu
<LWS1>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
[LWS1]ip route-static 0.0.0.0 0.0.0.0 192.168.60.100
```



### R2：

```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWR2
[LWR2]int g0/0/0
[LWR2-GigabitEthernet0/0/0]ip add 200.200.200.100 24
 [LWR2-GigabitEthernet0/0/0]int g0/0/1
[LWR2-GigabitEthernet0/0/1]ip add 200.200.201.1 24
[LWR2-GigabitEthernet0/0/1]quit
[LWR2]quit
<LWR2>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait.......
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated

R1：
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWR1
[LWR1]int g0/0/0
[LWR1-GigabitEthernet0/0/0]un sh
Info: Interface GigabitEthernet0/0/0 is not shutdown.
[LWR1-GigabitEthernet0/0/0]ip add 192.168.60.100 24
[LWR1-GigabitEthernet0/0/0]int g0/0/1
[LWR1-GigabitEthernet0/0/1]ip add 200.200.200.1 24
[LWR1-GigabitEthernet0/0/1]quit
[LWR1]ip route-static 192.168.0.0 255.255.0.0 192.168.60.1
[LWR1]ip route-static 200.200.0.0 255.255.0.0 200.200.200.100
[LWR1]acl number 2000
[LWR1-acl-basic-2000]rule 0 per source 192.168.10.0 0.0.0.255 
[LWR1-acl-basic-2000]rule 5 per source 192.168.30.0 0.0.0.255
[LWR1-acl-basic-2000]rule 10 per source 192.168.50.0 0.0.0.255
[LWR1-acl-basic-2000]quit
[LWR1]int g0/0/1
[LWR1-GigabitEthernet0/0/1]nat outbound 2000
[LWR1-GigabitEthernet0/0/1]nat static global 200.200.200.10 inside 192.168.50.254
[LWR1-GigabitEthernet0/0/1]quit
[LWR1]quit
<LWR1>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait..........
....
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated
```
测试
PC1、PC2、服务器分别pingPC5
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/PC1.png)
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/PC2.png)
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL8/Server.png)









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

