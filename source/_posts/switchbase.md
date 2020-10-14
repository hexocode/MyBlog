---
title: HCNA学习——交换机基础配置
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
tags:
	- HCNA
	- 交换机
categories:
	- 网络
	- HCNA
comments: true
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/cover/(00).jpg'
date: 2020-03-02 23:19:15
keywords: 
---

## 0、序言







今天就水一下，直接按照教材上的讲吧

**今日目标：**

1. 理解全双工、半双工，掌握更改接口速率的配置
2. 通过实验了解ARP和代理ARP，并掌握其配置







## 1、交换机基础配置












**交换机**(Switch)之间通过以太网电接口对接时需要协商一些接口参数，比如速率、双工模式等



单工、半双工、全双工

- **单工**数据传输只支持数据在一个方向上传输；在同一时间只有一方能接受或发送信息，不能实现双向通信，举例：电视，广播。
- **半双工**数据传输允许数据在两个方向上传输,但是,在某一时刻,只允许数据在一个方向上传输,它实际上是一种切换方向的单工通信；在同一时间只可以有一方接受或发送信息，可以实现双向通信。举例：对讲机。
- **全双工**数据通信允许数据同时在两个方向上传输,因此,全双工通信是两个单工通信方式的结合,它要求发送设备和接收设备都有独立的接收和发送能力；在同一时间可以同时接受和发送信息，实现双向通信，举例：电话通信。





如果交换机两端接口协商模式不一致(例如一端使用半双工、另一端为全双工)，就会导致报文交互异常



**接口速率**指交换机接口每秒钟传输数据的多少。



在交换机上可根据需要调整以太网接口速率

默认情况下，当以太网接口工作在非自动协商模式时，它的速率为接口支持的最大速率





(1)配置接口的双工模式



配置接口的双工模式可在自动协商或者非自动协商模式下进行



在自动协商模式下，接口的双工模式是和对端接口协商得到的，如果协商得到的双工模式不符合实际要求，可以通过配置双工模式的取值范围来控制协商的结果，默认情况下，以太网接口自协商双工模式范围是接口支持的双工模式

半双工：

auto duplex half

全双工：

auto duplex full



在非自动协商模式下，可以根据实际需求手动配置接口的双工模式

首先进入接口 eg: int g0/0/0

接着通过命令关掉自动协商功能： undo negotiation auto

指定接口为全双工或者半双工：duplex full 或 half



(2)配置接口速率



自动协商模式下 auto speed 100 或者10  #100Mbit/s或10Mbit/s



非自动协商模式下，需手动配置接口速率，避免发生无法正常通信的情况

默认情况下，以太网接口的速率为接口支持的最大速率

关闭接口自动协商模式：undo negotiation auto

根据需要配置GE或者Ethernet接口速率：speed 100 或 10





## 2、ARP及代理ARP







![img](https://mmbiz.qpic.cn/mmbiz_gif/9p7k9sjaO4WO0xvic9azzXTZpacThQn0kNIynIaF1c4srP28bQbs0icst3t6B6KbbtBC4V5PQUz83sL55VOfkRJA/640?tp=webp&wxfrom=5&wx_lazy=1)









[*上一篇文章*](http://mp.weixin.qq.com/s?__biz=MzI1OTc5NTA2OA==&mid=2247483897&idx=1&sn=3b152f2b2628693be2ecbeee693fa3a7&chksm=ea7230eadd05b9fc38053b7abfcf0a514279cc956c495a20decae0a68b80fcac4bb43ecf327c&scene=21#wechat_redirect)已经提到过，ARP是地址解析协议，可以把IP地址解析为MAC地址

> ARP表项可以分为动态和静态两种类型。
>
> 动态ARP是利用ARP广播报文，动态执行并自动进行IP地址到以太网MAC地址的解析，无需网络管理员手工处理。
>
> 静态ARP是建立IP地址和MAC地址之间固定的映射关系，在主机和路由器上不能动态调整此映射关系，需要网络管理员手工添加。



设备上有一个ARP高速缓存(ARP cache)，用来存放IP地址到MAC地址的映射表，利用ARP请求和应答报文来缓存映射表，以便能正确地把三层数据包封装成二层数据帧，达到快速封装数据帧、正确转发数据的目的。



代理ARP(Proxy ARP)，当主机上没有配置默认网关地址，可以发送一个广播ARP请求，使具备Proxy ARP功能的路由器收到这个请求后，在确认请求地址可达后，会使用自身的MAC地址作为该ARP请求的回应，是的处于不同物理网络的同一网段的主机之间可以正常通信



网络拓扑图如下：

![pic41](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic41.png)

现在先配置好下面的三台PC，地址、掩码按图中配置，网关不配置

例如，PC3

![pic42](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic42.png)

进入任一台PC机命令行，输入命令arp -a 查看主机的ARP表

![pic43](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic43.png)

可以看到ARP表项为空

我们开始配置路由器




```
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]sys R1
[R1]int g0/0/0
[R1-GigabitEthernet0/0/0]ip add 192.168.1.1 24
Mar  2 2020 22:32:54-08:00 R1 %%01IFNET/4/LINK_STATE(l)[0]:The line protocol IP 
on the interface GigabitEthernet0/0/0 has entered the UP state. 
[R1-GigabitEthernet0/0/0]int g0/0/1
[R1-GigabitEthernet0/0/1]ip add 192.168.2.1 24
Mar  2 2020 22:33:13-08:00 R1 %%01IFNET/4/LINK_STATE(l)[1]:The line protocol IP 
on the interface GigabitEthernet0/0/1 has entered the UP state. 
[R1-GigabitEthernet0/0/1]quit
```

上面我们已经把路由器命名为R1，配置好两个接口地址和掩码

现在我们使用命令 `display arp all` 查看R1的ARP表

![pic44](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcanpic44.png)

可以看到，表中只有R1两个接口IP地址及其对应的MAC地址表项，没有其他条目

现在需要用到一个功能了：数据抓包

点击图示位置，选择好设备和接口，开始抓包，这时将会打开wireshark

![pic45](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic45.png)

打开wireshark后会开始抓取数据包，我们只想看到arp的数据包，因此，在红框中输入arp后回车，开始过滤数据包

![pic46](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic46.png)



我们开始在PC上尝试ping R1的IP地址，检测连通性



下面就是ping过程抓的包

![pic47](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/test/hcnapic47.png)

不深入讲了

自己再到PC和R1上分别执行`arp -a `和 `display arp all` 查看结果吧，我就不贴图了





------



静态配置ARP



实施静态IP的好处是安全、操作简单，但是一旦设备多了，工作量太大，更换了网卡还需要自己手动更新arp映射

使用命令 arp static IP地址 MAC地址 就能成功添加一条ARP映射了



------



配置Proxy ARP



不同广播域(R1两边就是两个广播域)之间不经过其他配置不能进行通信(这里指没配置网关地址)，开启代理ARP能暂时解决，让两边的PC能够通信

开启ARP代理功能： 进入接口模式使用命令arp-proxy enable

但是这个不经常用，只是作为临时解决方案使用





![img](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaZEGn5b7odL7EkjBrdMksVEymqAcElYYPuYKiacsGdyceFl1Pe99nMgLBqsIqHcaEqz1apDmwnSJ3g/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)





今天文章就到这里了