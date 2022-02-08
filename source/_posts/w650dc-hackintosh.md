---
title: 毁灭者DC W650DC装黑苹果心得
tags:
    - w650dc
    - hackintosh
    - 黑苹果
categories:
    - 笔记
    - 黑苹果
top: 2
date: 2019-03-14 21:27:46
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
comments: true
keywords: Hackintosh
description: 
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---


## 00.先贴一下配置：
| 配置         |                  参数                        |
| ---------------------- | ----------------------- |
| 品名         | 炫龙毁灭者DC-G85S1N    |
| 电脑型号 |     No Enclosure CW65S04 笔记本电脑 |
| 操作系统 |    Windows 10 64位 ( DirectX 12 )  |
| 处理器     |   ~~英特尔Pentium(奔腾)G4400双核~~   |
|                  |  I3-8100  四核 |
| 主板         |         Notebook W650DC |
| 内存         |        8 GB |
| 主硬盘     |       三星MZNTY128HDHP-00000 ( 128 GB / 固态硬盘 ) |
| 独显         |          ~~ Nvidia GeForce GTX 950M ( 蓝天(CLEVO) ) ~~  |
| 核显         |       ~~英特尔HD Graphics 510~~   |
|                  |  英特尔HD Graphics 630 |
| 声卡         |        ACL269 |
| 网卡         |      ~~自带的忘了~~   |
|                  |    DW1820A/BCM94350ZAE   |

---

## 01.折腾经历

刚开始cpu是奔腾的，网上看到一篇帖子：

