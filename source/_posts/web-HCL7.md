---
title: OSPF配置
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.top
authorAbout: 确定了目标就努力奋斗吧
authorDesc: 一个好奇的人
comments: true
tags:
  - eNSP
  - OSPF
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner6.jpg'
date: 2019-09-27 07:58:04
categories: 
  - 网络
keywords: OSPF配置
description:
---


## ■实验目的

与上一个实验差不多，将RIP换成OSPF即可

拓扑如下：
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL7/pic1.png)





## ■配置





### ▲S4：

> 去除提示信息，修改交换机名称

```
<Huawei>sys 
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS4
```

> 创建VLAN

```
[LWS4]vlan 10
[LWS4-vlan10]vlan 20
[LWS4-vlan20]quit
```

> 配置接口

```
[LWS4]int e0/0/3
[LWS4-Ethernet0/0/3]un sh
Info: Interface Ethernet0/0/3 is not shutdown.
[LWS4-Ethernet0/0/3]port link-t a
[LWS4-Ethernet0/0/3]port de vlan 10
[LWS4-Ethernet0/0/3]int e0/0/4
[LWS4-Ethernet0/0/4]un sh
Info: Interface Ethernet0/0/4 is not shutdown.
[LWS4-Ethernet0/0/4]port link-t a
[LWS4-Ethernet0/0/4]port de vlan 20
[LWS4-Ethernet0/0/4]int e0/0/1
[LWS4-Ethernet0/0/1]un sh
Info: Interface Ethernet0/0/1 is not shutdown.
[LWS4-Ethernet0/0/1]port link-t t
[LWS4-Ethernet0/0/1]port t allow vlan all
[LWS4-Ethernet0/0/1]int e0/0/2
[LWS4-Ethernet0/0/2]un sh
Info: Interface Ethernet0/0/2 is not shutdown.
[LWS4-Ethernet0/0/2]port link-t t
[LWS4-Ethernet0/0/2]port t allow vlan all
[LWS4-Ethernet0/0/2]quit
```

> 启动stp并保存配置

```
[LWS4]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
[LWS4]quit
<LWS4>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```

### ▲S5：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS5
[LWS5]vlan 30
[LWS5-vlan30]vlan 40
[LWS5-vlan40]quit
[LWS5]int e0/0/3
[LWS5-Ethernet0/0/3]un shu
Info: Interface Ethernet0/0/3 is not shutdown.
[LWS5-Ethernet0/0/3]port link-t a
[LWS5-Ethernet0/0/3]port de vlan 30
[LWS5-Ethernet0/0/3]int e0/0/4
[LWS5-Ethernet0/0/4]un sh
Info: Interface Ethernet0/0/4 is not shutdown.
[LWS5-Ethernet0/0/4]port link-t a
[LWS5-Ethernet0/0/4]port de vlan 40
[LWS5-Ethernet0/0/4]int e0/0/1
[LWS5-Ethernet0/0/1]un sh
Info: Interface Ethernet0/0/1 is not shutdown.
[LWS5-Ethernet0/0/1]port link-t t
[LWS5-Ethernet0/0/1]port t allow vlan all
[LWS5-Ethernet0/0/1]int e0/0/2
[LWS5-Ethernet0/0/2]un sh
Info: Interface Ethernet0/0/2 is not shutdown.
[LWS5-Ethernet0/0/2]port link-t t
[LWS5-Ethernet0/0/2]port t allow vlan all
[LWS5-Ethernet0/0/2]quit
[LWS5]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
[LWS5]quit
<LWS5>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.

```
### ▲S6：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS6
[LWS6]vlan 50
[LWS6-vlan50]vlan 60
[LWS6-vlan60]quit
[LWS6]int e0/0/2
[LWS6-Ethernet0/0/2]un sh
Info: Interface Ethernet0/0/2 is not shutdown.
[LWS6-Ethernet0/0/2]port link-t a
[LWS6-Ethernet0/0/2]port de vlan 50
[LWS6-Ethernet0/0/2]int e0/0/3
[LWS6-Ethernet0/0/3]un sh
Info: Interface Ethernet0/0/3 is not shutdown.
[LWS6-Ethernet0/0/3]port link-t a
[LWS6-Ethernet0/0/3]port de vlan 60
[LWS6-Ethernet0/0/3]int e0/0/1
[LWS6-Ethernet0/0/1]un sh
Info: Interface Ethernet0/0/1 is not shutdown.
[LWS6-Ethernet0/0/1]port link-t t
[LWS6-Ethernet0/0/1]port t allow vlan all
[LWS6-Ethernet0/0/1]quit
[LWS6]quit
<LWS6>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```



