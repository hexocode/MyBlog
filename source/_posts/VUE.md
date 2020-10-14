---
title: Vue学习笔记
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
tags:
	- 前端
	- web
	- Vue
	- JavaScript
categories:
	- 笔记
	- 前端
comments: true
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/cover/(00).jpg'
date: 2020-08-28 12:33:14
keywords: 前端, web, Vue
---



## 一、Vue概述

### 1.1 前言

#### 1.1.1 前端开发模式的发展

1. 静态页面

- 最初的网页以HTML为主，是纯静态的网页。网页是只读的，信息流只能从服务端到客户端单向流通。开发人员也只关心页面的样式和内容。

2. 异步刷新，操作DOM

- 1995年，网景工程师Brendan Eich花了10天时间设计了JavaScript语言。
  - 随着JavaScript的诞生，我们可以操作页面的DOM元素及样式，页面有了一些动态地效果，但是依然是以静态为主。
- ajax盛行：
  - 2005年开始，ajax逐渐被前端开发人员所重视，因为不用刷新页面就可以更新页面的数据和渲染效果。
  - 此时的开发人员不仅需要编写HTML样式，还要动ajax与后端交互，然后通过js操作DOM元素来实现页面动态效果。比较流行的框架如jQuery就是典型代表。

3. MVVM，关注模型和视图

- 2008年，Google的Chrome发布，随后就以极快的速度占领市场，超过IE称为浏览器市场的主导者。
- 2009年，Ryan Dahl在谷歌的Chrome V8引擎基础上，打造了基于事件循环的异步IO框架：Node.js。
  - 基于事件循环的异步IO
  - 单线程运行，避免多线程的变量同步问题
  - js可以编写后台diamante，前后台统一编程语言
- Node.js的伟大之处不在于让js迈向了后端开发，而是构建了一个庞大的生态系统。
- 2010年，NPM作为node.js的包管理系统首次发布，开发人员可以遵循CommonJS规范来编写Node.js模块，然后发布到NPM上供其他开发人员使用。目前已经是世界上最大的包模块管理系统。
- 随后，在Node的基础上，涌现了一大批的前端框架：

![image-20200827092403465](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827092819.png)



#### 1.1.2 MVVM模式

M：Model，模型，包括数据和一些基本操作

V：View，视图，页面渲染结果

VM：View-Model，模型与视图间的双向操作(无需开发人员干涉)

在MVVM之前，开发人员从后端获取需要的数据模型，然后要通过DOM操作Model渲染到View中。而后当用户操作视图，我们还需要通过DOM获取View中的数据，然后同步到Model中。

而MVVM中的VM要做的事情就是把DOM操作完全封装起来，开发人员不用再关心Model和View之间是如何相互影响的：

- 只要Model发生了改变，View上自然就会表现出来。
- 当用户修改了View，Model中的数据也会跟着改变。

把开发人员从繁琐的DOM操作中解放出来，把关注点放在如何操作Model上。

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827093743.png)

MVVM通过**视图**与**模型**的**双向绑定**，简化前端操作。

Vue就是一款MVVM模式的框架



### 1.2 认识Vue

