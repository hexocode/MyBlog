# <center><font size="18px" color="red">wallleap</font></center>


## <center><i class="fa fa-ravelry" aria-hidden="true"></i>每日一句</center>
<i class="fa fa-volume-up" aria-hidden="true"></i><span id="hitokoto">:D 获取中...</span>
<p align="right" id="afrom"></p>
<script src="https://cdn.jsdelivr.net/npm/bluebird@3/js/browser/bluebird.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/whatwg-fetch@2.0.3/fetch.min.js"></script>
<script>
  fetch('https://v1.hitokoto.cn')
    .then(function (res){
      return res.json();
    })
    .then(function (data) {
      var hitokoto = document.getElementById('hitokoto');
      var afrom = document.getElementById('afrom');
      hitokoto.innerText = data.hitokoto;
      afrom.innerText =  '——【' + data.from + '】';
    })
    .catch(function (err) {
      console.error(err);
    })
</script>

## <center><i class="fa fa-music" aria-hidden="true"></i>欣赏音乐</center>
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=100% height=450 src="//music.163.com/outchain/player?type=0&id=2162711186&auto=1&height=430"></iframe>



## <center><i class="fa fa-angle-double-right" aria-hidden="true"></i>对博客的理解</center>
喜欢写Blog的人，会经历三个阶段。
>第一阶段，刚接触Blog，觉得很新鲜，试着选择一个免费空间来写。

>第二阶段，发现免费空间限制太多，就自己购买域名和空间，搭建独立博客。

>第三阶段，觉得独立博客的管理太麻烦，最好在保留控制权的前提下，让别人来管，自己只负责写文章。
 
我们每个人的在网络上产生的数据越来越多，这些信息是我们在互联网上存在过的痕迹，值得我们认真对待。但是它们被分散分布在各个网站上。很多时候我们很难将它们聚合在一起，而且各个网站的信息排布方式也没有办法自由控制，所以我们需要一个可以由自己主宰的空间——博客。

通过博客，我们可以记录自己的生活和成长的轨迹。它不像 Twitter 那样碎片化，也不像 Facebook 那样关系化，它是私人的空间。

## <center><i class="fa fa-leaf" aria-hidden="true"></i>关于wallleap</center>
**wallleap** 是Luwang的个人站。

到目前为止已经写了<code class="article_number"></code>篇文章， 共<code class="site_word_count"></code>字。

本站访问人数：<code class="site_uv"></code>人次 ， 访问量：<code class="site_pv"></code>次

## <center><i class="fa fa-bold" aria-hidden="true"></i>博客平台</center>
这个博客通过 [Hexo](https://hexo.io/) 生成，部署在 [GitHub Pages](https://pages.github.com/)，主题 [3-hexo](https://github.com/yelog/hexo-theme-3-hexo) 已经在github上开源

- 三段式设计(分类、列表、正文)、分类过滤、关键字搜索(详情看下面)、多种评论模块支持、文章置顶、返回头部、多作者、二级分类等
- 搜索支持文章标题、标签(#标签)、作者(@作者)
- pad/手机等移动端适配
- 页面全局快捷键 <a href='http://yelog.org/2017/03/24/3-hexo-shortcuts/'>3-hexo快捷键说明</a>
- 文章置顶功能，参考[Hexo置顶及排序问题](https://yelog.org/2017/02/24/hexo-top-sort/)，直接加入代码即可，不要安装插件
- 字数统计：[hexo加入字数统计WordCount](https://yelog.org/2017/03/09/Hexo-WordCount/)
- [为Hexo添加RSS和Sitemap](https://yelog.org/2017/03/14/Hexo-RSS-Sitemap/)
- [3-hexo支持mermaid图表](https://yelog.org/2019/11/12/3-hexo-support-mermaid/)
- 评论模块[gitment](https://github.com/imsun/gitment)，解决报[object ProgressEvent]的问题:[使用Heroku，解决gitment登录失败，报object ProgressEvent的错](https://segmentfault.com/a/1190000018177680)
- 简易相册，[fancybox加入](https://github.com/honjun/hexo-tag-fancybox_img)
- [bilibili视频插入](https://github.com/Z4Tech/hexo-tag-bilibili)
- 底部悬浮音乐，使用的[APlayer](https://aplayer.js.org/#/zh-Hans/)，但是修改的代码有点多，就不说了；页面音乐：
```html
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=100% height=450 src="//music.163.com/outchain/player?type=0&id=2162711186&auto=1&height=430"></iframe>
```
- 一言引入：[hexo博客添加一言](https://www.jianshu.com/p/3a58d9a796c3)
- [看板娘](https://www.jianshu.com/p/ebde730615f5)
- 创建404页面：我们可以直接使用html代码，设置不渲染`layout: false;`



## <center><font color="blue"><i class="fa fa-pencil-square-o" aria-hidden="true"></i>留言板</font></center>

> 大伙快来留言呐~