### ▲S1：

> 创建VLAN

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
[LWS1-vlan40]vlan 70
[LWS1-vlan70]quit
```

> 配置接口

```
[LWS1]int g0/0/1
[LWS1-GigabitEthernet0/0/1]un sh
Info: Interface GigabitEthernet0/0/1 is not shutdown.
[LWS1-GigabitEthernet0/0/1]port link-t a
[LWS1-GigabitEthernet0/0/1]port de vlan 70
[LWS1-GigabitEthernet0/0/1]quit
[LWS1]int g0/0/2
[LWS1-GigabitEthernet0/0/2]un sh
Info: Interface GigabitEthernet0/0/2 is not shutdown.
[LWS1-GigabitEthernet0/0/2]port link-t t
[LWS1-GigabitEthernet0/0/2]port t allow vlan all
[LWS1-GigabitEthernet0/0/2]int g0/0/3
[LWS1-GigabitEthernet0/0/3]un sh
Info: Interface GigabitEthernet0/0/3 is not shutdown.
[LWS1-GigabitEthernet0/0/3]port link-t t
[LWS1-GigabitEthernet0/0/3]port t allow vlan all
[LWS1-GigabitEthernet0/0/3]int g0/0/4
[LWS1-GigabitEthernet0/0/4]un sh
Info: Interface GigabitEthernet0/0/4 is not shutdown.
[LWS1-GigabitEthernet0/0/4]port link-t t
[LWS1-GigabitEthernet0/0/4]port t allow vlan all
[LWS1-GigabitEthernet0/0/4]quit
```

> 开启stp并设置为根桥(优先级为0)

```
[LWS1]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
[LWS1]stp prio 0
```

> 配置VLAN地址(真实网关)并设置VRRP配置虚拟网关，将S1设置为VLAN10、20的主路由器，当上行接口断了时变为备用路由器

```
[LWS1]int vlan 10
[LWS1-Vlanif10]ip add 192.168.10.253 255.255.255.0
[LWS1-Vlanif10]vrrp vrid 10 virtual-ip 192.168.10.1
[LWS1-Vlanif10]vrrp vrid 10 prio  120
[LWS1-Vlanif10]vrrp vrid 10 track int g0/0/1 reduce 30
[LWS1-Vlanif10]int vlan 20
[LWS1-Vlanif20]ip add 192.168.20.253 255.255.255.0
[LWS1-Vlanif20]vrrp vrid 20 vi 192.168.20.1
[LWS1-Vlanif20]vrrp vrid 20 prio 120
[LWS1-Vlanif20]vrrp vrid 20 track int g0/0/1 reduce 30
[LWS1-Vlanif20]int vlan 30
[LWS1-Vlanif30]ip add 192.168.30.253 255.255.255.0
[LWS1-Vlanif30]vrrp vrid 30 vi 192.168.30.1
[LWS1-Vlanif30]int vlan 40
[LWS1-Vlanif40]ip add 192.168.40.253 255.255.255.0
[LWS1-Vlanif40]vrrp vrid 40 vi 192.168.40.1
[LWS1]int vlan 70
[LWS1-Vlanif70]ip add 192.168.70.253 24
[LWS1-Vlanif70]quit
[LWS1]quit
```

> 保存配置

```
<LWS1>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0..
Save the configuration successfully.
```

> OSPF

可以先用`dis ip int br`查看所有IP，再宣告网段

```
[LWS1]ospf 1
[LWS1-ospf-1]area 0.0.0.0
[LWS1-ospf-1-area-0.0.0.0]net 192.168.10.0 0.0.0.255
[LWS1-ospf-1-area-0.0.0.0]net 192.168.20.0 0.0.0.255
[LWS1-ospf-1-area-0.0.0.0]net 192.168.30.0 0.0.0.255
[LWS1-ospf-1-area-0.0.0.0]net 192.168.40.0 0.0.0.255
[LWS1-ospf-1-area-0.0.0.0]net 192.168.70.0 0.0.0.255
[LWS1-ospf-1-area-0.0.0.0]quit
[LWS1-ospf-1]quit
[LWS1]quit
<LWS1>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```



### ▲S2：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS2
[LWS2]vlan 10
[LWS2-vlan10]vlan 20
[LWS2-vlan20]vlan 30
[LWS2-vlan30]vlan 40
[LWS2-vlan40]vlan 80
[LWS2-vlan80]quit
[LWS2]int g0/0/1
[LWS2-GigabitEthernet0/0/1]un sh
Info: Interface GigabitEthernet0/0/1 is not shutdown.
[LWS2-GigabitEthernet0/0/1]port link-t a
[LWS2-GigabitEthernet0/0/1]port de vlan 80
[LWS2-GigabitEthernet0/0/1]int g0/0/2
[LWS2-GigabitEthernet0/0/2]un sh
Info: Interface GigabitEthernet0/0/2 is not shutdown.
[LWS2-GigabitEthernet0/0/2]port link-t t
[LWS2-GigabitEthernet0/0/2]port t allow vlan all
[LWS2-GigabitEthernet0/0/2]int g0/0/3
[LWS2-GigabitEthernet0/0/3]un sh
Info: Interface GigabitEthernet0/0/3 is not shutdown.
[LWS2-GigabitEthernet0/0/3]port link-t t
[LWS2-GigabitEthernet0/0/3]port t allow vlan all
[LWS2-GigabitEthernet0/0/3]int g0/0/4
[LWS2-GigabitEthernet0/0/4]un sh
Info: Interface GigabitEthernet0/0/4 is not shutdown.
[LWS2-GigabitEthernet0/0/4]port link-t t
[LWS2-GigabitEthernet0/0/4]port t allow vlan all
[LWS2-GigabitEthernet0/0/4]quit
[LWS2]int vlan 10
[LWS2-Vlanif10]ip add 192.168.10.254 24
[LWS2-Vlanif10]vrrp vrid 10 vi 192.168.10.1
[LWS2-Vlanif10]int vlan 20
[LWS2-Vlanif20]ip add 192.168.20.254 24
[LWS2-Vlanif20]vrrp vrid 20 vi 192.168.20.1
[LWS2-Vlanif20]int vlan 30
[LWS2-Vlanif30]ip add 192.168.30.254 24
[LWS2-Vlanif30]vrrp vrid 30 vi 192.168.30.1
[LWS2-Vlanif30]vrrp vrid 30 prio 120
[LWS2-Vlanif30]vrrp vrid 30 track int g0/0/1 reduce 30
[LWS2-Vlanif30]int vlan 40
[LWS2-Vlanif40]ip add 192.168.40.254 24
[LWS2-Vlanif40]vrrp vrid 40 vi 192.168.40.1
[LWS2-Vlanif40]vrrp vrid 40 prio 120
[LWS2-Vlanif40]vrrp vrid 40 track int g0/0/1 reduce 30
[LWS2-Vlanif40]int vlan 80
[LWS2-Vlanif80]ip add 192.168.80.254 24
[LWS2-Vlanif80]quit
[LWS2]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
[LWS2]stp prio 4096
[LWS2]quit
<LWS2>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.


[LWS2]ospf 1
[LWS2-ospf-1]area 0.0.0.0
[LWS2-ospf-1-area-0.0.0.0]net 192.168.10.0 0.0.0.255
[LWS2-ospf-1-area-0.0.0.0]net 192.168.20.0 0.0.0.255
[LWS2-ospf-1-area-0.0.0.0]net 192.168.30.0 0.0.0.255
[LWS2-ospf-1-area-0.0.0.0]net 192.168.40.0 0.0.0.255
[LWS2-ospf-1-area-0.0.0.0]net 192.168.80.0 0.0.0.255
[LWS2-ospf-1-area-0.0.0.0]quit
[LWS2-ospf-1]quit
[LWS2]quit
<LWS2>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```