> Vue (读音 /vjuː/，类似于 **view**) 是一套用于构建用户界面的**渐进式框架**。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与[现代化的工具链](https://cn.vuejs.org/v2/guide/single-file-components.html)以及各种[支持类库](https://github.com/vuejs/awesome-vue#libraries--plugins)结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

- 前端框架三巨头：Vue.js、React.js、Angular.js，Vue.js以其轻量易用著称，Vue.js和React.js发展速度最快。
- 遵循 MVVM 模式  
- 渐进式 JavaScript 框架  
  - 渐进式：可以**选择性**地使用该框架的一个或一些组件，这些组件的使用也不需要将框架全部组件都应用，而且用了这些组件也不要求你的系统全部都使用该框架。
- 中文官网：https://cn.vuejs.org/
- 英文官网：https://vuejs.org/
- 参考：https://cn.vuejs.org/v2/guide/
- 作用: 动态构建用户界面  
- 特点：
  - 易用
  - 灵活
  - 高效
- 编码简洁, 体积小, 运行效率高, 适合移动/PC 端开发  
- 它本身只关注 UI, 可以轻松引入 vue 插件或其它第三库开发项目  
- GitHub地址：https://github.com/vuejs
- 作者：[尤雨溪](https://github.com/yyx990803)(一位华裔前 Google 工程师)，Vue.js创作者，Vue Technology创始人，致力于Vue的研究开发。



### 1.3 与其它前端JS框架的关联

- 借鉴 angular 的**模板**和**数据绑定**技术
- 借鉴 react 的**组件化**和**虚拟 DOM** 技术  



### 1.4 Vue扩展插件

- vue-cli: vue 脚手架
- vue-resource(axios): ajax 请求
- vue-router: 路由
- vuex: 状态管理
- vue-lazyload: 图片懒加载
- vue-scroller: 页面滑动相关
- mint-ui: 基于 vue 的 UI 组件库(移动端)
- element-ui: 基于 vue 的 UI 组件库(PC 端)  





## 二、快速入门

搭建示例工程

### 2.1创建工程

创建一个目录，例如：`testVue`



### 2.2 引入Vue

- 使用CDN(使用jsdelivr，也可以到bootcdn中找)

  - 开发版(包含了有帮助的命令行警告)：https://cdn.jsdelivr.net/npm/vue/dist/vue.js
  - 生产版(压缩了，优化了尺寸和速度)：https://cdn.jsdelivr.net/npm/vue

  ```html
  <!-- 引入 -->
  <script src="https://……"></script>
  ```

  

- 下载到本地

  - 下载地址：https://github.com/vuejs/vue
  - 下载release版：https://github.com/vuejs/vue/archive/v2.6.11.zip，解压之后在`dist`目录中可以看到`vue.js`文件

  ```html
  <!-- 引入 -->
  <script src="vue.js"></script>
  ```

  

- **npm安装**(推荐)

  - 进入工程目录：`cd testVue`
  - 初始化项目：`npm init -y`
  - 下载安装Vue：`npm install vue --save`



### 2.3、演示双向绑定与事件处理

需求：创建testVue.html页面并初始化Vue实例，通过console修改Vue数据实现双向绑定效果和创建按钮实现点击自增效果。

- 创建页面，初始化Vue
- `{ {} }`获取显示数据
- `v-model`实现**双向绑定**
- `v-on`演示**事件处理**

在刚刚`testVue`目录中新建`testVue.html`文件，书写代码，测试初始化Vue实例、`{ {} }`使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<!-- 引入vue.js
		1. cdn
		2. 下载后本地引入
		3. npm安装后从node_modules中引入(项目中import引入)
	-->
	<script src="node_modules/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>{{name}}</h2>  <!-- 插值 -->
		<p>渐进式JavaScript框架</p>
	</div>
	<script type="text/javascript">
		/* 创建Vue实例，在里面可以指定一些vue的参数 */
		var app = new Vue({ // 键值对
			el: "#app", // 指定需要渲染的元素
			data:{ // 指定数据
				name: "Vue.js"
			}
		})
	</script>
</body>
</html>
```



在控制台输入命令：

```javascript
app.name="Vue"
```

Vue.js也会变成Vue



测试`v-model`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<input type="text" v-model="num"> <!-- 模型 -->
		<h2>{{name}} 创建 {{num}} 年了</h2>
	</div>
	<script type="text/javascript">
		var app = new Vue({
			el: "#app",
			data:{
				name: "Vue.js",
				num: 5
			}
		})
	</script>
</body>
</html>
```



修改文本框中的值，下面的xx年也会变(模型改变，视图也改变；视图改变也会影响对应的模型)，控制台中也能修改



上面的演示的是双向绑定，下面接着演示事件处理

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<input type="text" v-model="num"> <!-- 模型 -->
		<h2>{{name}} 创建 {{num}} 年了</h2>
		<button v-on:click="num++">num+1</button>
	</div>
	<script type="text/javascript">
		var app = new Vue({ 
			el: "#app",
			data:{
				name: "Vue.js",
				num: 5
			}
		})
	</script>
</body>
</html>
```



点击按钮，num会自增



## 三、Vue实例

在创建Vue实例的时候可以指定模板id、数据和方法；而如果要在实例化、模板渲染的过程中需要执行一些其他操作的话，那么可以使用生命周期钩子函数

### 3.1 创建Vue实例

每个Vue应用都是通过用`Vue`函数创建一个新的**Vue实例**开始的(常用变量vm——ViewModel接收)

```javascript
var vm = new Vue({ // 传入的参数——对象
  // 选项
})
```



在构造函数中传入一个对象，并且在对象中声明各种Vue需要的数据和方法，包括：

- el：指定一个页面元素，受Vue实例的管理，只有被Vue实例管理的元素内部才能使用Vue的语法。

- data：定义Vue实例中使用到的数据，本身就是一个对象，里面的键值对可以随意写。使用时可以直接`vm.msg`使用这个数据(不需要`vm.data.msg`)，在声明周期钩子函数中使用`this.msg`。

- methods：定义Vue实例的一些函数

- computed：计算属性，可以将一些属性数据经过方法处理之后返回。

- watch：监控属性，可以指定一些方法，监控指定的值的变化。

  - 监控简单数据：定义一个和监控的变量名称一致的函数即可，函数的参数为新值和旧值。例如，要监控data中的message，在watch中`message(newValue,oldValue){}`

  - 监控对象中的数据——深度监控：定义一个和监控的对象名称一致的属性，值是一个对象。内部设置deep属性为true代表深度监控开启，回调函数为handler，会传过来新的对象，例如：

    ```javascript
    watch:{
      person: {
        /* 开启深度监控，监控对象中的属性值变化 */
        deep: true,
        // 可以获取到最新的对象属性数据
        handler(obj){
         console.log("姓名：" + obj.name + ",年龄：" + obj.age)
      }
    }
    ```

    

- template

- 声明周期钩子函数名(ES6语法`created: function(){}`简化为`created(){}`)，本质仍是键值对

- ...



### 3.2 模板或元素

每个Vue实例都需要关联一段HTML模板，Vue会基于此模板进行视图渲染；可以通过el属性来指定。

例如一段HTML模板：

```html
<div id="app">

</div>
```



然后创建Vue实例，关联这个div

```javascript
var vm = new Vue({
  el: "#app"
})
```



这样，Vue就可以基于id为app的div元素作为模板进行渲染了，在这个div范围以外的部分是无法使用vue特性的。



### 3.3 数据

当Vue实例被创建时，它会尝试获取在data中定义的所有属性，用于视图的渲染，并且**监视**data中的属性变化，当data发生改变，所有相关的视图都将重新渲染，这就是“响应式”系统。

例如在HTML中模型指定name

```html
<div id="app">
  <input type="text" v-model="name" />
</div>
```



js中vue的data属性设置一个name

```javascript
var vm = new Vue({
  el: "#app",
  data:{
    name: "Vue.js"
  }
})
```



- name的变化会影响到input的值
- input中输入的值，也会导致vm中的name发生改变



### 3.4 方法

Vue实例中除了可以定义data属性，也可以定义方法，并且在Vue的作用范围内使用。

例如HTML模板中指定v-on事件click之后执行的代码(可以是一个语句也可以是个函数)

```html
<div id="app">
  <button v-on:click="add">add</button>
</div>
```



在创建实例时到methods属性中定义add方法

```javascript
var vm = new Vue({
  el: "#app",
  data:{},
  methods:{
    add: function(){
      console.log("add被点击了")
    }
  }
})
```



### 3.5 声明周期及钩子函数

#### 3.5.1 声明周期

> 每个Vue实例在被创建时都要经过一系列的初始化过程——创建实例、装载模板、渲染模板等，Vue为生命周期中的每个状态都设置了钩子函数(监听函数)，每当Vue实例处于不同的声明周期时，对应的函数就会被触发调用。

所有的生命周期钩子自动绑定`this`上下文到实例中，因此你可以访问数据，对属性和方法进行运算。这意味着你**不能使用箭头函数来定义一个声明周期方法**(比如 `created: () => console.log(this.a)` 或 `vm.$watch('a', newValue => this.myMethod())`)，因为箭头函数的 `this`与你期待的Vue实例不同，`this` 会作为变量一直向上级词法作用域查找，直至找到为止，经常导致 `Uncaught TypeError: Cannot read property of undefined` 或 `Uncaught TypeError: this.myMethod is not a function` 之类的错误。

声明周期：

![](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827121350.png)

实例化——>挂载——>销毁    (如果使用构建步骤，模板编译会提前执行，例如单文件组件)

钩子函数会在Vue实例的各个声明周期阶段自动调用，具体有：

(1) 初始化显示：

- `beforeCreate`：在实例初始化之后，数据观测(data observer)和event/watcher事件配置之前被调用。
- **`created`**：在实例创建完成后被立即调用。在这一步，实例已完成以下的配置：数据观测(data observer)，属性和方法的运算，watch/event事件回调。然而，挂载阶段还没开始，$el属性目前不可见。
- `beforeMount`：在挂载开始之前被调用。相关的render函数首次被调用。
- **`mounted`**：el被新创建的`vm.$el`替换，并挂载到实例上去之后调用该钩子。如果root实例挂载了一个文档内元素。当mounted被调用时`vm.$el`也在文档内。[vm.$el：Vue实例使用的根DOM元素]

(2) 更新状态：(`this.xxx=value`)

- `beforeUpdate`：数据更新时调用，发生在虚拟DOM打补丁之前，这里适合在更新之前访问现有的DOM，比如手动移除已添加的事件监听器。
- `updated`：由于数据更改导致的虚拟DOM重新渲染和打补丁，在这之后会调用该钩子。当这个 钩子被调用时，组件DOM已经更新，所以此时可以执行依赖于DOM的操作。然而在大多数情况下，应该避免在此期间更改状态，如果要相应状态改变，通常最好使用计算属性或watcher取而代之。

(3) 销毁Vue实例：(`vm.$destory()`)

- **`beforeDestroy`**：实例在销毁之前调用。在这一步，实例仍然完全可用。
- `destroyed`：Vue实例销毁后调用。调用后，Vue实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。

[vm.$root：当前组件树的根Vue实例，如果当前实例没有父实例，此实例将会是其自己]



#### 3.5.2 钩子函数

例如：created代表在Vue实例创建后

可以在Vue中定义一个created函数，代表这个时期的构造函数：

创建页面`vueLifCycle.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js声明周期钩子created测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>{{msg}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				msg: ""
			},
			// 钩子函数
			created(){
				this.msg = "Hello Vue.js created"
				console.log(this)
			}
		})
	</script>
</body>
</html>
```



created常用于**数据的初始化**，即发送ajax，获取后台数据，给data属性中的数据进行赋值，接着在模板中应用数据，视图也会发生改变，从而实现数据的异步加载。

mounted发送 ajax 请求, 启动定时器等异步任务  

beforeDestory做收尾工作, 如: 清除定时器  



#### 3.5.3 this

打印的this(这个Vue实例对象)如下：

![image-20200827155038198](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827155040.png)





## 四、指令

指令(Directives)是带有`v-`前缀的特殊属性。例如在入门案例中的v-model，代表双向绑定。

### 4.1 插值表达式

#### 4.1.1 大括号

- 格式：`{{表达式}}`

- 说明：
  - 该表达式支持**JS语法**，可以调用js内置函数(必须有**返回值**)
  - 表达式必须有返回结果。例如`1+1`，没有结果的表达式不允许使用，如`var a = 1 + 1`
  - 可以直接获取Vue实例data中定义的**数据或函数**
  - 可以直接写`""`
- 示例：

````html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js插值表达式测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>{{msg}}</h2>
    <h2>{{"说的没错"}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				msg: "Vue.js 轻便好用"
			}
		})
	</script>
</body>
</html>
````



#### 4.1.2 ~~插值闪烁~~

使用`{ {} }`方式在网速较慢的时候会出现问题，在数据未加载完成时，页面会显示出原始的`{{表达式}}`，加载完毕后才显示正确数据，这种情况称为插值闪烁(在最新的Vue中几乎没有这个问题)。

在以前版本中，出现插值闪烁，可以使用v-text、v-html解决。



#### 4.1.3 v-text和v-html

- 使用v-text和v-html指令来代替`{ {} }`

- 说明：
  - `v-text`：将数据输出到元素内部，如果输出的数据有HTML代码，会作为普通文本输出
  - `v-html`：将数据输出到元素内部，如果输出的数据有HTML代码，会被渲染
- 示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js v-html/v-text测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2 v-text="msg"></h2>
		<h2 v-html="msg"></h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				msg: "<span style='color: red;'>Vue.js 很好用</span>"
			}
		})
	</script>
</body>
</html>
```



![image-20200827164954008](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827164955.png)



**插值**可以使用在需要显示Vue实例数据的地方，可以在插值表达式中调用实例的属性和函数。

v-text和v-html的作用：可以将数据在模板中进行显示；区别：**v-html**会对内容中出现的HTML标签进行渲染，而**v-text**会将内容当作普通文本输出到元素里面。(有点像js中的innerHTML和innerText)



### 4.2 v-model

刚才的v-text和v-html可以看做是**单向绑定**，数据影响了视图渲染，但是反过来就不行。接下来的v-model就是**双向绑定**的了，视图(View)和模型(Model)之间会相互影响。

既然是双向绑定，一定是在视图中可以修改数据，这样就限定了视图的元素类型。目前v-model可以使用的元素有：

- input
- select
- textarea
- checkbox
- radio
- components(Vue中的自定义组件)

基本上除了最后一项，其它都是表单的输入项。

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js v-model测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<label><input type="checkbox" value="C/C++" v-model="language" />C/C++ </label><br>
		<label><input type="checkbox" value="Java" v-model="language" />Java </label><br>
		<label><input type="checkbox" value="PHP" v-model="language" />PHP </label><br>
		<h2>你选择了：{{language.join(", ")}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				language: []
			}
		})
	</script>
