---
title: Mac使用Hexo和GitHub搭建博客(1)--搭建博客
author: luwang
avatar: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg
authorLink: wallleap.top
authorAbout: luwang
authorDesc: luwang
date: 2019-08-24 20:14:35
tags: [Hexo,GitHub,Blog,博客]
categories: 
    - 笔记
    - Hexo
comments: true
keywords: Hexo+GitHub Pages搭建博客
description: Hexo+GitHub Pages搭建博客
photos: https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/banner/banner1.jpg
---


## 一、安装

### （一）git安装及GitHub注册

1.git

命令安装git需要先安装好homebrew和XCode(可以先在APP Store下载)：
```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
安装git：
```shell
brew install git
```
2.GitHub

进入[GitHub官网](https://github.com)，Sign up页面输入相关信息，没有错误之后点击<kbd><font color="green">Sign up for GitHub</font></kbd>，注册账号
![2-1](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github1.png)
接着点击右上角头像，点击Your repositories
![2-2](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github2.png)
到达仓库(repositories)界面，点击<kbd><font color="green">New</font></kbd>
![2-3](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github3.png)
如图2-4，前面是用户名，仓库名设置为```用户名.github.io```，点击<kbd><font color="green">Create repository</font></kbd>，创建仓库
![2-4](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github4.jpg)
接着进入图2-5界面，左边的暂时不用管，直接点击头像
![2-5](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github5.jpg)
点击Settings
![2-6](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github6.jpg)
点击左侧导航栏中SSH and GPG keys
![2-7](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github7.jpg)

接着打开iTerm2或者终端输入一下命令
```
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱地址"
ssh-keygen -t rsa -C "你的邮箱地址"   #需要回车4次左右
cat .ssh/id_rsa.pub
```
将文件中的key复制下来

回到网页，单击<kbd><font color="green">New SSH key</font></kbd>
![2-8](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github8.jpg)
```Title```随意填，将刚复制的key粘贴到```Key```的文本框中，点击<kbd><font color="green">Add SSH key</font></kbd>

3.测试
输入命令```ssh -T git@github.com ```,显示如下字样，说明连接成功
![3](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/mac-blog1/github9.png)

### （二）node.js安装
在上一步基础上可以直接使用homebrew下载安装node.js，输入命令：
```brew install node```

### （三）Hexo安装
安装好git和node.js之后就可以使用npm安装Hexo了
```npm install -g hexo-cli ```
如果报的不是关键性错误，可以跳过不管，直接下一步




## 二、Hexo初始化及本地测试
### 1.初始化Hexo
创建一个目录用来作为你的blog目录，例如 blog；并在该目录中进行Hexo的初始化：
```
hexo init blog
cd ~/blog
npm install
```
### 2.本地测试
先安装hexo server
```
sudo npm install hexo-server 
```
然后生成静态页面并打开hexo本地服务
```
hexo generate   (或 hexo g)
hexo server
```
按命令行提示，打开http:/\/localhost:4000即可测试代码了。 



## 三、配置

### 1.关联GitHub账户
进入blog目录，编辑该目录下 **_config.yml** 文件
```
cd ~/blog
vi _config.yml
```
修改最下方的 __deploy__：
```
deploy:
type: git
repo: git@github.com:y/用户名.用户名github.io.git   #将你刚刚创建的仓库地址复制过来
branch: master
```

接下来安装hexo的git部署，在命令行中执行：
```
npm install hexo-deployer-git --save
```
最后，将生成静态页面并部署到github的仓库中，执行：
```
hexo generate
hexo deploy
```
或者```hexo d -g ```

### 2.基本配置
详情见[配置](https://hexo.io/zh-cn/docs/configuration)
一下是基本的配置
```
# Hexo Configuration
## Docs: https://hexo.io/docs/configuration.html
## Source: https://github.com/hexojs/hexo/
# Site  ##页面信息
title: Who's Blog  ##标题，即浏览器标签栏显示的内容
subtitle: Why so serious?  ##副标题
description:        ##描述，简介
author:        ##作者
language: zh-CN  ##语言
timezone: Asia/Shanghai  ##时区

