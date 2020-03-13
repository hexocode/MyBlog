---
title: 微信公众号图片防盗链破解
date: 2020-03-07 23:50
tags: [Hexo,Blog,博客,微信防盗链]
categories: 
    - 笔记
    - Hexo
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
comments: true
keywords: 
description: 
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---


知道微信可以利用Markdown Here插件使用Markdown语法写文章之后。

就一直是先在微信发布文章之后再copy到博客上。

因为图片可以放到微信上，不需要再上传到自己图床上了。

但是有一个问题，就是由于微信公众号图片防盗链机制，会让图片不正常显示。

看了这两篇文章：


[微信图片防盗链“此图片来自微信公众平台 未经允许不得引用”的解决方案](https://blog.p2hp.com/archives/5931)



[前端解决第三方图片防盗链的办法 - html referrer 访问图片资源 403 问题](https://juejin.im/post/5d074ee46fb9a07ede0b435d)

直接借用了第二篇文章的方法

referrer还是得留着，毕竟SEO需要

在head中加入了

<meta id="referrer" name="referrer" content="always" />
<script>
  const referrer  = document.getElementById("referrer");
  setTimeout(function(){
    referrer.setAttribute("content", "never");
  },5000);
</script>
Emmmm，好吧，还是不能用，如果你发现修改好代码能够使用，请留言告诉我哈，万分感谢





---



这种方法用不了了



然后在hexo的某个群中看到一篇文章：



[Typora原生集成PicGo了](https://zhuanlan.zhihu.com/p/112726299)



于是又重新打开了N久没用的PicGo，设置好之后，在Typora中写文章终于变得很爽了，哈哈哈