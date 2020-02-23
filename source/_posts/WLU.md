---
title: Win10启用其子系统Ubuntu并安装图形界面
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.top
authorAbout: 
authorDesc: 不忘初心 继续前进
categories:
  - 电脑
comments: true
tags:
  - Win10
  - Ubuntu
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner20.jpg'
date: 2019-11-07 10:21:17
keywords:
description:
---

# Win10启用其子系统Ubuntu并安装图形界面

# 0.说明

好像只有16215版本之后的才可以



鉴于双显卡安装时会卡logo，需要自己修改命令，MacOS+win10+Ubuntu总是会进入紧急模式，而且虚拟机体验非常不好，所以直接启用Win10的子系统，使用起来还是很方便的

## 1.启用 “适用于 Linux 的 Windows 子系统”可选功能 

方法一: 设置-更新和安全-开发者选项-勾选开发人员模式，接着打开控制面板-程序-启用或关闭Windows功能-勾选“适用于Linux的Windows子系统”前的复选框

方法二：搜索Poweshell，选择`以管理员身份运行`![1572956839709](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/wlu/1572956839709.png)

输入命令

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

接着输入`Y`回车，重启

## 2.下载Linux发布版

打开Win10自带的Microsoft Store，选择自己需要的版本下载

![1572957066606](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/wlu/1572957066606.png)

单击以下链接会打开每个分发版的 Microsoft Store 页面：

- [Ubuntu 16.04 LTS](https://www.microsoft.com/store/apps/9pjn388hp8c9)
- [Ubuntu 18.04 LTS](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q)
- [OpenSUSE Leap 15](https://www.microsoft.com/store/apps/9n1tb6fpvj8c)
- [OpenSUSE Leap 42](https://www.microsoft.com/store/apps/9njvjts82tjx)
- [SUSE Linux Enterprise Server 12](https://www.microsoft.com/store/apps/9p32mwbh6cns)
- [SUSE Linux Enterprise Server 15](https://www.microsoft.com/store/apps/9pmw35d7fnlx)
- [Kali Linux](https://www.microsoft.com/store/apps/9PKR34TNCV07)
- [Debian GNU/Linux](https://www.microsoft.com/store/apps/9MSVKQC78PK6)
- [Fedora Remix for WSL](https://www.microsoft.com/store/apps/9n6gdm4k2hnc)
- [Pengwin](https://www.microsoft.com/store/apps/9NV1GV1PXZ6P)
- [Pengwin Enterprise](https://www.microsoft.com/store/apps/9N8LP0X93VCP)
- [Alpine WSL](https://www.microsoft.com/store/apps/9p804crf0395)

## 3.启动并设置账户

点击<kbd>win</kbd>键，找到Ubuntu，点击打开

之后会显示`Installing...`等待安装完

之后会要求输入用户名和密码，按照自己的输入即可(ps:输入密码不会显示，输完之后回车即可)

## 4.修改软件源(可选)及更新和升级分发版的包

由于默认官方源服务器在国外，访问速度慢，因此将服务器源改为国内的：

`阿里云源`: http://mirrors.aliyun.com/ubuntu/
`清华源`: http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ 

方法一：修改源列表(`/etc/apt/sources.list`)

(1)模板：

```
deb http://cn.archive.ubuntu.com/ubuntu/ boinc main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-security main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-updates main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-backports main restricted universe multiverse
##測試版源
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-proposed main restricted universe multiverse
# 源碼
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-security main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-updates main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-backports main restricted universe multiverse
##測試版源
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-proposed main restricted universe multiverse
# Canonical 合作夥伴和附加
deb http://archive.canonical.com/ubuntu/ boinc partner
deb http://extras.ubuntu.com/ubuntu/ boinc main
```

(2)编辑

![1572958785969](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/wlu/1572958785969.png)

所有的源都是这种模式，我们需要改的是红绿部分，红色的为源地址，绿色的为Ubuntu版本代号

源地址为上面给的两个，直接替换掉就行

Ubuntu版本代号通过命令查看：

```
lsb_release -a
```

![1572958997879](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/wlu/1572958997879.png)

故修改后为

```
# 阿里云源
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
##測試版源
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
# 源碼
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
##測試版源
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse



# 清华大学源
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
##測試版源
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# 源碼
deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
##測試版源
deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```

(3)修改源文件` sources.list `

修改前我们先做个备份，在终端中执行以下命令：

```Ubuntu
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bcakup
```

然后执行下面的命令打开 sources.list 文件，清空里面的内容`dG`，把上面我们编辑好的国内的源复制进去，保存后退出<kbd>ESC</kbd>,`wq`+<kbd>Enter</kbd>。

```Ubuntu
sudo vi /etc/apt/sources.list
```

(4)更新软件列表和升级
在终端上执行以下命令更新软件列表，检测出可以更新的软件：

```Ubuntu
sudo apt-get update
```

在终端上执行以下命令进行软件更新：

```
sudo apt-get upgrade
```

方法二：通过[命令apt-add-repository]( https://blog.csdn.net/l740450789/article/details/50856596 )

略



## 5. 安装图形界面

对于Linux来说使用shell命令行完全满足大部分场景的使用，但是某些情况还是需要图形界面，比如查看图片、视频，浏览网页，UI设计等，还是需要图形界面的

### 安装必要软件包

可以通过执行`sudo dpkg-reconfigure locales` 选择zh-CN.UTF-8将系统切换为中文环境。

安装桌面、语言包、字体包、输入法等必要软件。

这里选择的是lxde轻量化桌面，个人比较推荐，当然也可以选择xfce，lxqt等其他桌面。

```
sudo apt install lubuntu-core lxde fcitx fcitx-googlepinyin
sudo apt install language-pack-gnome-zh-hans
sudo apt install fonts-wqy-zenhei
```

### 使用远程桌面软件连接

受限于Linux子系统实现原理，图形界面无法直接输出到显示器。

这里选择vnc远程桌面来解决，当然你也可以选择其他远程桌面方案。

最新版二进制包tigervnc_X86_64https://bintray.com/tigervnc/stable/download_file?file_path=tigervnc-1.9.0.x86_64.tar.gz，下载解压到根目录即可使用:

```
wget https://bintray.com/tigervnc/stable/download_file?file_path=tigervnc-1.9.0.x86_64.tar.gz
```

```
sudo tar -C / -zxvf download_file?file_path=tigervnc-1.9.0.x86_64.tar.gz
```

执行`vncserver :0 `打开一个远程桌面端口。:0 表示开启5900端口，:1表示5901端口，依次类推。vncserver详细用法见vncserver -h。

Win10打开[Windows端vnc客户端](https://bintray.com/tigervnc/stable/download_file?file_path=vncviewer64-1.9.0.exe)，输入IP(可用环回地址)和对于端口号即可进入图形界面。若为第0个端口（即5900）可省略。

![1572961279619](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/wlu/1572961279619.png)

通过客户端我们会发现，进入后为黑屏无图像显示。这是因为lxde桌面没启动。

第一次使用vnc会在用户家目录下生成 .vnc目录，里面是vnc的配置文件。通过在`~/.vnc/xstartup` 末行加上 `startlxde& `。

通过`vncserver -kill :0;vncserver :0`重启端口即可进入桌面。



 安装到此结束，然后就可以愉快地使用了。

