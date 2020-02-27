---
title: Mac使用Hexo和GitHub搭建博客(2)--优化配置
date: 2019-08-24 20:21:59
tags: [Hexo,GitHub,Blog,博客]
categories: 
    - 笔记
    - Hexo
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
comments: true
keywords: Hexo+GitHub Pages搭建博客
description: Hexo+GitHub Pages搭建博客
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---



## 一、修改_config.yml

搭建博客的时候顺便改了下基本的配置，现在来看下这些配置修改

>  ~/blog/_config.yml

这个是全局的配置文件，[上一个博客](../Mac使用Hexo和GitHub搭建博客-1/index.html)已经讲的很清楚了，这里不再赘述
由于需要用主题3-hexo高亮代码，将这里的高亮渲染关闭
```
highlight:
    enable: false
```
> ~/blog/themes/3-hexo/_config.yml
这个是主题的配置文件，仅给出需要修改的地方

> 你的头像url  需要到～/blog/themes/3-hexo/source/img下把avatar.jpg替换为自己头像
```
avatar: /img/avatar.jpg
favicon: /img/avatar.jpg
```
> 博客位置，如果没有错误不需要修改
```blog_path: /```
> 链接图标  将链接全部改为自己的即可
 ```   csdn: https://me.csdn.net/qq_36949103```
> 多作者模式  按需求填写
```
author:
    on: false
    authors:
        author1: luwang
        author2: wallleap
```
> 分类文章数、多级分类 按需启用 
```
category:
    num: true # 分类显示文章数
    sub: true # 开启多级分类
```
> 文末声明  改为自己的
```article_txt: 

```
> 打赏功能  需要到～/blog/themes/3-hexo/source/img下把weixin.jpg和alipay.jpg替换为自己微信和支付宝收款码
```
reward: true
```
> 其他的都有说明，自己看着修改就行
> 评论系统启用方式：[完美替代多说-gitment](https://yelog.org/2017/06/26/gitment/)


## 二、优化页面

### 1、主页 `~/blog/themes/3-hexo/indexs.md`
由于是.md文件，因此可以按照正常的Markdown语法进行修改

### 2、发布页模板 `~/blog/scaffolds/post.md`

为了以后写博文方便，可以按照习惯修改模板，我的模板如下：

```
---
title: {{ title }}
date: {{ date }}
tags: 
    - tag1
    - tag2
categories: 
    - category1
    - category2
---
```
标签改为多标签，分类为二级分类

### 3、其他页面

`hexo new page "about"`    
还有category等都可以添加

about页还需要修改主题_config.yml：
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic1.jpg)

## 三、域名解析

### 1、域名解析
进入到购买域名的控制台，找到域名服务或解析服务
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic2.jpg)
点击自己域名后的解析设置
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic3.jpg)
点击添加记录
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic4.jpg)
按照下图填写，注意记录值填`自己的用户名.github.io`
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic5.jpg)
也可以再添加主机记录用www的，这样输入www也能访问
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic6.jpg)
### 2、添加文件
做完了解析工作还是不行的，需要在仓库加上CNAME文件，文件中只需要填写域名，比如我的：
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/ mac-blog2/pic7.jpg)
由于仓库中上传时会自动删除，因此放到`~/blog/source/`下
## 四、评论系统

上面主题配置中有提到过，但对于一个博客而言，评论部分是不可或缺的，因此将其单独说明。

由于本人只用过`gitment`和`gitalk`，而个人感觉`gitalk`更好用一点，因此这里介绍`gitalk`使用，上面有`gitment`的教程链接
首先打开主题配置文件(`~/blog/themes/3-hexo/_config.yml`),找到评论设置，将comment字段的on设为true，type设为gitalk。找到gitalk字段，添加on:true,其他的评论系统字段添加on:false.接着打开链接[https://github.com/settings/applications/new](https://github.com/settings/applications/new),登录GitHub账户，
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic8.jpg)

注意callbalk URL一定要是自己域名的地址，接着点击绿色按钮，把Client ID和Client Secret复制到主题配置文件的gitalk字段相应位置，接着githubID和adminUser填自己的用户名即可,repo填博客的仓库(即`用户名.github.io`)
![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog2/pic9.jpg)


## 五、博客美化

### 1、了解hexo博客layout

### 2、修改layout中各布局代码

### 3、css美化

### 4、其他小部件






---
 **文章汇总：**
<table><tr><td bgcolor=#FFFF00> Mac使用Hexo和GitHub搭建博客(1)</td></tr></table>
<kbd>[go->](../mac-blog1/index.html)</kbd>

<table><tr><td bgcolor=#D1EEEE>Mac使用Hexo和GitHub搭建博客(2)</td></tr></table>
<kbd>[go->](../mac-blog2/index.html)</kbd>

<table><tr><td bgcolor=#C0FF3E>Mac使用Hexo和GitHub搭建博客(3)</td></tr></table>
<kbd>[go->](../mac-blog3/index.html)</kbd>

<table><tr><td bgcolor=#54FF9F>Mac使用Hexo和GitHub搭建博客(4)</td></tr></table>
<kbd>[go->](../mac-blog4/index.html)</kbd>

---