</body>
</html>
```



![demo](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827182301.gif)

- 多个`checkbox`对应一个model时，model的类型是一个**数组**，单个checkbox值是**boolean类型**
- `radio`对应的值是input的**value值**
- `input`和`textarea`默认对应的model是**字符串**
- `select`单选对应**字符串**，多选对应也是**数组**



补充：插件Vue.js devtools

https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?utm_source=chrome-ntp-icon



### 4.3 v-on

#### 4.3.1 基本用法

在没有使用Vue之前，页面标签可以通过设置onXXX响应事件；在Vue中可以通过v-on指令响应事件(**给页面元素绑定事件**)。

语法：`v-on:事件名="js片段或函数名"`

简写语法：`@事件名="js片段或函数名"`

例如`v-on:click="add"`可以简写为`@click="add"`

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js v-on测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<button v-on:click="num++">增加</button>
		<button @click="decrement">减少</button>
		<h2>num的数值为 {{num}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				num: 1
			},
			methods: {
				decrement: function(){
					this.num--
				}
			},
		})
	</script>
</body>
</html>
```



![on](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827184155.gif)



默认事件形参: `event`
隐含属性对象: `$event`



#### 4.3.2 事件修饰符

在事件处理程序中调用`event.preventDefault()`或`event.stopPropagation()`是非常常见的需求(阻止默认事件)。尽管我们可以在方法中轻松实现这点，但方法只有纯粹的数据逻辑，而不是去处理DOM事件细节。