# URL
## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
url: http://用户名.github.io              ## 有些人说这里填域名，可是后面需要用到图片的相关插件，这里填写这个即可
root: /
permalink: :year/:month/:day/:title/
permalink_defaults:

# Directory  ##文件目录，可不改
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:
# Writing  ##静态页面生成属性，可不改
new_post_name: :year-:month-:day-:title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link: true # Open external links in new tab
filename_case: 0
render_drafts: false
post_asset_folder: true   # 后面图片插入需要用到的
relative_link: false
future: true
highlight: 
enable: true 
line_number: true 
auto_detect: false 
tab_replace:

# Category & Tag ##标签，可不改
default_category: uncategorized
category_map:
tag_map:
# Date / Time format  ##时间格式，可不改
## Hexo uses Moment.js to parse and display date
## You can customize the date format as defined in
## http://momentjs.com/docs/#/displaying/format/
date_format: YYYY-MM-DD
time_format: HH:mm:ss

# Pagination ##每页显示文章数，按需改
## Set per_page to 0 to disable pagination
per_page: 10
pagination_dir: page
# Extensions ##主题设置
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: 3-hexo

# Deployment  ##git部署关联
## Docs: https://hexo.io/docs/deployment.html
deploy: 
type: git 
repo: github: https://github.com/用户名/用户名.github.io.git
branch: master
```

### 3.主题配置
#### 主题下载
到[Hexo的主题库](https://hexo.io/themes/)中挑选一个主题，比如3-hexo，首先找到[主题的仓库地址](https://yelog.org/2017/03/07/3-hexo/)，将文件克隆到themes目录下：
```
git clone https://github.com/yelog/hexo-theme-3-hexo.git themes/3-hexo
```
#### 安装插件
安装less，主题使用less作为css预处理工具：
```
npm install hexo-renderer-less --save
```
安装feed,用于生吃RSS：
```
npm install hexo-generator-feed --save
```
安装json-content，用于生成静态站点数据，提供搜索功能的数据源：
```
npm install hexo-generator-json-content --save
```
安装字数统计(由于主题使用这个插件，必须安装，否则会报错)
```
npm i --save hexo-wordcount
```
安装搜索插件
```
npm install hexo-generator-search --save
```

安装图片插件
```
npm install hexo-assert-folder --save
```

#### 新建页面
```
hexo new page tags    #开启标签页
hexo new page about。    #开启“关于”页
hexo new page categories #分类
hexo new page 404     #404
```
分别修改各个页面blog/source/tags/index.md的源数据：
```
---
title: tags
date: 2019-08-24 14:56:43
layout: tags
noDate: true
comments: false
---


---
title: about
date: 2019-08-24 19:27:02
---

---
title: categories
date: 2019-08-24 20:21:00
---

---
title: 404
permalink: /404
date: 2019-08-24 17:56:50
---
---
## 页面未找到！
```
#### 修改hexo配置文件_config.yml中的主题标签：
```
theme: 3-hexo
```

#### 修改主题配置文件blog/themes/3-hexo/_config.yml
[https://yelog.org/2017/03/07/3-hexo/](https://yelog.org/2017/03/07/3-hexo/)





## 四、测试后上传
### 1、测试
```
hexo g
hexo server
```
访问<http://localhost:4000/>，没有问题就可以上传了

### 2、上传
```
hexo d -g
```
### 3、访问网页
在浏览器输入地址：http://用户名.github.io即可访问

---
 **文章汇总：**
<table><tr><td bgcolor=#FFFF00> Mac使用Hexo和GitHub搭建博客(1)</td></tr></table>
<kbd>[go->](./index.html)</kbd>

<table><tr><td bgcolor=#D1EEEE>Mac使用Hexo和GitHub搭建博客(2)</td></tr></table>
<kbd>[go->](../mac-blog2/index.html)</kbd>

<table><tr><td bgcolor=#C0FF3E>Mac使用Hexo和GitHub搭建博客(3)</td></tr></table>
<kbd>[go->](../mac-blog3/index.html)</kbd>

<table><tr><td bgcolor=#54FF9F>Mac使用Hexo和GitHub搭建博客(4)</td></tr></table>
<kbd>[go->](../mac-blog4/index.html)</kbd>

---



