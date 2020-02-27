---
title: Mac使用Hexo和GitHub搭建博客(4)--博客维护
date: 2019-08-25 09:30:28
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
我们搭建好了博客，做好了美化，剩下的肯定就是默默的写文章啦，毕竟只有精品的文章才能更好地吸引流量啊

but写好了文章，万一因电脑故障等原因博客根目录直接删除了咋办呢

博客文章还好，毕竟已经上传了，直接导下来转换一下就OK了，但是自己美化的和其他配置咋办

so我们要做好备份

## 备份

首先在博客根目录`git init`创建 git 仓库，接着在 github（或其他托管平台、自建远程仓库等） 创建仓库并和本地仓库建立联系。

但是这个还是比较麻烦对吧

我们可以在GitHub上创建一个私有仓库，比如MyBlog，接着执行

```shell
git clone 仓库地址
```

把仓库克隆下来，这样直接就绑定了，不需要再进行其他配置

接下来我们要做的就是把以前的博客根目录下除了`.git`的其他文件和目录都复制过来

需要备份的时候就直接运行

```shell
git add . && git commit -m "update" && git push -f
```

就OK啦


## 设置快捷键

通过alias，触发一些命令的集合

在 ~/.bashrc 文件中添加

```shell
alias hs='hexo clean && hexo g && hexo s'
alias hd='hexo clean && hexo g && hexo d && git add . && git commit -m "update" && git push -f'
```

需要在本地调试时直接运行`hs`即可

部署和备份运行`hd`