为了解决这个问题，Vue.js为`v-on`提供了**事件修饰符**。修饰符是由点开头的指令后缀来表示的。

语法：`v-on:事件名.修饰符="js片段或函数名"` 或 `@事件名.修饰符="js片段或函数名"`

常用修饰符：

- **`.stop`**：阻止事件冒泡
  - 事件冒泡：默认情况下，在某个页面元素上触发的事件，在当前元素处理完之后会自动传递给祖先元素，祖先的相同事件也会执行
- **`.prevent`**：阻止默认事件发生
  - 浏览器默认的一些事件行为，例如：
    - 获取焦点事件会把光标放入输入框
    - 表单提交事件会提交数据到action指定的url
    - 点击a标签会跳转到href指定的地址
- `.capture`：使用事件捕获模式
  - 相当于和冒泡相反，父元素先于子元素获取事件
- `.self`：只有元素自身触发事件才执行(冒泡或捕获的都不执行)
- `.once`：只执行一次

冒泡测试：

````html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>事件冒泡测试</h2>
		<div v-on:click="print('点击了div')" style="background: skyblue; width: 400px; height: 400px;">
			<button @click="print('点击了button')">按钮</button>
		</div>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				num: 1
			},
			methods: {
				print(str){
					console.log(str)
				}
			},
		})
	</script>
</body>
</html>
````

![bubble](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827190036.gif)



阻止冒泡：

```html
<div id="app">
	<h2>阻止事件冒泡测试</h2>
	<div v-on:click="print('点击了div')" style="background: skyblue; width: 400px; height: 400px;">
		<button @click.stop="print('点击了button')">按钮</button>
	</div>
</div>
```

![stopbubble](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827190024.gif)



阻止默认事件：点击超链接不会跳转

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>阻止默认事件</h2>
		<a href="https://www.baidu.com" @click.prevent="print('点击了a')">百度</a>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				num: 1
			},
			methods: {
				print(str){
					console.log(str)
				}
			},
		})
	</script>
</body>
</html>
```



#### 4.3.3 按键修饰符

- `.keycode` : 操作的是某个 keycode 值的键
- `.keyName` : 操作的某个按键名的键(少部分)  

```html
<h2>3. 按键修饰符</h2>
<input @keyup.8="test"> <!-- 按键8 -->
<input @keyup.enter="test"> <!-- 按键enter -->
<script type="text/javascript" src="../js/vue.js"></script>
<script type="text/javascript">
new Vue({
  el: '#example',
  data: {
  	name: 'Vue.js'
  },
  methods: {
    test(event) {
  		alert(event.keyCode + '---' + event.target.value)
  	}
  }
})
</script>
```





### 4.4 v-for

可以在Vue实例化的时候指定要遍历的数据，然后通过v-for指令在模板中遍历显示数据。一般情况下，要遍历的数据可以通过钩子函数created发送异步请求获取数据。

#### 4.4.1 遍历数组

- 语法：`v-for="item in items"`
  - items：要遍历的数组名或对象名，需要在Vue的data中定义好。
  - item：循环遍历
- 示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<ul>
			<li v-for="user in users">
				我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
			</li>
		</ul>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				users:[
					{"name":"唐僧","age":24,"gender":"男"},
					{"name":"孙悟空","age":26,"gender":"男"},
					{"name":"猪八戒","age":30,"gender":"男"},
					{"name":"沙和尚","age":32,"gender":"男"},
					{"name":"蜘蛛精","age":18,"gender":"女"}
				]
			}
		})
	</script>
</body>
</html>
```



![image-20200827200311325](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827200312.png)



#### 4.4.2 数组角标

在遍历的过程中，如果需要知道数组角标/索引号，可以指定第二个参数

- 语法：`v-for="(item,index) in items"`
  - items：要遍历的数组
  - item：遍历得到的数组元素别名
  - index：遍历到的当前元素索引，从0开始
- 示例：

```html
<div id="app">
	<ul>
		<li v-for="(user, index) in users">
			{{index}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
		</li>
	</ul>
</div>
```



![image-20200827200727402](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827200728.png)



#### 4.4.3 遍历对象

v-for除了可以迭代数组，也可以迭代对象，语法基本类似

语法：

```
v-for="value in object"
v-for="(value,key) in object"
v-for="(value,key,index) in object"
```



- 1个参数时，得到的是对象的值
- 2个参数时，第一个是值，第二个是键
- 3个参数时，第三个是索引，从0开始

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<ul>
			<li v-for="(value, key, index) in person">
				{{index}}——{{key}}——{{value}}
			</li>
		</ul>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				person:{"name":"孙悟空","age":26,"gender":"男","address":"花果山"}
			}
		})
	</script>
