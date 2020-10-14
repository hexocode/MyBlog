---
title: 怎样拥有两个独立的Chrome
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
tags:
	- 前端
	- web
categories:
	- 笔记
	- 前端
comments: true
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/cover/(00).jpg'
date: 2020-03-24 10:33:14
keywords: 前端, web, Chrome
---

## 1、问题起源

* 由于自己日常使用的Chrome安装了太多插件，调试的时候受插件的影响，很难进行识别，因此需要一个单独用于开发调试的Chrome
* Chrome默认安装到C盘，移动到其他盘之后，再进行安装打开的仍是同一个浏览器



## 2、解决方法

主要就是利用Chrome的多用户会生成一个独立的、相互隔离的浏览器

### 方法一、自己指定存放数据路径(推荐)

1、进入Chrome所在目录(可以通过默认的快捷方式右击-属性-打开文件所在位置)，接着右击Chrome，选择创建快捷方式

![创建快捷方式](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716091222532.png)

2、对创建的图标进行命名，右键属性

![属性](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716091419216.png)

3、目标字段：添加`--user-data-dir`参数，设置一个目标存放数据，笔者设置的是`D:\ChromeData\WebChrome`

![修改目标](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716091648127.png)

4、确定（可以换一个图标再点确定！）

### 方法二、直接生成新用户快捷方式

 打开谷歌浏览器，点击如下的图标

![点击图标](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716092020261.png)

点击添加

![点击添加](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716092116598.png)

输入任意用户名，默认勾选添加快捷方式，点击添加

![image-20200716092240575](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716092240575.png)





之后就可以使用独立的Chrome了

![image-20200716092343187](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716092343187.png)

而且，你可以在开发工具中指定Chrome路径为你创建的快捷方式的路径，之后默认就会以该浏览器打开网页了

![IDE指定Chromepath](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/image-20200716092823125.png)



参考文档：

- [Chrome双开(同一个版本配置两个独立的浏览器,附图)](https://blog.csdn.net/lpw_cn/article/details/105574710)
- [启动多个独立谷歌浏览器](https://blog.csdn.net/QiaoRui_/article/details/86512063)