### ▲S3：

```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWS3
[LWS3]vlan 50
[LWS3-vlan50]vlan 60
[LWS3-vlan60]vlan 90
[LWS3-vlan90]quit
[LWS3]int g0/0/2
[LWS3-GigabitEthernet0/0/2]un sh
Info: Interface GigabitEthernet0/0/2 is not shutdown.
[LWS3-GigabitEthernet0/0/2]port link-t t
[LWS3-GigabitEthernet0/0/2]port t allow vlan all
[LWS3-GigabitEthernet0/0/2]int g0/0/1
[LWS3-GigabitEthernet0/0/1]un sh
Info: Interface GigabitEthernet0/0/1 is not shutdown.
[LWS3-GigabitEthernet0/0/1]port link-t a
[LWS3-GigabitEthernet0/0/1]port de vlan 90
[LWS3-GigabitEthernet0/0/1]quit
[LWS3]int vlan 50
[LWS3-Vlanif50]ip add 192.168.50.1 24
[LWS3-Vlanif50]int vlan 60
[LWS3-Vlanif60]ip add 192.168.60.1 24
[LWS3-Vlanif60]int vlan 90
[LWS3-Vlanif90]ip add 192.168.90.1 24
[LWS3-Vlanif90]quit
[LWS3]dhcp en
Info: The operation may take a few seconds. Please wait for a moment.done.
[LWS3]ip pool vlan50
Info:It's successful to create an IP address pool.
[LWS3-ip-pool-vlan50]gateway-list 192.168.50.1
[LWS3-ip-pool-vlan50]net 192.168.50.0 mask 255.255.255.0
[LWS3-ip-pool-vlan50]quit
[LWS3]ip pool vlan60
Info:It's successful to create an IP address pool.
[LWS3-ip-pool-vlan60]gateway-list 192.168.60.1
[LWS3-ip-pool-vlan60]net 192.168.60.0 mask 255.255.255.0
[LWS3-ip-pool-vlan60]quit
[LWS3]quit
[LWS3]int vlan50
[LWS3-Vlanif50]dhcp select global
[LWS3-Vlanif50]int vlan60
[LWS3-Vlanif60]dhcp select global
[LWS3-Vlanif60]quit
[LWS3]quit
<LWS3>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.




[LWS3]ospf 1
[LWS3-ospf-1]area 0.0.0.0
[LWS3-ospf-1-area-0.0.0.0]net 192.168.90.0 0.0.0.255
[LWS3-ospf-1-area-0.0.0.0]net 192.168.50.0 0.0.0.255
[LWS3-ospf-1-area-0.0.0.0]net 192.168.60.0 0.0.0.255
[LWS3-ospf-1-area-0.0.0.0]quit
[LWS3-ospf-1]quit
[LWS3]quit
<LWS3>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```