</body>
</html>
```



![image-20200827201525393](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200827201526.png)



#### 4.4.4 key

当Vue.js用`v-for`正在更新已渲染过的元素列表时，它默认用”就地复用”策略。如果数据项的顺序被改变,，Vue 将不会移动DOM元素来匹配数据项的顺序，而是简单复用此处每个元，并且确保它在特定索引下显示已被渲染过的每个元素。
如果使用key这个功能可以有效的提高渲染的效率; key一般使用在遍历完后，还要增、减集合元素的时候更有意义。
但是要实现这个功能，你需要给Vue-些提示，以便它能跟踪每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一key 属性。理想的`key`值是每项都有的且唯一的id。也就是key是该项的唯一标识。

示例：

```html
	<ul>
		<li v-for="(user, index) in users" :key="index">
			{{index}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
		</li>
	</ul>
```



这里使用了一个特殊的语法：`:key=""`，它可以读取Vue中的属性，并赋值给key属性

这里绑定的key是数组的索引，是唯一的(以后可以加其他的唯一的数据，例如user.id)



### 4.5 v-if和v-show

#### 4.5.1 基本使用

v-if，条件判断，当得到的结果为true时，所在的元素才会被渲染。

语法：`v-if="布尔表达式"`

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<button @click="show=!show">按钮</button>
		<h2 v-if="show">Hello Vue.js</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				show: true
			}
		})
	</script>
</body>
</html>
```



#### 4.5.2 与v-for结合

当v-if和v-for一起出现的时候，v-for优先级更高，即会先遍历，再判断条件。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>女性人物</h2>
		<ul>
			<li v-for="(user, index) in users" v-if="user.gender=='女'">
				{{index}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
			</li>
		</ul>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				users:[
					{"name":"唐僧","age":24,"gender":"男"},
					{"name":"孙悟空","age":26,"gender":"男"},
					{"name":"猪八戒","age":30,"gender":"男"},
					{"name":"沙和尚","age":32,"gender":"男"},
					{"name":"蜘蛛精","age":18,"gender":"女"}
				]
			}
		})
	</script>
</body>
</html>
```



#### 4.5.3 v-else

可以使用`v-else`指令来表示`v-if`的“else块”，需要注意，v-else元素必须紧跟在带有v-if或v-else-if的元素的后面，否则它将不会被识别(两者之间不能插入其他元素)

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>西游人物</h2>
		<ul>
			<li v-for="(user, index) in users" v-if="user.gender=='女'" style="color:pink;">
				{{index+1}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
			</li>
			<li v-else style="color:skyblue;">
				{{index+1}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
			</li>
		</ul>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				users:[
					{"name":"唐僧","age":24,"gender":"男"},
					{"name":"孙悟空","age":26,"gender":"男"},
					{"name":"猪八戒","age":30,"gender":"男"},
					{"name":"沙和尚","age":32,"gender":"男"},
					{"name":"蜘蛛精","age":18,"gender":"女"}
				]
			}
		})
	</script>
</body>
</html>
```



`v-else-if`，充当`v-if`的”else-if块“，可以连续使用(v-else-if也必须紧跟在带v-if或v-else-if的元素后)

```html
<div id="app">
	<h2>西游人物</h2>
	<ul>
		<li v-for="(user, index) in users" v-if="user.age<20" style="color:yellowgreen;">
			{{index+1}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
		</li>
		<li v-else-if="user.age<30" style="color:skyblue;">
			{{index+1}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
		</li>
		<li v-else style="color:yellow;">
			{{index+1}}：我是{{user.name}}，今年{{user.age}}岁了，性别{{user.gender}}
		</li>
	</ul>
</div>
```



#### 4.5.4 v-show

`v-show`也可以根据条件是否展示元素，例如：

````html
<h1 v-show="ok">Hello Vue.js.</h1>
````



但是，带有`v-show`的元素始终会被渲染并保留在DOM中，`v-show`只是简单地切换元素的CSS属性`display`的值。

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<button @click="show=!show">切换</button>
		<h2 v-if="show">Vue.js</h2>
		<h2 v-show="show">Vue.js</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				show: true
			}
		})
	</script>
</body>
</html>
```



![image-20200828082250681](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200828082251.png)

`v-if`在条件不满足的时候元素会消失；`v-show`条件不满足的时候只是`display:none`了



### 4.6 v-bind

#### 4.6.1 属性上使用vue数据

插值表达式不能用在属性中，会报错`<div id="box" class="{{bgcolor}}">点击按钮改变背景颜色</div>`

v-bind作用：可以对所有元素的属性值设置为vue中data的数据

语法：在属性名之前加上`v-bind:`(`v-bind:属性名='Vue中的变量'`)，简写为`:属性名='属性值'`

`<img src="" height="" />`其中src和height的值如果不想写死，而是想获取Vue实例中的数据属性值的话，那么可以通过使用v-bind实现

```html
<img v-bind:src="vue实例中的数据属性名" :height="vue实例中的数据属性名" />
```



利用v-bind实现点击切换背景颜色

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
	<style>
		#box{
			width: 150px;
			height: 150px;
			color: white;
		}
		.red{
			background-color: red;
		}
		.green{
			background-color: green;
		}
	</style>
</head>
<body>
	<div id="app">
		<button @click="bgcolor='red'">切换红色</button>
		<button @click="bgcolor='green'">切换绿色</button>
		<br><br>
		<div id="box" v-bind:class="bgcolor">点击按钮改变背景颜色</div>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				bgcolor: "red"
			}
		})
	</script>
</body>
</html>
```



#### 4.6.2 class属性的特殊用法

上面虽然实现了颜色切换，但是比较麻烦。

Vue对class属性进行了特殊处理，可接受数组或对象格式

对象语法：

可以传给`:class`一个对象，用于动态切换class：

```html
<div :class="{red: true, green: false}"></div>
```



- 对象中，key是已经定义的class样式的名称，比如上面的`red`、`green`
- 对象中，value是一个布尔值，如果为true，则这个样式会生效，如果为false，则不生效。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
	<style>
		#box{
			width: 150px;
			height: 150px;
			color: white;
		}
		.red{
			background-color: red;
		}
		.green{
			background-color: green;
		}
	</style>
</head>
<body>
	<div id="app">
		<button @click="bool=!bool">切换颜色</button>
		<br><br>
		<div id="box" v-bind:class="{red: bool, green: !bool}">点击按钮改变背景颜色</div>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				bgcolor: "red",
				bool: true
			}
		})
	</script>
