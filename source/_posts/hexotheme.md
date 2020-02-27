---
title: 都2020了，带你开发hexo主题
author: hojun
avatar: https://cdn.jsdelivr.net/gh/honjun/ImageHosting/sina/006bYVyvgy1ftand2qurdj303c03cdfv.jpg
authorLink: https://hojun.cn
authorAbout: 一个好奇的人
authorDesc: 一个好奇的人
copyright: false
reproduce: 'https://mp.weixin.qq.com/s/XhTqTpA77is96QKqnVVzwg'
categories: 
	- 转载
	- 主题
date: 2020-02-04 22:16:01
comments: true
tags: 
     - 主题
keywords:
description:
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner11.jpg
---

# 都2020了，带你开发hexo主题



## 前言

本系列文章是[博主hojun](https://www.hojun.cn/)日常业余折腾HEXO所总结的经验结果，不一定是最佳实践。了解更多请关注[HEXO官方网站](https://hexo.io/)。关于HEXO主题已经折腾过好多，当然拆腾的都是比较有条理的。
有关[HEXO主题Sakura](https://github.com/honjun/hexo-theme-sakura)已经是去年（前年）的事了，第一次提交：honjun committed on 20 Dec 2018。偶尔怀旧下23333~，之前[关于Sakura主题开发也录了大部分的视频教程](https://www.bilibili.com/video/av43856893)，不过估计大部分人没有看，毕竟直接拿来用更香。这次准备出文章教程，顺带练习下我那半吊子的五笔打字。

## 准备工作

回归到正文，先总结下该教程的计划，首先html页面不准备写，去html5up上找个模版，众所周知（不知道的现在也知道了）这个网站已经出了好几个HEXO博客，包括Phantom、Massively、strata、simplyspoke、Editorial(还没做完，看完教程的可以用这个模版练练手，给它PR完整)。
最后，选定story就刚刚决定的。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66Om7cna03iaBqicXeIzmWPOaKGiaM3ibgXH4EicsMTm2weh3DGh5UomicyRGQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 逛官网，读文档

首先来到hexo官网，你要折腾某个东西的时候，它的官网是一定要逛的。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66oV6oiaicmjefXcWnOGoc2TYUJmbk0WbicOe1yWiaqlxLCRek59czgtPdHA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
找到自定义主题我们可以看到：（请务必认真看完再往后阅读）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66GdMpz4j8yISL1X59bYAvgtF9NIP5Z5sxPXfqsGqkf11BYe7VFXR6gA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 本地新建

假设你已经看完上图的文档了，开始开发主题了。首先还是要新建一个hexo博客，在卡在这一步的时候就可以Ctrl+C停止了。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66OvS11hXiaviafktnyXhibLic2biaQqGe8o9JjUnK3LXk8iarBly92HrU4Sog/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
用subline打开新建好的博客(Story)，可以看到在themes目录下空空如也，反正我们准备自己开发一个，空的正好。
这个时候就要想到文档里的目录结构了：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66G88F2LicWvRoHpZu2CbV45I3Pef3iciaSsZl2WuuBBXulAzaNkpANAEHA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
新建如下：（当然要给主题建个目录，这里就叫story好了）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66pjFziaWd6B5ZMTicCk7dGF0qyzPyBI3vIEw4bCSUMU8q4N2Z3pSiaDVIg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
建好这后记得上级目录的_config.yml里面修改配置：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66bN6mIsVwce2oHiaRf4dBFxj2dnl55I4wLerUh7fcv1u8gxFUGOEonHg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
有好奇的小伙伴可以试着运行看看：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u663e95aXFkkoL8QcX6WuB1DrFZ7ku1We57Nf2WrgE5EdKX06BEcR3DVg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
不要担心，这是我们没有用npm安装依赖，因为上一步的时候直接ctrl+c跳过了。使用npm i命令安装。（有切换过淘宝镜像的可以使用cnpm i安装，npm安装淘宝镜像自行百度）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66ohuQ9hm51klBKjraLD3rtNpZCtWIwxQx4reIMJ33Xic2CQX93psF8bQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到安装成功后使用hexo s发布真的能跑起来，不过当我们访问的时候就会报No layout: index.html这个错。简单理解下它意思，没有layout(布局，或者说模版):index.html。

## 选择模板引擎

那么我们就应该建一个layout来展示index.html。不过在建之前要先确定用哪种模版引擎，官方文档如是说到：Hexo 内建 Swig 模板引擎，您可以另外安装插件来获得 EJS、Haml 或 Jade 支持。这里为了简单，学习成本低，采用了ejs模板引擎。文档也说的很明白了，用ejs我们还要安装。不过看了下package.json，hexo4.0已经集成了hexo-renderer-ejs，所以用ejs也不用安装了，直接用就是。（Jade等还是要另外安装插件的）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwetbsqfNUzTRqGfVgsF6u66mXX9Mwh95fibkh8fVjhY6GEn997PmJuFiceptKBNY34bjoE7DqXOSNCw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 构建主题页面

模板引擎选好之后，就可以新建模版页面了。在新建前要好好看下官方文档的模版说明。看完之后可以自己构思下怎么做
t

h

i

n

k

i

n

g

想不出来的可以参考下别人或者官方的主题是怎么做的。

## 构建主题页面

我们在阅读文档模版后，可以知道如下信息：

> 模板决定了网站内容的呈现方式，每个主题至少都应包含一个 index 模板，以下是各页面相对应的模板名称：

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SWIw5MOMKibqyTWvib2r8nmRzxVUlia4tkAX0LaIh0ryElOHm0QpPQfSWQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 布局（Layout），如果页面结构类似，例如两个模板都有页首（Header）和页脚（Footer），您可考虑通过「布局」让两个模板共享相同的结构。一个布局文件必须要能显示 body 变量的内容，如此一来模板的内容才会被显示，举例来说：

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5Sk9sUe2WBzLyiaakS1uYPx9SCFagCldH27mnjdtm8pN2d7BH6mGBCjDA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 每个模板都默认使用 layout 布局，您可在 front-matter 指定其他布局，或是设为 false 来关闭布局功能，您甚至可在布局中再使用其他布局来建立嵌套布局。

关于front-matter可以查下以下文档了解更多front-matter

```
Front-matter 是文件最上方以 --- 分隔的区域，用于指定个别文件的变量，举例来说：

---
title: Hello World
date: 2013/7/13 20:46:25
---
```

根据以上文档，我们就可以建模版页面了。其中`每个主题至少都应包含一个 index 模板`和`每个模板都默认使用 layout 布局`，所以我们先建个layout.ejs和index.ejs
index.ejs内容如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SvymxaHOCcRbjMIDJlBicxS4HD4CcbQtCyMplPmSk1MjUXTflH48JjLw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
layout.ejs内容如下：其中`<%- body %>`文档中并没有做出详细解释，可以理解body为页面内容。首页就是引入index.ejs，归档页就是引入archive.ejs这样。至于`<%- %>`的语法可以去参考ejs文档(看不懂的，就是没好好看文档。)
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SwVwcXMHqYnekVEeVGc5P9UeDAtBemVUInh7tNeDib73BcRoHibny3fHg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
hexo s 生成运行如下，可以看到我们的模版页编译成功了。（生成了layout的头部和尾部，并成功显示出了index中的内容）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5S0gYAbhXYot3El5kStqiaDKNhThvdEleQIZYQfk0JJu8aehIpqTDpP1Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
好了，主题页面就是这样构建的，接下来开始把从html5up上下载的story写成我们的主题。

## 构建 hexo-theme-story 首页

解压得到：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SqCEFd5j65Rya8kRXcORicBEF2ps2BoHgBMxWBTGJiaS0MRwKk4h9zmSA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
在subline中打开其index页面如下
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SeH34S9qfLy6Nuqd8zR6mZr5cIo1YIJvWHpS8ZB5KqqgnJPgbwTsLFA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我们要拆解这个页面，从简单的header和footer开始，将其代码收缩，可以就大致分出header、body、和footer了。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SfSB4TVCg8rcSnXoeVMH7Zic8l7l8cG5pGNyD0Hib6Ffr0NpLPUIhLibEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
再看官方文档中关于局部模版的说明，我想你已经学会怎么拆分了
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SWCtMjPzqFUX8ib1F7qNIicQGmKlBRA1cwiaWev2mhYYAmo6k26PRiat7IQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
文件夹这样建立：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5Sx7QnNuBpOS9Q00ZrCHuKiciajJ7tiaBXicIe0elEiaqqGKagnMl65bjrKLg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
稍难点的layout这样写：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5ScjSRfULCwiamo2YGtyqISo9nypQSxsorgamg2FfMBE0tfb4vNxegsOQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
但是这样拆分还是有些问题，比如有部分的footer内容在index中，暂时把这部分代码直接剪切到footer.ejs中
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SGXsMv7LEicxS9ibkrzjO0ibHbwzubEpkBdkU48W3zS6hmKZGoVgBvxrgw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
运行后页面如下所示：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SiaX2RoPwvhmewK3uYQCwWPhxRSaGYU1wYltEFxtEdAJO9dZ0R7XNzGg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
页面这种显示的原因是我们没有导入js、css。

## 导入css、js

> source
> 资源文件夹，除了模板以外的 Asset，例如 CSS、JavaScript 文件等，都应该放在这个文件夹中。文件或文件夹开头名称为 _（下划线线）或隐藏的文件会被忽略。
> 如果文件可以被渲染的话，会经过解析然后储存到 public 文件夹，否则会直接拷贝到 public 文件夹。

所以我们的 CSS、JavaScript、Images 文件要放在source文件夹中，怎么放我就不赘述了。说说怎么引入。可以hexo g先生成public文件夹，看一下目录结构：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SaMwJIVvptKmUdkVrSGTchrr4UrJBAK5BlUD9q0UHRiaqhjicsBH97GWA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到对于最外层的index.html来说，引入可以使用更通用的相对路径写法`./css/xxx.css`(./表示当前目录下)，但是这种写法放在hello-world下的文章页index.html就不适用了。必需使用绝对路径写法`/css/`（/表示从根目录开始）所以可以使用如下写法引入：

```html
<link rel="stylesheet" href="/css/main.css" />
<noscript><link rel="stylesheet" href="/css/noscript.css" /></noscript>
```

但是这种写法也有一个问题，若你的博客不是放在网站根目录也是不生效的。所以hexo辅助函数css()，js()就有意义了。

```ejs
<%- css(path, ...) %>
<%- js(path, ...) %>
```

最终改写成如下：
```html
<head>
  <title>Story by HTML5 UP</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
  <%- css(['/css/main.css', '/css/noscript.css']) %>
</head>
```
js雷同。
把layout中的注释改成html注释，hexo s 运行预览下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwf5qXudsPYOVrfldHecZK5SgDlWE1qicd3p4V3sDTbO5iccyWXeRWtmJlqP7LrCmSLc74WkRtdBWEyg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到页面已经正常了，图片路径自行修改下就可以呈现。
从这教成开始代码开始变多起来，我把代码同步上传到github仓库和百度云上，~关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story002获取。



我们已经搭建好了首页，上篇教程已经引入了css和js，接下来还是引入网站上的一些图标。

## 引入图标

上篇教程自行引入图片其实是不用的，因为我们建立的图片文件夹正好是images，和原来的html5up模板刚好一致。让我们看下代码：

```html
<div class="image">
  <img src="images/banner.jpg" alt="" />
</div>
```

但是也和之前的问题一样，用这种的话一定要把网站放到根目录访问，所以可以用到hexo的辅助函数“url_for”，
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UcgsHl1micMic4J5qjEUkK1iaibMknDTp7vcErJ5ia6oX3ibpDZ9PhsK5IV3Rw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
img代码改成如下即可：

```html
<div class="image">
  <img src="<%- url_for('/images/banner.jpg') %>" alt="" />
</div>
```

接下来回到正题，引入图标，首先确定下这个模板的图标是字体图标，字体文件在webfonts文件夹下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UcOUVGUr4bBVjSmwPaCaqIEg2UQTEic7rvzcHVPB0SVdgjfLe2l8ewI4A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
为了方便，就直接把这个文件夹复制到主题source下，hexo s 后就可以看到图标已经呈现出来了
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1Uc998BZqsUGTuWjjOFgkHrSzJDYmZJUOdCviapiahxmFsvgCSbrXCicrG8w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 完善首页

开始着手完善首页，首先删掉一些不需要的元素
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1Uc6lgWoR3YEgTWic9wcAXRHaTL3kKeicrdNoJ0dh8icmwYOyg86CwKSwpYw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
在index.ejs中的这个Five、Six、Seven分别是图集、图标、留言部分，首页不需要这些，我们给它删掉。
接下来看剩下的代码：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UcKYC87nPgfNmBFh27RdG7loLhTQ9c7V5nRfbzdsJ1A0XREpZ0tspnOA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
one是最上面的那个，图片占一半那种。自成一派先不管。two、three、four则是下面的部分。我们可以给它看做是文章列表。可以看出这几个的元素都一致，就是three的class是orient-left，所以可以删除多余的three、four后网页显示如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1Ucw38Xv5s12y9MuffskjV80cAIHtXqrotYAKOib8UGaCFGSn5p87LRdnQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
接下来考虑往首页填充内容了。不过在这之前还有很多东西要讲下（后悔用文章教程了，出视频的话会快很多55555）

首先，分析下我们首页或者说文章需要哪些东西。标题、封面图、简介还有一些给我们的如分类、标签、时间等等。这些东西都要我们自己建吗？hexo给了我们一个Scaffold文件夹，在官方文档的写作里面有说明：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UccgLMkg9uyDALAwFmiaRoickYyJhkSW0Q4tw8TSMlnyRHiazSsXMyiagFdA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
打开scaffolds>post.md(就是新建文章的模板)可以看到如下内容：（顺带再提，这个在hexo中叫Front-matter）

```
---
title: {{ title }}
date: {{ date }}
tags:
---
```

可以看到hexo给文章模板预置了title、date、tags，但是我们还需要封面图、简介、分类等等，我们直接修改post.md就可以让hexo生成我们想要的模板。修改的模板如下：(keywords是关键字，对网站seo有好处)

```
---
title: {{ title }}
date: {{ date }}
tags:
categories:
keywords:
description:
photos:
---
```

这里为了更方便我们可以给一些项预设初值。比如分类和封面图。

```
---
title: {{ title }}
date: {{ date }}
tags:
categories: 技术
keywords:
description:
photos: /images/pic01.jpg
---
```

好了，接下来可以使用 hexo n “你想要的文章名” 来创建文章了。这里我们创建了八篇文章：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UcKicRrOicLddofPg4GwQ2FCShrY0dMZsRWUV2SRy7JWicDU7zyUFStZJqQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
记住把第一个hello world.md删掉，因为这个是hexo init生成的，在它的Front-matter中没有一些项，不删除可能会导致一些错误。
好了，测试文章也有了，现在我们要去给首页填充起来。现在我们再来看index.ejs中的one和two,发现one其实和three一样是orient-left，不过多了个fullscreen的css，所以可以只剩下一个two。修改后two的代码如下：

```ejs
<!-- Two -->
<% page.posts.each(function(post){ %>
  <section class="spotlight style1 orient-right content-align-left image-position-center onscroll-image-fade-in">
    <div class="content">
      <h2><%= post.title %></h2>
      <p><%= post.description %></p>
      <ul class="actions stacked">
        <li><a href="#" class="button">Learn More</a></li>
      </ul>
    </div>
    <div class="image">
      <img src="<%= post.photos %>" alt="" />
    </div>
  </section>
<% }) %>
```

其中each/forEach函数（和js中的each差不多）参考model.js和query.js，post参考变量。![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1Ucfglhib2hyhRCJO30N1QqYSrWhEicUibclib2kiaiayFXGny7OFQJvhIg8czQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
hexo s后生成如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1Uc4JrZLIxA2w0Mz3p3eEW2UL4czx8HbzcianoZmg0tKn8iceFicc7GYF78g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
怎样将它弄成之前那种左右交替呢？最简单的可以使用css控制：

```css
.spotlight.style1:nth-child(even) {
  -moz-flex-direction: row-reverse;
  -webkit-flex-direction: row-reverse;
  -ms-flex-direction: row-reverse;
  flex-direction: row-reverse;
}

.spotlight.style1:first-child{
    min-height: 100vh;
}

.spotlight.style1:first-child .image{
    width: 50%;
}
```

稍微解释一下这个css,

> nth-child(n) 选择器匹配属于其父元素的第 N 个子元素，不论元素的类型。
> odd 和 even 是可用于匹配下标是奇数或偶数的子元素的关键词（第一个子元素的下标是 1）。
> 使用公式 (an + b)。描述：表示周期的长度，n 是计数器（从 0 开始），b 是偏移值。

就是匹配.spotlight.style1这俩class的元素。even表示偶数，就表示偶数项为row-reverse（设置

元素内弹性盒元素的方向为相反的顺序，参考flex布局），奇数项为row。所以就能实现左右左右的效果。而first-child则表示第一项，100vh表示 “相对于视口的高度，视口被均分为100单位的vh” 即铺满屏幕。最终效果如下
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdBKiamAvULZUXIKRc4dc1UceFWfeic0Yx9WWm4AJBwXszuhBNR3phg3ljyQJ8lhjuFlcQzJfA8YvYw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story003获取。



## 添加分页

上篇教程已经把首页内容给填充上去了，接下来继续给首页添加上分页。在文档辅助函数里有关如下
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsB4DIW2Ox0ssRjTlSFkOMT6oWiaiaAv0bt5INc3zcDVR9DPQJCzIiao7Zug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
直接复制这段代码到index.ejs最下面:

```ejs
<div class="paginator">
  <%- paginator({
    prev_text: '<i class="fa fa-angle-left"></i>',
    next_text: '<i class="fa fa-angle-right"></i>',
    escape: false
  }) %>
</div>
```

为了看到效果将根目录下config中的per_page改为三，表示每页三篇文章，这样我们八篇文章就会有三页了

```yml
index_generator:
  path: ''
  per_page: 3
  order_by: -date
```

hexo s后的效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsB1pRibaPxO7L3QCClibX5vlBNdiboD0xVZCSeFUibCbnYaFxJgLTvrn3Yeg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
样式有点不能忍受，用f12工具查看其html代码如下：

```html
<div class="paginator">
  <span class="page-number current">1</span>
  <a class="page-number" href="/page/2/">2</a>
  <a class="page-number" href="/page/3/">3</a>
  <a class="extend next" rel="next" href="/page/2/"><i class="fa fa-angle-right"></i></a>
</div>
```

为了方便直接在index.ejs中写css如下：(最终效果如下图)

```css
<style>
  .paginator {
    margin-top: 2em;
    width: 100%;
    text-align: center;
  }
  .paginator .page-number{
    display: inline-block;
    border-radius: 50%;
    font-size: 0.8em;
    font-weight: 600;
    height: 2em;
    line-height: 2em;
    margin: 0 0.125em;
    min-width: 2em;
    padding: 0 0.5em;
    text-decoration: none;
  }
  .paginator .current{
    box-shadow: inset 0 0 0 1px #47D3E5;
    color: #47D3E5 !important;
  }
</style>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsBib2En7LoxaNLZib7zoama77Ra2dGmPAZ5qjGqgX2MBtwvTNcnMjRH8ZA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 添加文章详情页

首先在_partial下新建article.ejs，里面代码如下：（story居然没有文章页的模板233，果然好模板都被人用了）

```ejs
<article>
  <%- page.content %>
</article>
```

然后在index.ejs中的a标签中加入文章超链接：

```html
<div class="content">
  <h2><a href="<%- url_for(post.path) %>"><%= post.title %></a></h2>
  <p><%= post.description %></p>
  <ul class="actions stacked">
    <li><a href="<%- url_for(post.path) %>" class="button">Learn More</a></li>
  </ul>
</div>
```

那么怎样让文章页能更根据我们的article.ejs页生成呢？回到一开始的模板介绍：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsBlxXAWiaptZ6r0k75kmGTdibloPXShvmBs24S4QJY6QqTibwnCYjUicsWRQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
按照hexo的文档来，post是用来显示文章的，我们在layout目录下新建这几个ejs(post、page、archive、category、tag），然后暂且把article中的内容复制到post.ejs下，hexo s预览下效果：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsBUsJG1bsJGZ6RWAY5l3xAn5FU65Qv1ibVgc4RkeJJUxIz0yHP0rf0kYg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
已经是能渲染出来了，但是md里面还没有内容，这里我直接把这篇文章的md复制到测试的md中

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfWibEjPrMjibCxiaaSRAkeZsBw2CUJoicO0tnrSCiaIMAiciaL3axz3YOEzC4lXeWiaZA1Pc3y1SKtJhoHwg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

样式又差不行不行，这个留到下篇教程再美化，现在把之前留下的问题解决，乍一看article.ejs是无用武之地了，不过考虑到page这个单页面的渲染和post差不多一致，所以我们要把文章部分抽离到article.ejs中，这样就可以复用代码了。抽离在教程二中就已经讲到，用局部模版（Partial），代码如下：

```ejs
<%- partial('_partial/article', {post: page}) %>
```

后面的{post: page}表示把page变量存到post中传递给了article，所以article中的代码就要改为：

```ejs
<article>
  <%- post.content %>
</article>
```

代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story004获取。



## 美化详情页


上篇文章已经可以跳转到文章详情页了，这篇教程先来美化下详情页的样式。
首先打开我们从html5up上下载的story网页，浏览器上打开index-demo.html那个，在演示完图标之后有“Additional Elements”
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxFhRgVCjEswJPKNLKHxMDXZibnV3H83jJ9Qw3PFZ7DGRb91eWiaV9e1ng/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到这部分用来当文章详情页的容器挺合适。修改代码如下：

```ejs
<article class="wrapper style1 align-left">
  <div class="inner">
    <%- post.content %>
  </div>
</article>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxVDQ0sPzjNyZnxEmebicjqlpV3fALwxs1Zw6jgMk2KmLcULOVcAW4nMg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

可以看出这个页面还缺一些必要的内容，如标题。添加后如下：

```
<article class="wrapper style1 align-left">
  <div class="inner">
    <div class="header">
      <h1 class="title"><%- post.title %></h1>
      <div>
        <span>日期：<%- post.date %></span>
        <span>字数：<%- post.count %></span>
      </div>
    </div>
    <%- post.content %>
  </div>
</article>
```

main.css

```css
/* 添加的css项 */
.title {
  font-size: 3rem;
  font-weight: 700;
}
article h2 {
  font-size: 1.7rem;
}
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxoLuAGH1A9hOHMgDla6ThU5FeicjGE5zAgyRmwlkGBDJAun1TxZyp2Wg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 解决日期和字数显示

可以看到网页上的日期显示的是一串数字，其实这个是日期的时间戳

> 百度百科：时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总毫秒数。通俗的讲， 时间戳是一份能够表示一份数据在一个特定时间点已经存在的完整的可验证的数据。它的提出主要是为用户提供一份电子证据， 以证明用户的某些数据的产生时间。在实际应用上， 它可以使用在包括电子商务、 金融活动的各个方面， 尤其可以用来支撑公开密钥基础设施的 “不可否认” 服务。

来到hexo官网，搜索date:
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxqn31wDXGndwd5HriaennYkJuYpNk26H1NylfcSfYSgelOkH31I2qSvw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxS9VZiaiaXoh27CTs5mqVjXDzMNPcKEak5FqOFUWCz96akXLBwpBZZtHw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
修改成下图：

```
<span>日期：<%- date(post.date, 'YYYY/M/D') %></span>
```

页面显示如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxgNzOKC4z3OhMKjrH2WvygpfIEaQibZ1icPIQ6w961ZfIxribTp5zblKjg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
和官方例子不一样，应该是文档错了。那如果要文档里那种显示该如何修改代码呢？接下来部分是干货，会举一反三的话能自己解决很多问题。分析下，date()这个函数归类在辅助函数helper里。所以先去找有没有hexo-helper-date的包，（在node_modules里找）。没找到，因为这个官方的辅助函数，试着在hexo-cli和hexo里面找。在node_modules_hexo@4.2.0@hexo\lib\plugins\helper\中找到我们要的date.js这个文件。打开它可以看到
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxys1eebZqlo9XXITWqXFQn4MefMibuLjhrunUWVUNT5icjRgghkVAtAwA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)它都原封不动的调用了 Moment.js，所以我们在hexo文档中直接点击date说明上面那个 Moment.js 的超链接去看 Moment.js 文档。找到了如下表：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwx9D8t7Micp6CKI8Ir1Fxb0K18nHYBjHS6Z4ZQv1UZ0Vic2stYuQchZPNA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
那就简单了，改成自己想要的日期显示类型就行。参考如下：

```
<span><%- date(post.date, 'MMMM DD, YYYY, dddd ') %></span>
```

接下来改成中文月份，只要在根目录的config下把language改为zh-cn即可。(为啥知道，看文档和源)

日期解决后就要来看下字数，现我们已经知道文章内容在post.contant里。用post.content.length这种写法会把html标签也算进去，hexo给我们提供了strip_html字符串处理函数：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxs26O7VtmOfDYTjIPx5HNWfnjHh0GeKxZiaeWIibYUsrSFEdmbZcNlE4g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
所以只要strip_html(post.content).length这种写法就好了。效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVweTW3WEhquqOHoCGkma1zwxiaLFBMibLdlqXlNBqwy6icpeybNj9MX2CpBsOHRGxtEy9BMib8fDEyvaLw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story005获取。




## 添加阅读次数

阅读次数采用不蒜子来实现

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdqzAlcDm1Dw5YTtZtiax0MqvxyuULKDuaVglAD99ic9k06PlBvFrQ1FjwKZEGMX8qZm96NTQJICvqw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

复制这两行代码，引入js的那段放到footer.ejs中，span的那段放在文章详情页中。

```
<article class="wrapper style1 align-left">
  <div class="inner">
    <div class="header">
      <h1 class="title"><%- post.title %></h1>
      <div class="stuff">
        <span><%- date(post.date, 'MMMM DD, YYYY') %></span>
        <span>字数  <%- strip_html(post.content).length %></span>
        <span id="busuanzi_container_site_pv">阅读 <span id="busuanzi_value_site_pv"></span></span>
      </div>
    </div>
    <%- post.content %>
  </div>
</article>
```

## 添加valine评论

前往valine.js.org官网，查看文档：
![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)
关于valine和leandcloud一些配置项请参考另一篇文章《hexo评论系统之valine快速使用》，这里就不赘述了。假设你已经有了API_ID和API_Key了，我们先把valine官方文档快速开始中的html片段复制到article.ejs(即文章详情页中)，因为我们是在页面body中了，所以要把head和body删掉，修改后代码如下:

```ejs
<!-- valine评论 -->
<script src='//unpkg.com/valine/dist/Valine.min.js'></script>
<div id="vcomments"></div>
<script>
  new Valine({
    el: '#vcomments',
    appId: '<API_ID>',
    appKey: '<API_Key>'
  })
</script>
```

接下来可以把API_ID和API_Key填入就可以使用了，不过这是开发主题，所以最好要把这些变量在配置里面赋值。在主题下的config里面输入如下：

```yml
valine:
  API_ID: 这里填你的API_ID
  API_Key: 这里填你的API_Key
```

接着修改valine部分代码如下：

```ejs
<!-- valine评论 -->
<script src='//unpkg.com/valine/dist/Valine.min.js'></script>
<div id="vcomments"></div>
<script>
  new Valine({
    el: '#vcomments',
    appId: '<%- theme.valine.API_ID %>',
    appKey: '<%- theme.valine.API_Key %>'
  })
</script>
```

网页上显示如下:
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdqzAlcDm1Dw5YTtZtiax0MqmNtUHgicl4DgYzHglBQ3y0Tya3lPv76m1icaBo0jRAXAweDCgsOsbX6Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
valine评论的样式乱了，使用f12工具发现main.css把input元素设为了块级元素（还有其他一些问题），所以在css中加入

```css
#vcomments input {
  display: inline-block;
}

#vcomments button {
  height: 2.25rem;
}
```

## 添加评论数

因为在valine的显示中是有评论数这个选项的。但文档里面并没有给我们提供这个接口，所以我们可以自行调用valine的函数来获取。代码如下:（看源码无所不能）

```ejs
<article class="wrapper style1 align-left">
  <div class="inner">
    <div class="header">
      <h1 class="title"><%- post.title %></h1>
      <div class="stuff">
        <span><%- date(post.date, 'MMMM DD, YYYY') %></span>
        <span>字数 <%- strip_html(post.content).length %></span>
        <span>评论 <span id="valine-count"></span></span>
        <span id="busuanzi_container_site_pv">阅读 <span id="busuanzi_value_site_pv"></span></span>
      </div>
    </div>
    <%- post.content %>
    <!-- valine评论 -->
    <script src='//unpkg.com/valine/dist/Valine.min.js'></script>
    <script src='//cdn.jsdelivr.net/npm/leancloud-storage/dist/av-min.js'></script>
    <div id="vcomments"></div>
    <script>
      var valine = new Valine();
      valine.init({
        el: '#vcomments',
        appId: '<%- theme.valine.API_ID %>',
        appKey: '<%- theme.valine.API_Key %>'
      })
      valine.Q(location.pathname.replace(/index\.html?$/, '')).count().then(num => {
        document.getElementById("valine-count").innerHTML = num;
      })
    </script>
  </div>
</article>
```

效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdqzAlcDm1Dw5YTtZtiax0MqWYeKc1qke6fLJrDhrhnhib97ClDKrl8TiaL8hMpwcCdZbKC9EibezDh6Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 添加上一篇和下一篇

这里直接使用了自己当前主题的代码，这个功能实现起来只要知道hexo官方文档中page变量就行：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdqzAlcDm1Dw5YTtZtiax0MqUg9QUQEI1kFdcgNrCAp3ydWlPYSnleHs71G7zIZqjDoFpDddibGQVNw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
代码和效果如下:

```ejs
<div class="post-nav">
    <% if (post.prev){ %>
    <div class="post-nav-prev post-nav-item">
        <a href="<%- url_for(post.prev.path) %>" ><%= post.prev.title %><i class="fa fa-chevron-left"></i></a>
    </div>
    <% } %>
    <% if (post.next){ %>
    <div class="post-nav-next post-nav-item">
        <a href="<%- url_for(post.next.path) %>" ><%= post.next.title %><i class="fa fa-chevron-right"></i></a>
    </div>
    <% } %>
</div>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdqzAlcDm1Dw5YTtZtiax0MqmNtUHgicl4DgYzHglBQ3y0Tya3lPv76m1icaBo0jRAXAweDCgsOsbX6Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story006获取。



## 添加文章标签

打算在hr的上边添加文章的标签，用f2开发者工具调试如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQCQh1NewX7O3EEEic2ncQaevianKrsEHjibuT7v5jqXfpMoKAv2vr3YLqA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
先到css的8551行把margin调为0：

```css
hr {
    margin: 0 0 0 0;
}
```

接着在hr上面添加html元素，先写好再调样式：

```html
<div class="tags">
  <span>标签：</span>
  <a href="" class="tag">XX标签</a>
  <a href="" class="tag">XX标签</a>
</div>

```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQ9PsAPJEYWzDrfdDA97QETyUD3F2qagLO1WCpeqxqckSFuAqvf7gL3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
再写css，可以自行添加一些交互效果，自由发挥：

```css
.tags a {
  font-size: 15px;
  padding: 3px 5px;
  text-decoration: none;
}

.tags a:hover{
  color: #fff;
  background: #333;
}
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQMhNkQThDWZjWhicdloYhBMFES4M8DrJ60ic0MzySzVdhNriap9oVcq6PQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

当然现在的标签不是文章设置的标签，来到官网可以看到：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQ7QfxDCiaTEy58wpgUSevl8lQYiaM7tGTTNXyicnoaTtlACXlBHXciattVA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
所以只要把page.tags循环输出即可。

```ejs
<div class="tags">
  <span>标签：</span>
  <% post.tags.each(function(tag){%>
    <a href="" class="tag">{{ tag.name }}</a>
  <% }) %>
</div>
```

当然了，再查看效果前你要给md加上标签才行：

```
---
title: story6
date: 2020-01-18 22:11:30
tags:
 - tag1
 - tag2
categories: 技术
keywords:
description:
photos: /images/pic01.jpg
---
```

![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)
光显示了名称还不行，还要跳转到相关页面，那url怎么获取呢？官方文档中并未做详细说明，可以去看源码。不过最简单的还是把tag输出就知道了，在tags循环中加入console.log：

```
<% post.tags.each(function(tag){%>
  <% console.log(tag) %>
  <a href="" class="tag"><%= tag.name %></a>
<% }) %>
```

可以看到cmd输出如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQ64XPCXGbnahIlKsLYhggxpXbqvD8Iibjaza6TrBYEjxvSzvemuXGJPA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
所以tag.path就可以获取到url了

```
<div class="tags">
<span>标签：</span>
<% post.tags.each(function(tag){%>
  <a href="<%- url_for(tag.path) %>" class="tag"><%= tag.name %></a>
<% }) %>
</div>
```

## 标签页空白？

再上一步加好url后，尝试点击标签，会跳转到一个页面:
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQxJyiaTb7XgB8Iu8NWJJkTUzyBfmLqjxLTgf9rIiaU4qPD77VY47DJyzQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
为啥除了footer全是空白。回想一下之前的文章详情页的时候是不是也这样，再次回顾文档：
![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)
加上这句：

> 每个模板都默认使用 layout 布局，您可在 front-matter 指定其他布局，或是设为 false 来关闭布局功能，您甚至可在布局中再使用其他布局来建立嵌套布局。

分析一下，链接跳转tag模板，默认使用layout:

```
<html>
  <!-- //头部模版 -->
  <%- partial('_partial/header') %>
  <body class="is-preload">
    <!-- //内容模版 -->
    <%- body %>
    <!-- //尾部模版 -->
    <%- partial('_partial/footer') %>
  </body>
</html>
```

所以在加载了footer和header(header只是引用css等，不会在页面显示)，然后<%- body %>加载了tag模板。而我们的tag模板里啥都没有，所以显示空白。

## tag页模板

tag页怎么建好呢，没想好的可以参考下其他主题点击标签后的效果。等你想好前可以试着验证下上一步的分析推论，在tag.ejs下加入如下代码：(可以看到页面出来了)

```html
<h1>This is Tags page</h1>
<h1>This is Tags page</h1>
<h1>This is Tags page</h1>
<h1>This is Tags page</h1>
<h1>This is Tags page</h1>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQoO0oJx1GJvmicMicbUwcxyUzvcVSfWjZKpZkEF2hicmykicDXdq2qBk4YQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

回到正题，tags页面应该显示什么？点击某一个标签，一个标签对应n篇文章（至少有一篇）。所以应该显示的是属于该标签下的文章列表页。所以tag.ejs中应该写显示文章列表页的代码，等等！index首页是显示文章列表页，tag是显示文章列表页，将来分类category也是显示文章列表页，我们应该把显示文章列表页部分单独抽离出来。hexo大部分主题用archive来表示文章列表页，但归档页也叫archive，这里为了好理解，就叫post-list好了。
在_partial下新建post-list.ejs文件，把index中的文章列表部分代码复制进去。(应该是全部233333，因为首页没其他东西了)
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQ8BB81IjKmPhluwbOJfwNTSunAjbcNYlnKSl4IicflzygaTQKJqf9FxA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
然后index和tag页都只要简单的引用post-list就行了。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwfUJbzBpSW0MMvBLOZAo6CQ5icrxHqWVJvxEqsy0gXZuEOkQhZguUf6Qu0aCpX65hJvSZuLkVBGN6A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story007获取。



## 继续完善文章详情页 

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdpWG8fTQjsjV05gD7hSTiaD3JISrw4AhFDGSvJstKgdjMw7gkMia3nmgAmKfTQjddd47GSO5nb5qyA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
现在的页面右边留空太多了，整体看上去不够居中。所以调下css:

```css
article.wrapper.style1 > .inner {
  padding: 2rem 2.5rem 3rem 2.5rem;
  margin: 50px auto;
  width: 960px;
  box-shadow: 1px 0px 5px 1px #ccc;
}
```

接着图片和代码块超出了范围：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdpWG8fTQjsjV05gD7hSTiaDkSUU7UzVGSHNw0kzX1d9NdhaFgHuAIZRAdNCXoUTow9HwUNxS9qnJA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

```css
article.wrapper.style1 > .inner img {
  width: 100%;
}

article.wrapper.style1 .highlight {
  overflow: auto;
}
```

## hexo-helper-tocbot添加文章目录toc

如果觉得目录有需要的继续往下看，这里直接安利我之前开发的hexo插件hexo-helper-tocbot及教程[hexo-helper-tocbot插件使用教程](http://mp.weixin.qq.com/s?__biz=MzI2NjE5Nzg4NQ==&mid=2247484082&idx=2&sn=29b6cb808c1d6804994876521b9ce744&chksm=ea908ca0dde705b64e61742117daa2c60ded907e51b77b1b7b11a6d6036c36596f956874c6da&scene=21#wechat_redirect)。

### 安装

在cmd中使用npm或cnpm安装：

```shell
npm i hexo-helper-tocbot --save
```

### 配置

安装好后在主题下的config中添加教程中的配置：

```yml
tocbot:
  contentSelector: .post-content
  scrollSmooth: true
  headingSelector: h1, h2, h3, h4, h5
  headingsOffset: 45
  scrollSmoothOffset: -45
```

其中headingsOffset和scrollSmoothOffset要和你主题的头部高度相对应。含义详见API

最后在article.ejs中添下如下代码（注意，这里要把content用

包起来才能识别）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdpWG8fTQjsjV05gD7hSTiaDuxNWiccb1KeDnWET0okfIQVF0QvxWQ8u1H2Xf7KOWmh8vZo68iccicfeA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



## 添加返回首页按钮

网上找了个svg按钮，放上去，然后把a的href改为javascript:history.back(-1)就行，修改后代码如下：（可自由发挥，找更棒的）



```
<article class="wrapper style1 align-left">
  <!-- 返回按扭 -->
  <a href="javascript:history.back(-1)" class="cd-nav-trigger"> 
    <span class="cd-nav-icon"></span>
    <svg x="0px" y="0px" width="54px" height="54px" viewBox="0 0 54 54">
    <circle fill="transparent" stroke="#656e79" stroke-width="1" cx="27" cy="27" r="25" stroke-dasharray="157 157" stroke-dashoffset="157"></circle>
    </svg>
  </a> 
  ......
  ......
```



css:



```css
/* 返回按钮 */
.cd-nav-trigger {
  transform: rotate(180deg);
}
.cd-nav-trigger {
  position: fixed;
  z-index: 3;
  left: 5%;
  top: 20px;
  height: 54px;
  width: 54px;
  background-color: #233;
  border-radius: 50%;
  overflow: hidden;
  text-indent: 100%;
  white-space: nowrap;
  transition: transform 0.5s;
}
#cd-nav {
  color: #9cb3a8;
  text-decoration: none;
}
.cd-nav-trigger .cd-nav-icon {
  position: absolute;
  left: 50%;
  top: 50%;
  bottom: auto;
  right: auto;
  transform: translateX(-50%) translateY(-50%);
  width: 22px;
  height: 2px;
  background-color: #ffffff;
}
.cd-nav-trigger circle {
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 0.4s 0.3s;
}
.cd-nav-trigger circle {
  transition: stroke-dashoffset 0.4s 0s;
}
.cd-nav-trigger .cd-nav-icon::before, .cd-nav-trigger .cd-nav-icon:after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 50%;
  height: 100%;
  background-color: inherit;
  transform: translateZ(0);
  backface-visibility: hidden;
  transition: transform 0.5s, width 0.5s;
}
.cd-nav-trigger .cd-nav-icon::before {
  transform-origin: right top;
  transform: rotate(45deg);
}
.cd-nav-trigger .cd-nav-icon::after, .cd-nav-trigger .cd-nav-icon::before {
  width: 50%;
  transition: transform 0.5s, width 0.5s;
}
.cd-nav-trigger .cd-nav-icon::after {
  transform-origin: right bottom;
  transform: rotate(-45deg);
}
```



代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story008获取。





继续完善主题，老实说能从一跟着练习到这里的人，开发一个自己的hexo主题已经不是什么难事了。（前题有html、js、css[学习这三最快的地方首推w3cshool]）。开发到这里其实已经讲的差不多了。剩下一些功能都是类似或可有可无的。比如分类和标签是类似的，单页面都是一样的，今天我个就来开发一个单页面。

## 文章归档单页面

即archive页，如果还记得之前的教程或有认真看过hexo文档的话，应该知道它是官方给出的六大模板之一。这也是它特殊的地方。如果你打开hexo根目录的package.json的话就能发现：(关于package.json是干啥用自行百度，好奇能使你进步)
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUtp3xIpuJjDaP7k4OXn0Pnq1cJ9oXbaiccOe7icxC3JB8VzSyJveoyiasw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
archive、category、index、tag都在里面，而且都是hexo-generator开头的。那么hexo-generator又是什么呢？来到hexo官网的api页：

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUFfayURFlTtjHvDQXUBFjVmdsspbmvQ5XTGs7V9YXN4hzy1O2Ntov1Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

而且也举了归档页面的例子来向我们说明:
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUsicmkaprhw2ClJgiahZGTurj6buxUoIichZlhywEoFdcVtibd1JneYEWhg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
认真看懂它。
意思是生成archives/index.html这个文件，提供的数据为所有的文章(data: locals.posts,)，渲染的模板是archive，没有archive就用index替补（layout: [‘archive’, ‘index’]）

好了好了不扯了，关于hexo运行原理一时半会儿也说不完。

## 编写代码

以上扯了这么久就是说我们直接在archive.ejs里面撸代码就行了。嗯嗯网上找了个模板，样子如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUEhMFHH98J0Bf6yFLvE3PGraUH1hSvJ9GdSCNjEHn2RLPxA4ZWh1oOw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
先直接将代码复制到archive.ejs中，在source/css中新建archive.css，把需要的css复制其中。再在archive.ejs中引入，部分代码如下：

```html
<%- css(['/css/archive.css']) %>
<div class="content">
  <article>
    <h3>2013</h3>
    <section>
      <span class="point-time point-yellow"></span>
      <time datetime="2013-03">
        <span>March</span>
        <span>2013</span>
      </time>
      <aside>
        <p class="things">The FAW</p>
        <p class="brief"><span class="text-yellow">Award</span> (Miami. FL)</p>
      </aside>
    </section>
    <section>
      <span class="point-time point-red"></span>
      <time datetime="2013-03">
        <span>March</span>
        <span>2013</span>
      </time>
      <aside>
        <p class="things">You reached 500 followers on Twitter</p>
        <p class="brief"><span class="text-red">Social Appearance</span></p>
      </aside>
    </section>
  </article>
```

hexo s后，在浏览器地址栏输入localhost:4000/archives/就能访问到：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUAuwsYo1RGN2YZLbcpwbFMbZTAy7Ga0icev8mcdW5TDTG4iaNRPzkUBGw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)找到archive的页面变量：（page.year和page.month是undefined，可能哪里需要设置）
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUicV8parwl5vnjFHR0zWLKgmqVBLQ3A4eGIEHVTYcYKNjbZN8efNXJFw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
然后去把测试的md文章都改下时间。万事具备，接下来开始修改html代码：

```html
<%- css(['/css/archive.css']) %>
<div class="content">
  <% console.log(page)%>
  <% page.posts.each(function(post){ %>
    <% console.log(post.title)%>
  <% }) %>
  <article>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUVxKpzGfzzRcpjK7KkIQdUGIxgLicqTI9rOebuKjfztxibUgteuXqgJ6w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
这里说明一下，8,9,5都是我改了后还是2020年的，2019和2018的不在。说明page.posts是不全的，我们应该用网站变量：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUHlUcqZNbUD27xrCiafVrUib16apD1MkyzgfTZalz3UMtd1uqzCmfkiaSA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

```
<%- css(['/css/archive.css']) %>
<div class="content">
  <% console.log(site)%>
  <% site.posts.each(function(post){ %>
    <% console.log(post.title)%>
  <% }) %>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUNJCBk4FJcJ9Usic0M9iaA4hheFYGFzylTHVsmq5qUHMyJaAICnE8KqZA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
但是可以看出它似乎没有按照时间排序，前面我们有说过page.posts是Model.js的model对像，在Query.js中给我们提供了个sort方法如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUBD6T2siclzKgLyIddJQ55rVP9zQUiazXSrIrRmyIp3Pl63H388Njc60Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
所以修改代码如下：

```
<%- css(['/css/archive.css']) %>
<div class="content">
  <% console.log(site)%>
  <% site.posts.sort('date').each(function(post){ %>
    <% console.log(post.title)%>
  <% }) %>
```

![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZU7icVtZDY17yX1RyawEwPr2N2JczlNvtn2VAI1ofNBQXlv3P3OdNQsRQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到已经按时间排序了。

coding……

```
<%- css(['/css/archive.css']) %>
<div class="content">
  <% var tempYear %>
  <% var posts = site.posts.sort('date') %>
  <% posts.each(function(post, i){ %>
    <% var currentYear = parseInt(date(post.date, 'YYYY')); %>
    <% if (tempYear != currentYear){ %>
      <% tempYear = currentYear %>
      <article>
        <h3><%- currentYear%></h3>
    <% } %>
        <section>
          <span class="point-time point-yellow"></span>
          <time datetime="<%- date(post.date, 'YYYY-MM')%>">
            <span><%- date(post.date, 'MMMM DD,')%></span>
          </time>
          <aside>
            <p class="things"><%= post.title%></p>
             <p class="brief"><span class="text-yellow"><%= Object.values(post.categories.data[0])[0] %>
            </span></p>
          </aside>
        </section>
    <% if (!posts.eq(i + 1) || currentYear != parseInt(date(posts.eq(i + 1).date, 'YYYY'))){ %>
      </article>
    <% } %>
  <% }) %>
</div>
```

最后效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwdxTfh1Rq6s8gavhOm6siaZUxT6ia1lVylj8iaXhHdnjKk1lw2LTJ1TZHLe20NuMBqZuiaGAcB15WpW5w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果想让归档列表按照分类显示不同颜色怎么实现呢？

代码解释和实现方法待续 To be continued……
代码同步上传在github仓库和百度云上，关注公众号[Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)回复story009获取。





## 代码解释



```html
<%- css(['/css/archive.css']) %>
<div class="content">
  <% var tempYear %>
  <% var posts = site.posts.sort('date') %>
  <% posts.each(function(post, i){ %>
    <% var currentYear = parseInt(date(post.date, 'YYYY')); %>
    <% if (tempYear != currentYear){ %>
      <% tempYear = currentYear %>
      <article>
        <h3><%- currentYear%></h3>
    <% } %>
        <section>
          <span class="point-time point-yellow"></span>
          <time datetime="<%- date(post.date, 'YYYY-MM')%>">
            <span><%- date(post.date, 'MMMM DD,')%></span>
          </time>
          <aside>
            <p class="things"><%= post.title%></p>
             <p class="brief"><span class="text-yellow"><%= Object.values(post.categories.data[0])[0] %>
            </span></p>
          </aside>
        </section>
    <% if (!posts.eq(i + 1) || currentYear != parseInt(date(posts.eq(i + 1).date, 'YYYY'))){ %>
      </article>
    <% } %>
  <% }) %>
</div>
```



首先在循环外部定义了两个变量teamYear和posts。其中tempYear用来保存临时的年份信息，posts则是保存了按时间排序的所有文章数组。接下来循环posts，第一次循环的时候用currentYear来保存当前这篇文章的创建的年份，此时tempYear肯定和currentYear不等的，所以能进入if语句，将currentYear赋值给tempYear，并生成了article和年份的标题。接下来就是生成文章信息，没啥好说的。最后在用eq(i+1)来获取下一篇文章的信息。顺带一提，eq()这方法也是Model.js中提供的方法。如果没有下一篇了或者下一篇文章的创建年份和这一篇不同，则结束article标签，下一个循环又会再一次进if语句，生成新的年份。反之下一循环还在这一年份，那么此时tempYear肯定和currentYear是相等的，则不会进入if语句，只是在article中增加了一个section来展示文章。（不知道看懂没，我觉得应该能看懂了）

## 分类显示不同颜色

首先我们确定颜色是由text-yellow这个class决定的，只要把每个分类名对应一个颜色类就搞定了。可以使用js来实现，当然也可以用css来实现（中文类名也是可以的哦，当然不支持这样做）。这里我采用取巧的方法，顺带也讲个hexo文档中重要的知识点：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwen53icYdnElhxLWE09tibDulCOaicGvBePq1RdY8gaRmtnQ8OhALYCDHGdf5PkibgmNKIdPxCT36iaSoA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
我们要用它的关键在这里：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwen53icYdnElhxLWE09tibDulyJHsEicjIjJXukg5aXkGLbZvQKTp4ZxsOhcahOKT4UMMsvD74p3qRvA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
因为我们的language: zh-cn，所以在主题languages文件夹中新建zh-cn.yml，然后在里面输入下内容



```
color:
  技术: blue
  生活: green
  相册: red
  vlog: yellow
```



修改archive.ejs如下：



```html
......
<section>
  <!-- 取巧方法，只认第一个分类 -->
  <% var category = Object.values(post.categories.data[0])[0]%>
  <span class="point-time point-<%= __('color.' + category)%>"></span>
  <time datetime="<%- date(post.date, 'YYYY-MM')%>">
    <span><%- date(post.date, 'MMMM DD,')%></span>
  </time>
  <aside>
    <p class="things"><%= post.title%></p>
    <p class="brief"><span class="text-<%= __('color.' + category)%>"><%= category%>
    </span></p>
  </aside>
</section>
......
```



然后顺带把article.ejs中的返回按钮也给它加上，最终效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwen53icYdnElhxLWE09tibDuldK36WJt35HI4Yv81LzpNHnxEgGIOUHz7J2mqJTibvaaYwic8OkaBM2yQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 首页侧边栏导航

主题开发到这其实还有很多必要的东西未加上去，比如现在首页还没有一个导航能够到archive.ejs页，手机端适配等很多问题。还有一些小功能，比如赞赏、分享等等。想了一下，现在最紧急的应该就是首页导航了，准备用侧边栏。网上找了个侧边栏代码如下：



```html
<nav>
  <div class="menu-btn">
    <div class="line line__1"></div>
    <div class="line line__2"></div>
    <div class="line line__3"></div>
  </div>

  <div class="sub-menu-btn">
    <div class="line line__1"></div>
    <div class="line line__2"></div>
  </div>

  <ul class="nav-links">
    <li class="link">
      <a href="#">Home</a>
    </li>
    <li class="link">
      <a href="#">About</a>
      <ol>
        <li><a href="#">designers</a></li>
        <li><a href="#">developers</a></li>
      </ol>
    </li>
    <li class="link">
      <a href="#">Work</a>
      <ol>
        <li><a href="#">web</a></li>
        <li><a href="#">graphic </a></li>
        <li><a href="#">apps </a></li>
      </ol>
    </li>
    <li class="link">
      <a href="#">Contact</a>
      <ol>
        <li><a href="#">Email</a></li>
        <li><a href="#">Social</a></li>
      </ol>
    </li>
    <li class="link">
      <a href="#">follow me</a>
      <ol>
        <li>
          <a target="_blank" href="https://www.17sucai.com/">
            Twitter <i class="fab fa-twitter"></i>
          </a>
        </li>
        <li>
          <a target="_blank" href="https://www.17sucai.com/">
            Codepen <i class="fab fa-codepen"></i>
          </a>
        </li>
      </ol>
    </li>
  </ul>
</nav>
```



包括css和js代码添加在story\source\js\sidebar.js和story\source\css\sidebar.css，而后在header中引入css,footer中引入js，由于篇幅有限，这里就不展示了。这里说一下为啥有些css和js不在header和footer中引入，比如archive.css。因为这个css只有归档页面中有用到，没必要在其他页面中引入它，这也加快了页面加载速度，后其也可以把多个css、js合并压缩成一个，这样会减少请求次数，也优化了页面速度。

加入后效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwen53icYdnElhxLWE09tibDul1Q1q08KKtMiaPv0bvF98qCvWuqYMsME5jN5BmVLU4l5icDj7GHJwVjXA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码同步上传在github仓库和百度云上，关注回复story010获取。



## 完善侧边栏 

上一篇教程我们已经把侧边栏成功的加入到我们的story主题中了，但是该侧边栏还是写死的数据。所以开始把它和我们的主题目录绑定起来。有用过hexo主题的朋友应该知道在config中一般有个menu配置项，用来配置博客的模板页。今天我们就来实现这一过程。
在此之前，有一样东西必须要了解一下（虽然不了解也没事）。那就是config.yml，如果说你学习过其他语言，甚至是开发过一些项目。那么你用的配置文件可能是.json.conf.xml.pro.ini。那么hexo中的.yml又是什么呢？感兴趣的可以学习另一篇文章：[yaml基本语法及实现Hexo二级导航栏功能](http://mp.weixin.qq.com/s?__biz=MzI2NjE5Nzg4NQ==&mid=2247484098&idx=4&sn=9291661cbddfcb5c4950143814a6d1a7&chksm=ea908cd0dde705c6e0e19f0db2b896353ca66665742869c636eba5f4cfa6b605119b42f6e2a6&scene=21#wechat_redirect)
开始撸代码之前我们要在config中添加sidebar的项：（暂定如下，图标还未考虑好）

```
sidebar: # 侧边栏
  首页: { path: /, fa: fa }
  归档: { path: /, fa: fa }
  关于: { path: /, fa: fa }
  项目: { path: /, fa: fa, submenus: { 
    hexo-theme-sakura: { path: /, fa: fa}, 
    hexo-theme-story: { path: /, fa: fa}, 
    hugo-theme-diaspora: { path: /, fa: fa}, 
    hugo-theme-jsimple: { path: /, fa: fa}
  } }
  友链: { path: /, fa: fa }
  FOLLOW ME: { path: /, fa: fa, submenus: { 
    qq: { path: /, fa: fa}, 
    sina: { path: /, fa: fa}, 
    github: { path: /, fa: fa },
    weichat: { path: /, fa: fa}, 
    bilibili: { path: /, fa: fa },
  } }
```

因为post-list中的代码已经够多，而且侧边栏也不算是post-list，所以我们在_partial下新建一个sidebar.ejs文件，把侧边栏代码放进去。然后修改代码如下：(为啥用for in?因为循环的是对象)

```html
<nav>
  <div class="menu-btn">
    <div class="line line__1"></div>
    <div class="line line__2"></div>
    <div class="line line__3"></div>
  </div>

  <div class="sub-menu-btn">
    <div class="line line__1"></div>
    <div class="line line__2"></div>
  </div>

  <ul class="nav-links">
    <% var sidebar = theme.sidebar %>
    <% for (item in sidebar) {%>
      <li class="link">
        <% if (!sidebar[item].submenus) {%>
          <a href="<%- url_for(sidebar[item].path) %>"><%- item %></a>
        <% } else { %>
          <a href="<%- url_for(sidebar[item].path) %>" style="pointer-events: none;"><%- item %></a>
          <ol>
            <% for (submenu in sidebar[item].submenus) {%>
              <li><a href="<%- url_for(sidebar[item].submenus[submenu].path) %>"><%- submenu %></a></li>
            <% } %>
          </ol>
        <% } %>
      </li>
    <% } %>
  </ul>
</nav>
```

就里讲下pointer-events: none
pointer-events 更像是JavaScript，它能够：

- 阻止用户的点击动作产生任何效果
- 阻止缺省鼠标指针的显示
- 阻止CSS里的 hover 和 active 状态的变化触发事件
- 阻止JavaScript点击动作触发的事件

了解更多参考MDN:pointer-events
侧边栏效果如下：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwegBEzbL544WYeRUgnRbwq4lBicxfmicxSsh7Tn3PDsicjRBgRkWEWxFW6UkGHs8PPLftRSeIuic17GxA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 给侧边栏添加图标

先在header.ejs中添加fontawesome的css:

```
<%- css(['/css/main.css', '/css/noscript.css', '/css/sidebar.css', '/css/fontawesome-all.min.css']) %>
```

接着来到fontawesome官网
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwegBEzbL544WYeRUgnRbwq45KHK1qFds94m7m1ekjTdhw0GO6ic12ayJjv9ttiaWgUIgZKEDupIiaTbg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
点击图标，找到home的class。同理找到其他的图标。
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwegBEzbL544WYeRUgnRbwq4UbTobL7DbXIhQc7VaOTUS5TcfoxOvCdywrAiaMhic0YEUZVOFS3gJH7w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
修改config如下：（subsmenu就留给你们练手了）

```
sidebar: # 侧边栏
  首页: { path: /, fa: fa fa-home }
  归档: { path: /archives/, fa: fa fa-archive }
  关于: { path: /, fa: fa fa-question-circle }
  项目: { path: /, fa: fa fa-paper-plane, submenus: { 
    hexo-theme-sakura: { path: /, fa: fa}, 
    hexo-theme-story: { path: /, fa: fa}, 
    hugo-theme-diaspora: { path: /, fa: fa}, 
    hugo-theme-jsimple: { path: /, fa: fa}
  } }
  友链: { path: /, fa: fa fa-link }
  FOLLOW ME: { path: /, fa: fa fa-heart, submenus: { 
    qq: { path: /, fa: fa}, 
    sina: { path: /, fa: fa}, 
    github: { path: /, fa: fa },
    weichat: { path: /, fa: fa}, 
    bilibili: { path: /, fa: fa }
  } }
```

然后修改sidebar.ejs代码如下：(加了个i标签哦)

```
<% if (!sidebar[item].submenus) {%>
  <a href="<%- url_for(sidebar[item].path) %>"><i class="<%= sidebar[item].fa %>"></i><%- item %></a>
<% } else { %>
  <a href="<%- url_for(sidebar[item].path) %>" style="pointer-events: none;"><i class="<%= sidebar[item].fa %>"></i><%- item %></a>
```

最终效果如下！：
![img](https://mmbiz.qpic.cn/mmbiz_png/7oh1DvJRVwegBEzbL544WYeRUgnRbwq4VdiadLy84CFLwUuBn7SJPHmUgeRdLQ2X8kx4Qm0Eicg1SC3BnrPtrbrg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)


代码同步上传在github仓库和百度云上，关注回复story011获取。





<font text-align="center">本文完</font>
由于转载的，故图片不想一个个弄出来了
你们自己到作者公众号去看吧




<font color="red" size="18px">文章来源：</font>

***

<font color="pink" size="6px">|文章链接：</font>[都2020了，带你开发hexo主题](https://mp.weixin.qq.com/s/XhTqTpA77is96QKqnVVzwg)

<font color="pink" size="6px">|公众号：</font> [Creators创作者](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2NjE5Nzg4NQ==&scene=124#wechat_redirect)

<font color="pink" size="6px">|作者：</font>Hojun

<font color="pink" size="6px">|作者博客：</font>https://www.hojun.cn/

***