### ●R1：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWR1
[LWR1]int e0/0/1
[LWR1-Ethernet0/0/1]un sh
Info: Interface Ethernet0/0/1 is not shutdown.
[LWR1-Ethernet0/0/1]ip add 192.168.70.50 24
[LWR1-Ethernet0/0/1]int g0/0/0
[LWR1-GigabitEthernet0/0/0]ip add 192.168.80.50 24
[LWR1-GigabitEthernet0/0/0]int e0/0/0
[LWR1-Ethernet0/0/0]ip add 192.168.100.50 24
[LWR1-Ethernet0/0/0]quit
[LWR1]quit
<LWR1>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 17.
Save the configuration successfully.
<LWR1>sys
Enter system view, return user view with Ctrl+Z.


[LWR1]ospf 1
[LWR1-ospf-1]area 0.0.0.0
[LWR1-ospf-1-area-0.0.0.0]net 192.168.70.0 0.0.0.255
[LWR1-ospf-1-area-0.0.0.0]net 192.168.80.0 0.0.0.255
[LWR1-ospf-1-area-0.0.0.0]net 192.168.100.0 0.0.0.255
[LWR1-ospf-1-area-0.0.0.0]quit
[LWR1-ospf-1]quit
[LWR1]quit
<LWR1>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Now saving the current configuration to the slot 17.
Save the configuration successfully.
```

### ●R2：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWR2
[LWR2]int e0/0/0
[LWR2-Ethernet0/0/0]un sh
Info: Interface Ethernet0/0/0 is not shutdown.
[LWR2-Ethernet0/0/0]ip add 192.168.100.51 24
[LWR2-Ethernet0/0/0]int e0/0/1
[LWR2-Ethernet0/0/1]ip add 192.168.110.51 24
[LWR2-Ethernet0/0/1]quit


[LWR2]ospf 1
[LWR2-ospf-1]area 0.0.0.0
[LWR2-ospf-1-area-0.0.0.0]net 192.168.100.0 0.0.0.255
[LWR2-ospf-1-area-0.0.0.0]net 192.168.110.0 0.0.0.255
[LWR2-ospf-1-area-0.0.0.0]quit
[LWR2-ospf-1]qu
[LWR2]qu
<LWR2>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 17.
Save the configuration successfully.
```
### ●R3：
```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]un in en
Info: Information center is disabled.
[Huawei]sys LWR3
[LWR3]int e0/0/0
[LWR3-Ethernet0/0/0]ip add 192.168.110.50 24
[LWR3-Ethernet0/0/0]int e0/0/1
[LWR3-Ethernet0/0/1]ip add 192.168.90.50 24
[LWR3-Ethernet0/0/1]quit
[LWR3]ospf 1
[LWR3-ospf-1]area 0.0.0.0
[LWR3-ospf-1-area-0.0.0.0]net 192.168.90.0 0.0.0.255
[LWR3-ospf-1-area-0.0.0.0]net 192.168.110.0 0.0.0.255
[LWR3-ospf-1-area-0.0.0.0]quit
[LWR3-ospf-1]quit
[LWR3]quit
<LWR3>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 17.
Save the configuration successfully.
```


## ■测试
Ping
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL7/pic2.png)
S1或S2
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL7/pic3.png)
S4或S5
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/web-HCL7/pic4.png)







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