</body>
</html>
```



### 4.7 计算属性

在插值表达式中使用js表达式是非常方便的，而且也经常被用到。

但是如果表达式的内容很长，就会显得不够优雅，而且后期维护起来也不方便。

例如，将一个日期的毫秒值显示转为格式化的yyyy-MM-dd：

````html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>日期：{{new Date(date).getFullYear()}}-{{new Date(date).getMonth()+1}}-{{new Date(date).getDate()}}</h2> <!-- 日期：2020-8-28 -->
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				date: 1598580451457 // 毫秒值
			}
		})
	</script>
</body>
</html>
````



这样利用js的方法能够实现需求，但是很麻烦。

Vue中提供了计算属性，来替代复杂的表达式：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<h2>日期：{{new Date(date).getFullYear()}}-{{new Date(date).getMonth()+1}}-{{new Date(date).getDate()}}</h2>
		<hr>
		<h2>computed,日期：{{getDay}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				date: 1598580451457 // 毫秒值
			},
			computed: {
				getDay(){
					const date = new Date(this.date)
					return date.getFullYear() + "-" + (date.getMonth()+1) + "-" + date.getDate()
				}
			}
		})
	</script>
</body>
</html>
```



computed计算属性可以应用在插值或者指令表达式复杂的时候，它可以将一些属性数据经过方法处理之后返回。



### 4.8 watch

#### 4.8.1 监控

在vue实例中，数据属性因为在页面中修改而产生了变化，可以通过watch监控获取其改变前后的值。

watch使用场景：可以监控视图中的数据变化从而做出相应的反应，例如，下拉列表中，如果选择了对应的下拉列表选项之后，要根据最新的值去加载一些其他数据。



#### 4.8.2 深度监控

如果是修改的对象数据属性，可以开启深度监控获取修改后最新的对象数据。



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<input type="text" v-model="message">
		<br><hr>
		<input type="text" v-model="person.name">
		<input type="text" v-model="person.age">
		<button @click="person.age++">年龄+1</button>
		<h2>姓名：{{person.name}}，年龄：{{person.age}}</h2>
	</div>
	<script type="text/javascript">
		var vm = new Vue({
			el: "#app",
			data:{
				message: "你好啊！",
				person:{
					name: "张三",
					age: 21
				}
			},
			watch: {
				message(newValue, oldValue){
					console.log("新值："+ newValue +"，旧值：" + oldValue)
				},
				person: {
					/* 开启深度监控，监控对象中的属性值变化 */
					deep: true,
					// 可以获取到最新的对象属性数据
					handler(obj){
						console.log("姓名：" + obj.name + ",年龄：" + obj.age)
					}
				}
			},
		})
	</script>
</body>
</html>
```



## 五、组件化

在大型应用开发的时候，页面可以划分成很多部分。

但是如果每个页面都独自开发，无疑会增加开发的成本，因此会把页面的不同部分拆分成独立的组件，然后再不同的页面共享这些组件，避免重复开发。

### 5.1 定义全局组件

通过Vue的component方法来定义一个全局组件。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<!-- 引入组件(使用) -->
		<counter />
	</div>
	<script type="text/javascript">
		// 定义组件
		const counter = {
			// el 组件不需要el绑定一个具体的元素
			template: "<button @click='num++'>你点击了{{num}}次</button>",
			data() {
				return {
					num: 0
				}
			} // data只能是一个函数，并且有返回
			/* data: {
				num: 0
			} */
		}
		// 全局注册组件：在所有的vue实例中都可以使用组件
		Vue.component("counter", counter) // 参数1：组件内名称，参数2：具体的组件
		var vm = new Vue({
			el: "#app"
		})
	</script>
</body>
</html>
```



- 组件其实也是一个Vue实例，因此它在定义时也会接收data、methods、生命周期函数等

- 不同的是，组件不会与页面的元素绑定，否则就无法复用了，因此没有el属性

- 但是组件渲染需要hmtl模板，所以添加了template属性，值就是HTML模板

- 全局组件定义完毕，任何Vue实例都可以直接在HTML中通过组件名称来使用该组件

- data的定义方式比较特殊，必须是一个函数



### 5.2 组件的复用

定义好的组件，可以任意复用多次：

```html
<div id="app">
	<!-- 引入组件(使用) -->
	<counter></counter>
	<counter></counter>
	<counter></counter>
</div>
```



![image-20200828121651862](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200828121653.png)

每个组件互不干扰，有自己的num值，这是因为

**组件的data属性必须是函数**

当定义这个组件的时候，它的data并不是像这样直接提供一个对象：

```javascript
data:{
	num: 0
}
```



而必须是一个函数，因此每个实例可以维护一分被返回对象的独立的拷贝

```javascript
data: function() {
  return {
    num: 0
  }
}
```



如果Vue没有这条规则，点击一个按钮就会影响到其他所有实例



### 5.3 局部注册

一旦全局注册，就意味着即便以后不再使用这个组件，它依然会随着Vue的加载而加载。因此，对于一些使用并不频繁的组件，会采用局部注册。

先在外部定义一个对象，结构与创建组件时传递的第二个参数一致，然后再Vue中使用它：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<!-- 引入组件(使用) -->
		<counter></counter>
		<counter></counter>
		<counter></counter>
	</div>
	<script type="text/javascript">
		// 定义组件
		const counter = {
			// el 组件不需要el绑定一个具体的元素
			template: "<button @click='num++'>你点击了{{num}}次</button>",
			data() {
				return {
					num: 0
				}
			} // data只能是一个函数，并且有返回
		}
		// 全局注册组件：在所有的vue实例中都可以使用组件
		/* Vue.component("counter", counter) */ // 参数1：组件内名称，参数2：具体的组件
		var vm = new Vue({
			el: "#app",
			// 局部注册组件
			components:{
				counter: counter // 组件名: 具体的某个组件
			}
		})
	</script>
</body>
</html>
```



- components就是当前vue对象子组件集合
  - 其key就是子组件名称
  - 其值就是组件对象的属性
- 效果与全局注册时一样的，但是这个局部注册的counter组件只能在当前的Vue实例中使用



组件使用场景：在项目需要重用某个模块(头部、尾部、内容……)的时候，可以将模块抽取成组件，其他页面中注册组件并引用。

全局注册：在任何Vue实例中都可以引用，如：网站的头部导航菜单

局部注册：可以在有需要的页面引入组件，如：商城网站首页页面中各种活动模块



### 5.4 组件通信

通常一个单页面应用会以一颗嵌套的组件树的形式来组织：

![img](https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/pic/illustrtion/20200828155751.png)

- 页面首先分为了顶部导航、左侧内容区、右侧边栏三个部分
- 左侧内容区又分为上下两个组件
- 右侧边栏中包含了3个子组件

各个组件之间以嵌套的关系组合在一起，那么这个时候不可避免地会有组件间通信的需求。

#### 5.4.1 父向子传递 props

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<introduce :title="msg"></introduce>
	</div>
	<script type="text/javascript">
		const introduce = {
			template:"<h2>{{title}}</h2>",
			// 定义接收父组件的属性
			props:["title"]
		}
		Vue.component("introduce", introduce)
		var vm = new Vue({
			el: "#app",
			data:{
				msg:"父组件的msg属性数据内容"
			}
		})
	</script>
</body>
</html>
```