![G4400仿冒ID](https://img-blog.csdnimg.cn/20190314205443964.png)
[G4400+H110M黑苹果成功](http://bbs.zol.com.cn/diybbs/d231_872661.html)

我在虚拟机装好了Mac，改好了config.plist

(就这里我踩了个坑：使用的Clover Configurator版本不对，打死都进不去安装界面，一直卡在update那，这还是我换U装好黑苹果后才发现的)

咨询了下某些大佬，他们说就算装了显卡也没得玩，so直接买了块i3 8100，刷了下BIOS，换上U，引导直接成功安装10.12.6

把引导文件放到EFI分区之后，发现有些地方一直闪屏，根据黑果小兵的教程改好了显存(改到了3072MB)还是会闪，有的网友说SMBIOS只留型号那一栏为18,1可以解决，然并卵。然后我直接把整个EFI换了clover4596，保留了改好了之后的config.plist，开机，很好不闪了，然后干脆直接装了带Clover4596的10.13.6  

对了，教程的话参考这个吧：[【爱折腾】RE：从零开始安装黑苹果](https://www.bilibili.com/video/av8653761)，顺带看下其他帖子

## 02.黑苹果状态

=处理器         变频正常

=显卡             独显没办法，HD510也没办法。UHD630没毛病了，能驱动，能调亮度。睡眠有问题，长时间会睡死，Mojave好像升级到最新版Clover4020好像不会睡死

=声卡             声卡正常 注入29

=网卡             随便搜下“网卡 黑苹果”然后购买安装驱动就行了

=型号             可使用下面的：  

|     型号       |         platform      |
| ---------------------- | ----------------------- |
|        iMac17,1       |     也就是下面给出的EFI里的   |
|  MacBook Pro14,3   |     0x591b0000  |
|  iMac18,2或18,3      |     0x59120000   |
|  MacBook Pro15,1   |    0x3e9b0000    |
|  Macmini8,1               |    0x3e9b0007    |


 `不过好像HD630的换以上所有机型都能用0x591b0000`

 10.13.6基本都没问题了

 10.14.3的声卡有问题，要自己将Lilu.kext及AppleALC.kext替换为最新版

***

 ## 03.EFI分享

 G4400(还是建议换成下面两种U):https://pan.baidu.com/s/1q0-QVWzNhDWPpS4GRzU9NQ 
 提取码：4y22 

 i3-8100:https://pan.baidu.com/s/1l_9oTLSyIpO-u6ezZrcUxw 
 提取码：7c0a 

 i5-6400:https://pan.baidu.com/s/11siLSXgcLmLRi_3EOp1t4w 
 提取码：757s 

 

 =================================2019.6.30更新================================

 

## 04.网卡驱动更换


 由于USB网卡占用一个USB接口，蓝牙是内置网卡提供的，总是会掉，而且隔空投送功能不能实现，因此萌生了更换网卡的想法。

 黑苹果NGFF M.2内置无线网卡主要有：

 >-DW1820A/BCM94350ZAE

 >-DW1560/BCM94352Z

 >-DW1830/BCM943602BAED

 后面两种因为很好驱动，市场价越来越高，穷苦人家实在买不起，然后就盯着第一款，发现有一家店卖￥49，因此就直接入手了。
 ![DW1820A价格](https://img-blog.csdnimg.cn/20190630104200606.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTQ5MTAz,size_16,color_FFFFFF,t_70)
 >注：

 >1、此网卡大部分电脑应该都支持，17年前的HP、联想慎入。

 >2、黑苹果直接先把三个驱动放到Clover/kext下，然后替换掉以前的网卡就行了，隔空投送终于能用了
 ![黑苹果驱动](https://img-blog.csdnimg.cn/20190630104303392.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTQ5MTAz,size_16,color_FFFFFF,t_70)

 >3、Win下需要安装WLAN和蓝牙驱动，有以下解决方案：  
 ①直接下载驱动安装  
 ②用手机USB网络共享，之后用驱动精灵安装  
 ③插网线，再用驱动精灵下载驱动  
 ④外置USB网卡，驱动精灵  
 ![win驱动](https://img-blog.csdnimg.cn/20190630104842234.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTQ5MTAz,size_16,color_FFFFFF,t_70)

 >4、WIFI_5G  
 网卡是支持5G的，WIN下不用修改，Mac可以参考这个：
 [[网卡] BCM94350ZAE(dw1820A)驱动教程，基本完美](http://bbs.pcbeta.com/viewthread-1817645-1-1.html)


 >  **驱动分享**  
 链接:https://pan.baidu.com/s/1jMlFTShoqn068pIgmpgreQ  密码:w073

 

 

 ===============================2019.7.4更新===================================


## 05.补充

 试了下10.5感觉不好用，就干脆直接回到了最稳定的10.13.6

 再补充下以前没说的吧

 ### (1)开HiDPI

 [HiDPI是什么？以及黑苹果如何开启HiDPI](https://www.sqlsec.com/2018/09/hidpi.html)

 ### (2)iTerm2配置

 [Mac OS 终端利器 iTerm2配置大全](https://www.cnblogs.com/diyxiaoshitou/p/9017413.html)

 ### (3)安装任何来源命令  

 `sudo spctl --master-disable` 

 ### (4)Dock栏插入空格  
 ```
 defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'
 ```  
 再输入下面的命令

 `killall Dock`  
 ![程序坞](https://img-blog.csdnimg.cn/20190704220349999.png)

 不过以上命令只是对 Dock 栏的左半部分有效,如果你想在右半部分（应用、文稿、下载、废纸篓）也添加空格的话,可以用下面的这个命令：
 ```
 defaults write com.apple.dock persistent-others -array-add '{tile-data={}; tile-type="spacer-tile";}' ;killall Dock
 ```  
 不想要了直接拖出去就行


 ###  (5)开机第二段八苹果花屏解决方案

 使用EDID Edit获取EDID到Clover中注入
 ![注入EDID](https://img-blog.csdnimg.cn/20190706162642419.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTQ5MTAz,size_16,color_FFFFFF,t_70)


 ### (6)一些下载地址(更新ing)
 Config.plist https://github.com/RehabMan/OS-X-Clover-Laptop-Config/blob/master/hotpatch/config.plist

 Clover https://github.com/Dids/clover-builder/releases

 Clover Configaration（CCG） https://mackie100projects.altervista.org/clover-configurator/
 ![CCG](https://img-blog.csdnimg.cn/20190704221926207.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTQ5MTAz,size_16,color_FFFFFF,t_70)

 ### (7)推荐下载

![推荐下载](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/20200808085257.png)

 

 


 ===============================2019.7.26更新==================================

## 06.升级MacOS10.15Catalina

 哈哈，说好回到最稳定的10.13.6，可本着冒险精神的我，又上10.15了，而且还找到了一个完美的EFI，哇哈哈。

 闲着无聊，然后就使用镜像升级到了10.14.5，然后直接通过系统升级到10.15 Beta 版(19A512f)。能开机，重要的问题就两个，声卡不能驱动、蓝牙无法使用。

 声卡的好解决，直接升级AppleACL、LiLu驱动到最新版，layout-id仍使用29即可。

 蓝牙的真的不会，现在也还是不会，不过在远景找到了一篇帖子，然后尝试使用了[@CeWnHai](http://i.pcbeta.com/space-uid-4841127.html)的EFI，直接完美，根本不需要怎么修改。感觉最棒的就是已修复输入密码的延迟（通过NoTouchID.kext)，输密码卡半天真的令人不爽，居然就这样解决了，开心啊。

 [炫龙DC Pro 蓝天W650kj i3-8100 10.14.6完美99%](http://bbs.pcbeta.com/viewthread-1803477-1-1.html)

***
 再说下现在的配置吧

 | 配置 | 参数 |
 |:----------:|:----------:|
 |     操作系统       |     macOS Catalina 10.15 Beta版       |
 |        处理器        |        I3-8100    |
 |          主板          |       蓝天W650DC     |
 |          内存          |        8 GB+8 GB    |
 |          核显          |      英特尔HD Graphics 630   |
 |          声卡          |       ACL269VC     |
 |          网卡          |        DW1820A/BCM94350ZAE   |       

 大部分都能驱动(声卡、显卡、网卡都能用)，USB使用正常，睡眠没试，CPU变频OK。 

 至于最新的EFI，毕竟是直接拿的别人的，我就不共享了。

 


 ===============================2019.8.5更新===================================


## 07.蓝牙解决方案
 还是[@CeWnHai](http://i.pcbeta.com/space-uid-4841127.html)这位大佬的方案，就上面的那个基本完美的EFI分享者。

 简而言之就是在VirtualSMC加入蓝牙的id即可。具体参考：

 [关于DW1820A蓝牙连接问题解决方法，其它应该也可以。](http://bbs.pcbeta.com/viewthread-1802647-1-1.html)

 

 ===============================2019.8.27更新==================================

 以后文章优先在[使用hexo部署在github page搭建的博客](http://wallleap.top)更新


 ===============================2020.5.28更新==================================

## 08.更换OC引导

使用的是[OpenCore引导神舟k670d蓝天W650kj完美](http://bbs.pcbeta.com/viewthread-1842304-7-1.html)这个帖子里的

需要先刷D大的BOOT，之后按照帖子[蓝天解锁CFG锁教程](http://bbs.pcbeta.com/viewthread-1842372-1-1.html)操作。

接着就可以把EFI换成OC的了

 ===============================2020.5.28更新==================================

## 09.尝试上车Big sur

上车失败，硬盘空间不够，想安装到移动硬盘，还是不行