introduce这个子组件中要使用title属性渲染页面，但是自己并没有title属性。通过props来接收父组件属性，名为title。父组件使用子组件，同时传递title属性。





#### 5.4.2 传递复杂数据



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		<my-list :items="lessons"></my-list> <!-- 这里就不能用驼峰命名法了 -->
	</div>
	<script type="text/javascript">
		const myList = {
			template:`
				<ul>
					<li v-for="item in items" :key="item.id">{{item.id}}——{{item.name}}</li>
				</ul>
			`, // 这里用的是模板字符串，也可以用双引号、单引号
			props:{ // 通过props来接收父组件传递来的属性
				items:{ // 这里定义items属性
					// 数据类型，如果是数组则是Array，如果是对象则是Object
					type:Array,
					// 默认值(如果父组件没有传值，那么就是一个空数组)
					default:[]
				}
			}
		}
		var vm = new Vue({
			el: "#app",
			data:{
				msg:"父组件的msg属性数据内容",
				lessons:[
					{"id":1, "name":"语文"},
					{"id":2, "name":"数学"},
					{"id":3, "name":"英语"},
					{"id":4, "name":"物理"},
					{"id":5, "name":"化学"},
					{"id":6, "name":"生物"}
				]
			},
			components:{
				myList // ES6语法
			}
		})
	</script>
</body>
</html>
```



- 这个子组件可以对items进行迭代，并输出到页面

- 但是组件中并没有定义items属性

- 可以通过props来定义需要从父组件中接收的属性

  - items：要接收的属性名称

    - type：限定父组件传递来的必须是数组，否则报错[type的值可以是Array或者Object，传递对象的时候使用]

    - default：默认值，如果是对象则需要写成方法的方式返回默认值，如：

      ```
      default(){
      	return {"xxx":"默认值"}
      }
      ```

      



#### 5.4.3 子向父的通信

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Vue.js测试</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
	<div id="app">
		num = {{num}}
		<counter @plus="numPlus" @reduce="numReduce()" :snum="num"></counter>
	</div>
	<script type="text/javascript">
		const counter = {
			template:`
				<div> 
					<button @click='incrNum'>增加</button>
					<button @click='decrNum'>减少</button>
				</div>
			`,/* 只能是一个容器包裹多个元素 */
			props:["snum"],
			methods: {
				incrNum(){
					// 调用到父组件中的方法
					return this.$emit("plus")
				},
				decrNum(){
					// 调用到父组件中的方法
					return this.$emit("reduce")
				}
			},
		}
		Vue.component("counter", counter)
		var vm = new Vue({
			el: "#app",
			data:{
				num: 0
			},
			methods: {
				numPlus(){
					this.num++
				},
				numReduce(){
					this.num--
				}
			}
		})
	</script>
</body>
</html>
```



实现了在子组件中点击对应按钮，父组件中属性数据的改变

子组件绑定自定义事件，在子组件中通过`$emit`触发这个事件，去调用执行外界父组件传递过来的函数操作，函数调用时可以传递参数，从而间接地传递数据给父组件。(父组件给子组件传递一个函数，然后子组件调用此函数，调用时可以传参，函数执行时，实际执行的是父组件中的逻辑，从而可以拿到子组件传参过来的数据)

`$emit`可以传值，`this.$emit("自定义事件名",要传的数据)`，接着会在父组件中以方法的参数传过去



## 六、Vuejs ajax

Vuejs并没有直接处理ajax的组件，但可以使用axios或vue-resource组件实现对异步请求的操作。

### 6.1 vue-resource

vue-resource是Vue.js的插件，提供了使用XMLHttpRequest或JSONP进行web请求和处理响应的服务。当Vue更新到2.0之后，作者就宣告不再对vue-resource更新，而是推荐使用axios。

GitHub地址：https://github.com/pagekit/vue-resource

### 6.2 axios简介

axios是一个基于promise的HTTP库，可以用在浏览器和Node.js中。

GitHub地址：https://github.com/axios/axios

```sh
# npm 安装
npm install axios
```



也可以直接使用cdn服务：

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```



### 6.3 axios应用

#### 6.3.1 方法说明

axios可以使用的方法有：

- `axios(config)`
- `axios.get(url[,config])`
- `axios.delete(url[,config])`
- `axios.head(url[,config])`
- `axios.post(url[,data[,config]])`
- `axios.put(url[,data[,config]])`
- `axios.patch(url[,data[,config]])`

1、config请求配置

这些是创建请求时可以用的配置选项。只有`url`是必须的，如果没有指定`method`，请求将默认使用`get`方法。

```javascript
{
  // url是用于请求的服务器URL
  url: '/user',
    
  // method是创建请求时使用的方法
  method: 'get', // 默认是get方式

  // baseURL将自动加在url的前面，除非url是一个绝对URL。
  // 它可以通过设置一个baseURL，便于为axios实例的方法传递相对URL。
  baseURL: 'https://some-domain.com/api/',

  // transformRequest允许在将请求数据发送到服务器之前对数据进行修改
  // 只能用在'PUT'、'POST'、'PATCH' and 'DELETE'这些请求方法
  // 数组中的最后一个函数必须返回字符串或Buffer，ArrayBuffer，FormData或Stream的实例
  // You may modify the headers object.
  transformRequest: [function (data, headers) {
    // 对data进行任意转换处理

    return data;
  }],

  // transformResponse在传递给then/catch前，运行修改响应数据
  transformResponse: [function (data) {
    // 对data进行任意转换处理

    return data;
  }],

  // headers是即将被发送的自定义请求头
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json'
  },

  // params是即将与请求一起发送的URL参数
  // 必须是一个无格式对象(plain object)或URLSearchParams对象
  params: {
    ID: 12345
  },

  // paramsSerializer是用于序列化params的可选功能(e.g. https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)
  paramsSerializer: function (params) {
    return Qs.stringify(params, {arrayFormat: 'brackets'})
  },

  // data是作为请求主体被发送的数据
  // 只适用于'PUT'、'POST'、'DELETE'和'PATCH'请求方法
  // 在没有设置transformRequest时, 必须是一下类型之一:
  // - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams
  // - 浏览器专属: FormData, File, Blob
  // - Node专属: Stream, Buffer
  data: {
    firstName: 'Fred'
  },
  
  // syntax alternative to send data into the body
  // method post
  // only the value is sent, not the key
  data: 'Country=Brasil&City=Belo Horizonte',

  // timeout指定请求超时的毫秒数(0表示无超时时间)
  // 如果请求花费超过timeout的时间, 请求将被中断
  timeout: 1000, // 默认是`0` (no timeout)

  // withCredentials表示跨域请求时是否需要凭证
  withCredentials: false, // 默认是false

  // adapter` allows custom handling of requests which makes testing easier.
  // Return a promise and supply a valid response (see lib/adapters/README.md).
  adapter: function (config) {
    /* ... */
  },

  // `auth` indicates that HTTP Basic auth should be used, and supplies credentials.
  // This will set an `Authorization` header, overwriting any existing
  // `Authorization` custom headers you have set using `headers`.
  // Please note that only HTTP Basic auth is configurable through this parameter.
  // For Bearer tokens and such, use `Authorization` custom headers instead.
  auth: {
    username: 'janedoe',
    password: 's00pers3cret'
  },

  // responseType表示服务器响应的数据类型，可以是'arraybuffer', 'document', 'json', 'text', 'stream'
  // 浏览器专属: 'blob'
  responseType: 'json', // 默认是json

  // responseEncoding` indicates encoding to use for decoding responses (Node.js only)
  // Note: Ignored for `responseType` of 'stream' or client-side requests
  responseEncoding: 'utf8', // default

  // `xsrfCookieName` is the name of the cookie to use as a value for xsrf token
  xsrfCookieName: 'XSRF-TOKEN', // default

  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'X-XSRF-TOKEN', // default

  // `onUploadProgress` allows handling of progress events for uploads
  // browser only
  onUploadProgress: function (progressEvent) {
    // Do whatever you want with the native progress event
  },

  // `onDownloadProgress` allows handling of progress events for downloads
  // browser only
  onDownloadProgress: function (progressEvent) {
    // Do whatever you want with the native progress event
  },

  // maxContentLength定义运行的响应内容的最大尺寸
  maxContentLength: 2000,

  // `maxBodyLength` (Node only option) defines the max size of the http request content in bytes allowed
  maxBodyLength: 2000,

  // validateStatus` defines whether to resolve or reject the promise for a given HTTP response status code. 如果validateStatus返回true(或者设置为null或undefined), promise将被resolved; 否则promise将被rejected.
  validateStatus: function (status) {
    return status >= 200 && status < 300; // 默认是200~300
  },

  // maxRedirects定义在node.js中执行重定向的最大数目
  // 如果设置为0，将不执行任何重定向。
  maxRedirects: 5, // 默认是5

  // `socketPath` defines a UNIX Socket to be used in node.js.
  // e.g. '/var/run/docker.sock' to send requests to the docker daemon.
  // Only either `socketPath` or `proxy` can be specified.
  // If both are specified, `socketPath` is used.
  socketPath: null, // default

  // `httpAgent` and `httpsAgent` define a custom agent to be used when performing http
  // and https requests, respectively, in node.js. This allows options to be added like
  // `keepAlive` that are not enabled by default.
  httpAgent: new http.Agent({ keepAlive: true }),
  httpsAgent: new https.Agent({ keepAlive: true }),

  // `proxy` defines the hostname and port of the proxy server.
  // You can also define your proxy using the conventional `http_proxy` and
  // `https_proxy` environment variables. If you are using environment variables
  // for your proxy configuration, you can also define a `no_proxy` environment
  // variable as a comma-separated list of domains that should not be proxied.
  // Use `false` to disable proxies, ignoring environment variables.
  // `auth` indicates that HTTP Basic auth should be used to connect to the proxy, and
  // supplies credentials.
  // This will set an `Proxy-Authorization` header, overwriting any existing
  // `Proxy-Authorization` custom headers you have set using `headers`.
  proxy: {
    host: '127.0.0.1',
    port: 9000,
    auth: {
      username: 'mikeymike',
      password: 'rapunz3l'
    }
  },

  // `cancelToken` specifies a cancel token that can be used to cancel the request
  // (see Cancellation section below for details)
  cancelToken: new CancelToken(function (cancel) {
  }),

  // `decompress` indicates whether or not the response body should be decompressed 
  // automatically. If set to `true` will also remove the 'content-encoding' header 
  // from the responses objects of all decompressed responses
  // - Node only (XHR cannot turn off decompression)
  decompress: true // default

}
```



2、响应结构

```javascript
{
  // data是由服务器提供的响应数据
  data: {},

  // status是来自服务器响应的HTTP状态码
  status: 200,

  // statusText服务器响应的HTTP状态信息
  statusText: 'OK',

  // headers是服务器响应的头，服务器使用所有标头名称响应的HTTP标头均使用小写字母，并且可以使用方括号表示法进行访问。
  // 例如: `response.headers['content-type']`
  headers: {},

  // config是为请求提供给axios的配置
  config: {},

  // `request` is the request that generated this response
  // It is the last ClientRequest instance in node.js (in redirects)
  // and an XMLHttpRequest instance in the browser
  request: {}
}
```



使用`then`时，将会收到如下响应：

```javascript
axios.get('/user/12345')
  .then(function (response) {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
```



当使用`catch`或将[拒绝回调](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)作为`then`的第二个参数传递时，响应将通过`error`对象提供，如“[处理错误](https://github.com/axios/axios#handling-errors)”部分所述。



#### 6.3.2 axios方法示例



#### 6.3.3 get方法示例



#### 6.3.4 post方法示例













