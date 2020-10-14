---
title: ES和模块化学习笔记
author: luwang
avatar: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/custom/avatar.jpg'
authorLink: wallleap.cn
tags:
  - 前端
  - ES
  - 模块化
categories:
  - 笔记
  - 前端
comments: true
photos: 'https://cdn.jsdelivr.net/gh/wallleap/cdn@latest/img/cover/(00).jpg'
date: 2020-06-04 23:33:49
keywords: 前端, ES, 模块化
---

## 一、理解ES

1. 全称: ECMAScript

   - 它是一种由ECMA组织(前身为欧洲计算机制造商协会)制定和发布的脚本语言规范
   - 我们学习的JavaScript就是ECMA的实现，但属于ECMAScript和JavaScript平时表达同一个意思

2. JS包含三个部分：

   - ECMAScript(js基础、核心)

   - 扩展-->浏览器端
     - BOM(浏览器对象模型)
     - DOM(文档对象模型)

   - 扩展-->服务器端
     - Node.js

3. ES的几个重要版本

   - ES5：09年发布
   - **ES6(ES2015)**:15年发布，也称为ECMA2015——重点
   - ES7(ES2016):16年发布，也称为ECMA2016（变化不大）



## 二、ES5

### 1、严格模式

  * 理解

      * 运行模式: 正常(混杂)模式与严格模式
      * 这种模式使得JavaScript在更严格的语法条件下运行

  * 目的/作用: 
    * 使得Javascript在更严格的条件下运行
    * 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为
    * 消除代码运行的一些不安全之处，保证代码运行的安全
    
* 使用

  * 在全局或函数的第一条语句定义为：`use strict`
  * 如果浏览器不支持，只解析为一条简单的语句，没有任何副作用

* 语法和行为改变

  * 声明定义变量必须用var
  * 禁止自定义的函数中的this关键字指向全局对象(window)
  * 创建eval作用域, 更安全
  * 对象不能有重名的属性

  ```html
  <script>
    'use strict'
    var username = 'luwang'
    // name = 'luwang' 在严格模式下不用var声明变量会报错
    console.log(username)
  
    function Person(name, age){
      this.name = name
      this.age = age
    }
    new Person('luwang', 23)
    // Person('luwang', 23) //没有new会报错
  
    var str = 'web'
    eval('var str = "HTML"; alert(str)') // HTML
    alert(str) // web 即开启严格模式之后不会污染全局作用域
  
    var obj = {
      username: 'luwang',
      username: 'luwang'  // 定义重名了
    }
  </script>
  ```

  
### 2、JSON对象

  * 作用: 用于在json对象/数组与js对象/数组相互转换
  * `JSON.stringify(obj/arr)` js对象(数组)转换为json对象(数组)
  * `JSON.parse(json)` json对象(数组)转换为js对象(数组)
```html
<script>
  var obj = {username: 'wallleap'}
  obj = JSON.stringify(obj)
  console.log(typeof obj)
  obj = JSON.parse(obj)
  console.log(typeof obj)
</script>
```



### 3、Object扩展

ES5给Object扩展了一些静态方法，常用的两个：

  * `Object.create(prototype[, descriptors]) `: 创建一个新的对象
    
    * 作用：以指定对象为原型创建新的对象
    
    * 为新的对象指定新的属性, 并对属性进行描述
      * `value `: 指定值
      * `writable` : 标识当前属性值是否是可修改的, 默认为`false`
      * `configurable`：标识当前属性是否可以被删除，默认为`false`
      * `enumerable`：标识当前属性是否能用for in枚举，默认为`false`
      
      ```html
      <script>
        var obj = {username: 'luwang', age:23}
        var obj1 = {}
        obj1 = Object.create(obj, {  // obj的属性为obj1的原型
          sex: {
            value: '男',
            writable: true,  // 默认false
            configurable: true,
            enumerable: true
          }
        })
        console.log(obj1.sex)
        obj1.sex = 'nan'
        console.log(obj1.sex)
        delete obj1.sex
        console.log(obj1)
        for(var i in obj1){
          console.log(i)
        }
      </script>
      ```
      
      
    
  * `Object.defineProperties(object, descriptors) `: 为指定对象定义扩展多个属性

    - **get方法** : 用来得到当前属性值的回调函数
    - **set方法** : 用来监视当前属性值变化的回调函数

    ```html
    <script>
      var obj = {username: 'luwang', age:23}
      var obj1 = {}
      var obj2 = {firstName: 'lu', lastName: 'wang'}
      Object.defineProperties(obj2, {
        fullName: { // 此方法在原型中
          get: function(){ // 获取扩展属性的值
            console.log('get方法被调用')
            return this.firstName + ' ' + this.lastName
          },
          set: function(data){ // 监听扩展属性，当扩展属性发生变化的时候会自动调用，自动调用后会讲变化的值作为实参注入到set函数
            console.log('set方法被调用，', data)
            var names = data.split(' ') // 根据空格拆分为数组
            this.firstName = names[0]
            this.lastName = names[1]
          }
        }
      })
      console.log(obj2.fullName) // get会自动调用 
      obj2.fullName = 'lu wang'  
      console.log(obj2.fullName)
    </script>
    ```

    console.log(obj2)   fullName

    惰性求值：点击才给值(什么时候要什么时候给)，会再次调用get方法

    ![惰性求值](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1589786198022.png)

    - 什么时候调用：
      - get方法：获取扩展属性值的时候get方法自动调用
      - set方法：监听
    - 存储器属性：setter，getter一个用来存值，一个用来取值



对象本身也有两个方法

* get propertyName(){}
* set propertyName(){}

```html
<script>
  var obj = {
    firstName: 'lu', 
    lastName: 'wang',
    get fullName(){
      return this.firstName + ' ' + this.lastName
    },
    set fullName(data){
      var names = data.split(' ')
      this.firstName = names[0]
      this.lastName = names[1]
    }
  }
  console.log(obj)
  obj.fullName = 'lu wang'
  console.log(obj.fullName)
</script>
```





### 4、Array扩展

  * Array.prototype.indexOf(value) : 得到值在数组中的第一个下标

  * Array.prototype.lastIndexOf(value) : 得到值在数组中的最后一个下标

  * **Array.prototype.forEach(function(item, index){}) : 遍历数组**

  * **Array.prototype.map(function(item, index){}) : 遍历数组返回一个新的数组**

  * **Array.prototype.filter(function(item, index){}) : 遍历过滤出一个子数组，返回条件为true的值**

    ```javascript
    var arr = [2,4,5,1,6,7,4,3,9]
    console.log(arr.indexOf(4))
    console.log(arr.lastIndexOf(4))
    arr.forEach(function(item, index){
        console.log(item, index)
    })
    var arr1 = arr.map(function(item, index){
        return item + 10
    })
    console.log(arr, arr1)
    arr.filter(fuction(item, index){
        return item > 3
    })
    ```

    

### 5、Function扩展

this，强制绑定使用call和bind

eg:

```javascript
var obj = {username: 'luwang'}
function foo(){
    console.log(this)   
}
foo() // this-->Window 全局
// call和apply不传参的时候是一样的
foo.call(obj) // this-->{username: 'luwang'} obj对象
foo.apply(obj) // this-->{username: 'luwang'} obj对象
// bind的特点： 绑定完this不会立即调用当前的函数，而是将函数返回
// var bar = foo.bind(obj)
// bar()
foo.bind(obj)()


// 传入参数的形式
var obj1 = {age: 23}
function fun(data){
    console.log(this, data)
}
fun(22) // Window  22
// call直接从第二个参数开始，依次传入
fun.call(obj1, 21) // {age: 23} 21
// 第二参数必须是数组，传入放在数组里
fun.apply(obj1, [20]) // {age: 23} 20

// bind传参的方式通call一样
fun.bind(obj1, 18)()
```



  * `Function.prototype.bind(obj)`
    
      * 将函数内的this绑定为obj, 并将函数返回
  * 面试题: 区别bind()与call()和apply()?
      * `fn.bind(obj)` : 指定函数中的this, 并返回函数(不会立即调用)，一般用在回调函数绑定其他对象的this
      
        ```javascript
        var obj = {username: 'luwang'}
        setTimeout(function(){
            console.log(this) // Window
        }, 1000)
        setTimeout(function(){
            console.log(this) // Window
        }.bind(obj), 1000)
        ```
      
      * `fn.call(obj) `: 指定函数中的this,并调用函数
      
      * `fn.apply(obj)`
      
        
      
### 6、Date扩展

  * Date.now() : 得到当前时间值

    

## 三、ES6

### 1、2个新的关键字

- 块作用域：ES5中没有(只有全局和函数作用域)，ES6有

1. **let**

   - 作用：与var相似，用于声明一个变量

   - 特点

     - 在块作用域内有效
     - 不能重复声明
     - 不会预处理，不存在变量提升

   - 应用

     - 循环遍历加监听

       ```html
       <br/><button>按钮1</button><br/><br/>
       <button>按钮2</button><br/><br/>
       <button>按钮3</button>
       <script>
           var btns = document.getElementsByTagName('button')
           for(var i = 0; i < btns.length; i++){
               var btn = btns[i]
               btn.onclick = function(){
                   alert(i)
               }
           }
           /*
            * 一直会显示3
            * 点击事件对应的是回调函数，回调函数又称勾子函数，回调函数会被放到事件队列中，等主线程上的代码执行完毕之后再通过钩子一样的形式，勾出来执行
            * 以前的方式是通过闭包，立即执行函数(自己的作用域)
           */
           for(var i = 0; i < btns.length; i++){
             var btn = btns[i]
             ;(function(i){  // 声明的形参
               btn.onclick = function(){
               alert(i)
             }
             })(i)   // 传的实参
           }
           /*
           * 闭包利用的是函数作用域的特点
           * 因此可以直接使用let
           */
           for(let i = 0; i < btns.length; i++){ // let，在块作用域内有效
             var btn = btns[i]
             btn.onclick = function(){
               alert(i)
             }
           }
       </script>
       ```

     - 使用let代替var是趋势

2. **const**

   - 作用：定义一个常量

   - 特点

     - 不能修改
     - 其他特点同let

   - 应用

     - 保存不用改变的数据

     ```javas
     const PI = 3.1415926
     ```

     

### 2、变量(对象)的解构赋值

  * 理解：从对象或数组中提取数据，并赋值给多个变量

  * 将包含多个数据的对象(数组)一次赋值给多个变量

  * 数据源: 对象/数组

  * 目标: {a, b}/[a, b]

  * 对象的解构赋值：`let {n, a} = {n:'tom', a:12}` 把对象中的值赋值出来(根据属性名key)

  * 数组的解构赋值：`let[a, b] = [1, 'luwang']` (根据下标)

  * 用途：给多个形参赋值

    ```javascript
    let obj = {
        username: 'luwang',
        age: 23
    }
    // let username = obj.username
    // let age = obj.age
    // console.log(username, age)
    // let {username, age} = obj // 对象，因此需要以对象的形式来接收 只需要一个就写一个，不需要按顺序
    // console.log(username, age)
    let {age} = obj
    console.log(age)
    
    let arr = [1, 3, 5,'abc', true]
    // let [a, b, c, d, e] = arr
    // console.log(a, b, c, d, e)
    // let [a, b] = arr
    // console.log(a, b)
    let [,,a, b] = arr
    console.log(a, b)
    
    function foo({username, age}){ // {username, age} = obj
        console.log(username, age)
    }
    foo(obj)
    ```





### 3、各种数据类型的扩展

  * 字符串
    * **模板字符串** 
      * 作用: 简化字符串的拼接
      * 模板字符串必须用``，波浪线那个
      * 变化的部分使用${xxx}定义
    
    ```javascript
    let obj = {username: 'luwang', age: 23}
    /*
    * 之前的写法：简单拼串
    * 缺点：可能会拼错，效率低。比如，url携带10个参数，动态拼起来
    */
    let str = 'My name is ' + obj.username + ', age is '+ obj.age
    console.log(str)
    /*
    * ES6提供的模板字符串
    */
    str = `My name is ${obj.username} age is ${obj.age}`
    ```
    
    * `includes(str)` : 判断是否包含指定的字符串
    * `startsWith(str) `: 判断是否以指定字符串开头
    * `endsWith(str)` : 判断是否以指定字符串结尾
    * `repeat(count) `: 重复指定次数
    
    ```javascript
    let str = 'asdfghjkklqwrtyuiopzxcvbnm123467890'
    console.log(str.includes('t')) // true
    console.log(str.includes('abc')) // false
    console.log(str.startsWith('a')) // true
    console.log(str.endsWith('0')) // true
    console.log(str.repeat(2)) // asdfghjkklqwrtyuiopzxcvbnm123467890asdfghjkklqwrtyuiopzxcvbnm123467890
    ```
    
    

- 数值扩展

  - 二进制与八进制表示法：二进制用0b，八进制用0o
  - `Number.isFinite(i)`：判断是否是有限大的数字
  - `Number.isNaN(i)`：判断是否是NaN
  - `Number.isInteger(i)`：判断是否是整数
  - `Number.parseInt(str)`：将字符串转换为对应的数值
  - `Math.trunc(i)`：直接去除小数部分

  ```javascript
  console.log(0b1010)
  console.log(0o12)
  console.log(Number.isFinite(Infinity))
  console.log(Number.isNaN(NaN))
  console.log(Number.isInteger(123.1))
  console.log(Number.isInteger(123.0))
  console.log(Number.parseInt('123abc123')) // 123
  console.log(Number.parseInt('a123abc123')) // NN
  console.log(Math.trunc(123.123)) // 123
  ```

  



  * 对象
    * **简化的对象写法**
      
      * 省略同名的属性值
      * 省略方法的function
      
      ```JavaScript
      let name = 'Tom';
      let age = 12;
      /* 正常情况 */
      let obj = {
          name: name,
          age: age，
          getName: function(){
              retrun this.name
          }
      }
      console.log(obj)
      /* key和value相同，可以省略 */
      let person = {
          name,  // 同名的属性可以不写
          age,
          setName (name) { // 可以省略函数的function
              this.name = name
          }
      }
      ```
      
    * `Object.assign(target, source1, source2..) `: 将源对象的属性复制到目标对象上
    
    ```javascript
    let obj = {}
    let obj1 = {username:'a', age: 20}
    let obj2 = {sex: '男'}
    // Object.assign(obj, obj1)
    // console.log(obj) // {username: "a", age: 20}
    Object.assign(obj, obj1, obj2)
    console.log(obj) // {username: "a", age: 20, sex: "男"}
    ```
    
    * `Object.is(v1, v2)` : 判断2个数据是否完全相等
    
    ```javascript
    console.log(0 == -0) // true
    console.log(NaN == NaN) //false
    console.log(Object.is(0, -0)) // false
    console.log(Object.is(NaN, NaN)) // true
    ```
    
    * __proto__属性 : 隐式原型属性.ES6中能直接操作`__proto__`属性
    
    ```javascript
    let obj = {}
    let obj1 = {salary: 5000000}
    obj.__proto__ = obj1
    console.log(obj)
    console.log(obj.salary)
    ```
    
    





  * 数组
    * `Array.from(v)` : 将伪数组对象或可遍历对象转换为真数组
    * `Array.of(v1, v2, v3)` : 将一系列值转换成数组
    * `find(function(value, index, arr){return true})` : 找出第一个满足条件返回true的元素
    * `findIndex(function(value, index, arr){return true}) `: 找出第一个满足条件返回true的元素下标
    
    ```html
    <button>測試1</button><br>
    <button>測試2</button><br>
    <button>測試3</button>
    <script>
      let btns = document.getElementsByTagName('button')
      // 偽數組 不能使用forEach(數組的方法)
      Array.from(btns).forEach(function(item, index){
        console.log(item)
      })
    
      let arr = Array.of(1, 4, 'abc', true)
      console.log(arr)
    
      let arr2 = [2,3,4,2,5,7,3,6]
      console.log(arr2.find(function(item, index){
        return item > 4
      }))
      console.log(arr2.findIndex(function(item, index){
        return item > 4
      }))
    </script>
    ```
    
    





  * 函数
    * **箭头函数**
      * 用来定义匿名函数
      * 基本语法:
        * 没有参数: () => console.log('xxxx')   箭头前的()不能省略
        * 一个参数: i => i+2  可以省略
        * 大于一个参数: (i,j) => i+j  ()不能省略
        * 函数体不用大括号: 默认返回结果
        * 函数体如果有多个语句, 需要用{}包围
      * 使用场景: 多用来定义回调函数
      * 特点：
        * 简洁
        * 箭头函数没有自己的this，箭头函数的this不是调用的时候决定的，而是在定义的时候所处的对象就是它的this
        * 扩展理解：箭头函数的this看外层是否有函数
          * 箭头外层有函数，this是外层函数的this
          * 箭头外层无函数，this是window
    
    ```javascript
    let fun = function(){console.log('fun')}
    fun()
    // 1、没有形参
    let fun1 = () => console.log('fun1')
    fun1()
    
    // 2、只有一个形参
    let fun2 = (a) => console.log(a)
    // 可省略() let fun2 = a => console.log(a)
    fun2('aaa')
    
    // 3、两个及两个以上的形参
    let fun3 = (x,y) => console.log(x, y)
    fun3(1, 2)
    
    // I、函数体只有一条语句或表达式，{}可以省略-->会自动返回语句执行的结果或表达式的结果
    let foo = (x, y) => x + y
    // let foo = (x, y) => {return x + y}
    console.log(foo(1, 3))
    
    // II、函数体不止一条语句或者表达式， {}不可以省略
    let foo2 = (x, y) => {
        console.log(x, y)
        return x + y
    }
    console.log(foo2(3, 5))
    
    // 箭头函数的this
    <br/><button id="btn1">按钮1</button><br/><br/>
    <button id="btn2">按钮2</button><br/><br/>
    <button id="btn3">按钮3</button>
    <script>
        let btn1 = document.getElementById('btn1')
        let btn2 = document.getElementById('btn2')
        let btn3 = document.getElementById('btn3')
        btn1.onclick = function(){
          console.log(this) // <button id="btn1">按钮1</button>
        }
        btn2.onclick = () => {
          console.log(this)  // Window
        }
        let obj = {
          name: '箭头函数',
          getName: function(){
            btn3.onclick = () => {
              console.log(this) // {name: "箭头函数", getName: ƒ}
            }
          }
        }
        obj.getName()
    	let obj1 = {
          name: '箭头函数',
          getName: () => {
            btn3.onclick = () => {
              console.log(this) // Window
            }
          }
        }
        obj.getName()
    </script>
    ```





- **3点运算符/点点点运算符**

  * rest(可变)参数
    * 通过形参左侧的...来表达, 取代arguments的使用
    * 比arguments灵活，只能是最后部分形参参数
      * arguments是伪数组，有length，但是没有数组的一般方法，不能使用forEach遍历
      * callee是arguments的一个属性，等于函数本身，递归的时候可以写为：`arguments.callee()`

  ```javascript
  // arguments
  function foo(a, b){
    console.log(arguments)
    // arguments.callee() 调用自身，相当于foo(参数)
    /* arguments.forEach(function(item, index){ // 会报错，伪数组并没有数组的一般方法
        console.log(item, index)
    }) */
  }
  foo(2,5)
  ```

  ![参数](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1590476357564.png)

  ```javascript
  // 点点点运算符
  function foo(...value){
    console.log(arguments)
    console.log(value) // 就是一个正常的数组
    value.forEach(function(item, index){
      console.log(item, index)
    })
  }
  foo(2,5)
  
  function foo(a, ...value){// ...value只能放在最后面
    console.log(arguments)
    // arguments.callee()
    console.log(value)	// 使用的时候不用加...
    value.forEach(function(item, index){
      console.log(item, index)
    })
  }
  foo(2, 3, 5, 7) // 最前面的就是a，value就不包括它了
  ```

  

  * 第二种用法——扩展运算符
    * 可以分解出数组或对象中的数据

  ```javascript
  let arr = [1, 6]
  let arr1 = [2, 3, 4, 5]
  arr = [1, ...arr1, 6]
  console.log(arr)	// (6) [1, 2, 3, 4, 5, 6]  数组
  console.log(...arr) // 1 2 3 4 5 6  每项值
  ```





- **形参的默认值**

  * 定义形参时指定其默认的值
  * 当不传入参数的时候默认使用形参里的默认值

  ```javascript
  // 定义一个点的坐标的构造函数
  function Point(x, y){
    this.x = x
    this.y = y
  }
  let point = new Point(50, 20)
  console.log(point) // Point {x: 50, y: 20}
  // 忘记传参
  let point1 = new Point()
  console.log(point1) // Point {x: undefined, y: undefined}
  
  /* 
  * 因此会有需求，在忘记传参的时候使用默认值
  * 在形参的位置赋默认值
  */
  function Point(x = 0, y = 0){
    this.x = x
    this.y = y
  }
  let point = new Point(50, 20)
  console.log(point) // Point {x: 50, y: 20}
  // 忘记传参，使用默认值
  let point1 = new Point()
  console.log(point1) // Point {x: 0, y: 0}
  ```



### 4、深度克隆

- 拷贝数据：

  - 基本数据类型
    - 拷贝后会生成一份新的数据
    - 修改拷贝以后的数据不会影响原数据
  - 引用数据类型
    - 拷贝后不会生成新的数据，而是拷贝的引用
    - 修改拷贝以后的数据会影响原来的数据

  ```javascript
  // 基本數據類型
  let str = 'abcd'
  let str2 = str
  console.log(str, str2)
  str2 = ''
  console.log(str, str2)
  
  // 引用數據類型
  let obj = {username: 'kobe', age:39}
  let obj1 = obj
  console.log(obj, obj1)
  obj1.username = 'wade'
  console.log(obj, obj1)
  let arr = [1,4,{username:'kobe',age:39}]
  let arr2 = arr
  arr2[0] = 'abcd'
  console.log(arr, arr2)
  ```

  

- 拷贝数据的方法

  - 直接赋值给一个变量    // 浅拷贝(浅克隆)——能影响
  - `Object.assign()`     // 浅拷贝

  ```javascript
  let obj = {username: 'kobe'}
  let obj2 = Object.assign(obj)
  console.log(obj, obj2)
  obj2.username = 'wade'
  console.log(obj, obj2)
  ```

  - `Array.prototype.concat()`   //浅拷贝
  
  ```javascript
  let arr = [1, 4, {username: 'kobe'}]
  let testArr = ['ce', 'shi']
  // let arr2 = arr.concat(testArr)
  let arr2 = arr.concat()
  console.log(arr, arr2)
  arr2[1] = 'a'
  console.log(arr, arr2)
  arr2[2].username = 'wade'
  console.log(arr, arr2)
  ```
  
  - `Array.prototype.slice()`   // 浅拷贝
  
  ```javascript
  let arr = [1, 4, {username: 'kobe'}]
  let arr2 = arr.slice()
  arr2[2].username = 'wade'
  console.log(arr, arr2)
  ```
  
  - `JSON.parse(JSON.stringify())`   // 深拷贝(深度克隆)——修改不影响引用类型的原数据。
    - 拷贝的数据里不能有函数(处理不了)，先是将数据转为了JSON格式，字符串对应js中的只有对象和数组，没有函数
  
  ```javascript
  let arr = [1, 4, {username: 'kobe'}]
  let arr2 = JSON.stringify(arr)
  arr2 = JSON.parse(arr2)
  arr2[2].username = 'wade'
  console.log(arr, arr2)
  ```
  
- 浅拷贝

  - 特点：拷贝的是引用，修改拷贝以后的数据会影响原来的数据，使得原数据不安全

- 深拷贝

  - 特点：拷贝的时候生成新数据，修改拷贝以后的数据不会影响原数据

- 这两个都是针对对象/数组来说的

- 思考：如何实现深度拷贝？

  - 拷贝的数据里有对象/数组，即使有对象/数组可以继续遍历对象、数组，拿到里边的每一项值，直到拿到的是基本数据类型，然后再去复制(拷贝的数据里不能有对象/数组)

  - 知识点储备

    - 如何判断数据类型
      1. `typeof `返回的数据类型： String、Number、boolean、undefined、Object、Function
      2. `Object.prototype.toString.call(obj)`--->`Object.prototype.toString.call(data).slice(8, -1)`

    ```javascript
    let result = 'abc' // [object String]
    result = null // [object Null]
    result = [1, 'a'] // test-demo.html:17 [object Array]
    // console.log(Object.prototype.toString.call(result))
    // console.log(typeof Object.prototype.toString.call(result)) // 返回的是string
    // 因此可以用下面这种方式显示数据类型
    console.log(Object.prototype.toString.call(result).slice(8, -1))
    
    ```

    - for in 循环

      - 用于循环对象，枚举出来的是属性名

      ```javascript
      let obj = {username: 'kobe', age: 39}
      for(let i in obj){
        console.log(i) // username age
      }
      ```

      - 循环数组时，枚举的是下标

      ```javascript
      let arr = [1,3,'abc']
      for(let i in arr){
        console.log(i) // 0 1 2
      }
      ```

  - 实现深度克隆

  ```javascript
  // 定义检测数据类型的功能函数
  function checkType(target){
    return Object.prototype.toString.call(target).slice(8, -1)
  }
  console.log(checkType([1,2,'a']))
  // 实现深度克隆-->对象/数组
  function clone(target){
    // 1.判断拷贝的数据类型
    let result, targetType = checkType(target)
    if(targetType === 'Object'){
      // 2.初始化数据，对象/数组/其他类型仍不改变
      result = {}
    }else if(targetType === 'Array'){
      result = []
    }else{
      return target
    }
    // 3.遍历目标数据
    for(let i in target){
      // 遍历数据结构的每一项值
      let value = target[i] // key、下标都可以用[]
      // 判断目标结构里的每一值是否存在数组/对象
      if(checkType(value) === 'Object' || checkType(value) === 'Array'){// 对象、数组中还嵌套了对象数组
        // 继续遍历获取到的value值
        result[i] = clone(value)
      }else{ // 获取到的value值是基本数据类型或函数
        result[i] = value
      }
    }
    return result
  }
  let arr = [1,2,{username: 'kobe'}]
  let arr2 = clone(arr)
  console.log(arr, arr2)
  arr2[2].username = 'abdc'
  console.log(arr, arr2)
  
  let obj = {username: 'luwang', age: 23}
  let obj2 = clone(obj)
  console.log(obj, obj2)
  obj2.username = 'LUWANG'
  console.log(obj, obj2)
  ```

  



### 7、class类

  * 通过class定义类，实现类的继承

    * 回顾：原型、构造函数、构造函数+原型——继承

      ```javascript
      function Person(name, age){
        this.name = name
        this.age = age
      }
      let person = new Person('kobe', 39)
      console.log(person)
      ```

      ![继承](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591769869983.png)

  * 在类中通过 constructor() 定义构造方法(相当于构造函数)

    ```javascript
    // 定義一個人物的類
    class Person{
     // 类的构造方法
      constructor(name, age){
        this.name = name
        this.age = age
      }
      // 类的一般方法
      showMe(){
        console.log(this.name)
      }
    }
    let person = new Person('kobe', 39)
    console.log(person)
    person.showName()
    ```

    ![继承](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591770059566.png)

  * 一般方法: xxx () {}

  * 用extends来定义子类（实现累的继承）

  * 用super()来调用父类的构造方法

  * 子类方法自定义: 将从父类中继承来的方法重新实现一遍（重写从父类继承的一般方法）

    ```javascript
    // 定義一個人物的類
    class Person{
      constructor(name, age){
        this.name = name
        this.age = age
      }
      showMe(){
        console.log('調用父類的方法')
        console.log(this.name, this.age)
      }
    }
    let person = new Person('kobe', 39)
    person.showMe()
    
    // 子類
    class StarPerson extends Person{
      constructor(name, age, salary){
        super(name, age) // 調用父類的構造方法
        this.salary = salary
      }
      showMe(){
        console.log('子類重寫的方法')
        console.log(this.name, this.age, this.salary)
      }
    }
    let p1 = new StarPerson('wade', 36, 10000000)
    console.log(p1)
    p1.showMe()
    ```

  * js中没有方法重载(方法名相同, 但参数不同)的语法





### 4、set/Map容器结构

  * 容器: 能保存多个数据的对象, 同时必须具备操作内部数据的方法

  * 任意对象都可以作为容器使用, 但有的对象不太适合作为容器使用(如函数)

  * **Set的特点**: 保存多个value, value是不重复 ====>数组元素去重

  * **Map的特点**: 保存多个key--value, key是不重复, value是可以重复的

  * API
    
      * Set容器：无序不可重复的多个value的集合体
        * `Set()`
        * `Set(arr)` //arr是一维数组
        * `add(value)`
        * `delete(value)`
        * `clear()`
        * `has(value)`
        * `size`
    * Map容器：无序的key、不重复的多个key-value的集合体
      * `Map()`
      * `Map(arr) `//arr是二维数组
      * `set(key, value)`
      * `get(key)`
      * `delete(key)`
      * `clear()`
      * `has(key)`
      * `size`
    
    ```javascript
    // let set = new Set()
    let set = new Set([1,2,4,5,2,3,6]) // 重复的会去除
    console.log(set)
    set.add(7)
    console.log(set.size, set)
    console.log(set.has(8))
    console.log(set.has(7))
    set.delete(7)
    console.log(set.size, set)
    set.clear()
    console.log(set.size, set)
    
    // let map = new Map()
    let map = new Map([['username', 'aaa'], ['age', 35], ['sex', 'female']]) // 二维数组，且只能有两值(一个是key，一个是value)
    map.set('other', 'shuoming')
    console.log(map.size, map)
    map.delete('other')
    console.log(map)
    console.log(map.has('username'))
    map.clear()
    console.log(map)
    ```



### 5、for--of循环

  * 可以遍历任何容器（Set、Map）

```javascript
let set = new Set([1, 2, 4, 3, 4, 5]) 
for(let i of set){
  console.log(i)
}

// 可以用Set给数组去重
let arr = [1,2,4,5,5,6,2]
let arr1 = arr
arr = [] // 保留数组类型
let set = new Set(arr1)
for(let i of set){
  arr.push(i)
}
console.log(arr)
```

  * 数组
  * 对象
  * 伪/类对象
  * 字符串
  * 可迭代的对象













### 6、Promise对象

- 理解：
  - Promise对象代表了某个将要发生的事件（通常是一个异步操作）
  - ES6的Promise是一个构造函数，用来生成promise实例

  * 解决`回调地狱`(回调函数的层层嵌套, 编码是不断向右扩展, 阅读性很差)；有了promise对象，可以将异步操作以同步的流程表达出来，避免了层层嵌套的回调函数（回调地狱）

  * 能以同步编码的方式实现异步调用

  * 在es6之前原生的js中是没这种实现的, 一些第三方框架(jQuery)实现了promise

  * promise对象的3个状态：

      * pending：初始化状态
      * fullfilled：成功状态
      * rejected：失败状态

  * 应用：

      * 使用promise实现超时处理
      * 使用promise封装处理Ajax请求

    ```
    let request = new XMLHttpRequest()
    request.responseType = 'json'
    request.open("GET", url)
    request.send()
    ```

    

  * ES6中定义实现API(使用Promise基本步骤): 
    ```
    // 1. 创建promise对象
    let promise = new Promise((resolve, reject) => { 
      	// 初始化promise状态为pending
      // 执行异步操作 
      if(异步操作成功) { // 调用成功的回调
        resolve(result); 	// 修改promise状态为fullfilled
      } else { // 调用失败的回调
        reject(errorMsg);   // 修改promise的状态为rejected
      } 
    }) 
    // 2. 调用promise对象的then()
    promise.then(function(
      result => console.log(result), 
      errorMsg => alert(errorMsg)
    ))
    ```
    
    例子：
    
    ```javascript
    // 1、创建promise对象
    let promise = new Promise((resolve, reject) => {
      // 初始化promise状态  pending： 初始化
      console.log('11111111')
      // 执行异步操作，通常是发送Ajax请求，开启定时器
      setTimeout(() => {
        console.log('3333333')
        // 根据异步任务的返回结果去修改promise的状态
        // 异步任务执行成功
        // resolve('哈哈，') // 修改promise的状态为 fullfilled：成功
        // 异步任务执行失败
        reject('555, ') // 修改promise的状态为 rejsected： 失败
      }, 2000)
    })
    console.log('222222222')
    // 2. 调用promise对象的then()
    promise
      .then((data) => { // 成功的回调
        console.log(data, '成功了~~~')
      }, (error) => { // 失败的回调
        console.log(error, '失败了……')
    })
    ```
    
    实例：新闻、新闻的评论：只发新闻的内容；在接着根据新闻的id拿取这个新闻下的评论
    
    1、打开ES5_6_7中code目录中的es_server
    
    2、输入命令`node bin/www`
    
    3、浏览器中访问 http://localhost:3000/news ，能够获取数据
    
    ```javascript
    // 定义获取新闻的功能函数
    function getNews(url){
      let promise = new Promise((resolve, reject) => {
        // 状态：初始化
        // 执行异步任务
        let xmlHttp = new XMLHttpRequest()
        // 绑定监听readyState
        /*xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState === 4 && xmlHttp.status == 200){
            // 请求成功
            console.log(xmlHttp.responseText)
            // 修改状态
            resolve(xmlHttp.responseText) // 修改promise的状态为成功
          }else{
            // 请求失败
            reject('暂时没有新闻内容')
          }
        } --> 逻辑有问题*/
        xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState === 4){
            if(xmlHttp.status == 200){
              // 请求成功
              // console.log(xmlHttp.responseText)
              // 修改状态
              resolve(xmlHttp.responseText) // 修改promise的状态为成功
            }else{
              // 请求失败
              reject('暂时没有新闻内容')
            }
          }
        }
    
        // open 设置请求得方式以及url
        xmlHttp.open('GET', url)
        // 发送
        xmlHttp.send()
      })
      return promise
    }
    getNews('http://localhost:3000/news?id=2')
      .then((data) => {
        console.log(data)
        // 发送请求获取评论内容准备url
        let commentsUrl = JSON.parse(data).commentsUrl
        let url = 'http://localhost:3000' + commentsUrl
        // 发送请求
        return getNews(url)
      },(error) => {
        console.log(error)
      })
      .then((data) => {
        console.log(data)
      }, () => {
        
    })
    ```
    
    



### 8、Symbol属性

- 前言：ES5中对象的属性名都是字符串，容易造成重名，污染环境
- 概念：ES6中添加了一种**原始数据类型symbol**(已有的数据类型：String、Number、boolean、null、undefined、对象)
- 特点
  - Symbol属性对应的值是**唯一**的，解决命名冲突问题
  - Symbol值**不能**与**其他数据**进行**计算**，包括与字符串拼串
  - for in、for of遍历时不会遍历symbol属性
- 使用
  - 调用Symbol函数得到symbol值
  - 传参标识
  - 内置Symbol值
    - 除了定义自己使用的Symbol值以外，ES6还提供了11个内置的Symbol值（查看官方文档）
    - 对象的Symbol.iterator属性，指向该对象的默认遍历器方法

```javascript
// 创建symbol属性值
let symbol = Symbol()
console.log(symbol)  // Symbol()
let obj = {username:'kobe', age:39}
// 可以添加symbol属性——但是得用另一种方式
obj.gender = '男'
obj[symbol] = 'hello'
console.log(obj)  // {username: "kobe", age: 39, gender: "男", Symbol(): "hello"}

//let symbol2 = Symbol()
//let symbol3 = Symbol()
// 并不相同，值是唯一的
//console.log(symbol2, symbol3, symbol2 == symbol3)  // Symbol() Symbol() false

// 可以传参，这样就能很明显看出不同了
let symbol2 = Symbol('one')
let symbol3 = Symbol('two')
console.log(symbol2, symbol3, symbol2 == symbol3)  // Symbol(one) Symbol(two) false

// 可以用来定义常量
const Person_key = Symbol('person_key')
console.log(Person_key)  // Symbol(person_key)






// 等同于在指定的数据结构上部署了Iterator接口
// 当使用for of去遍历某一个数据结构的时候，首先去找Symbol.itearator，找到了就去遍历，没有找到就不能遍历
let targetData = {
  [Symbol.iterator]: function(){
    let nextIndex = 0
    return{
      next: function(){
        return nextIndex < this.length ? {value: this[nextIndex++], done: false} : {value: undefined, done: true}
      }
    }
  }
}
// 使用三点运算符、解构赋值，默认会去调用Iterator接口
let arr2 = [1,6]
let arr3 = [2,3,4,5]
arr2 = [1,...arr3,6]
console.log(arr2)
let [a,b] = arr2
console.log(a,b)

```





### 9、Iterator遍历器

- 概念：iterator是一种接口机制，为各种不同的数据结构提供统一的访问机制

- 作用：

  - 为各种数据结构，提供一个统一的、简便的访问接口
  - 使得数据机构的成员能够按照某种次序排列
  - ES6创造了一种新的遍历命令for...of循环，Iterator接口主要供for...of消费

- 工作原理

  - 创建一个指针对象(遍历器对象)，指向数据结构的起始位置
  - 第一次调用next方法，指针自动指向数据结构的第一个成员
  - 接下来不断调用next方法，指针会一直往后移动，直到指向最后一个成员
  - 没调用next方法返回的是一个包含value和done的对象`{value: 当前成员的值, done: 布尔值}`
    - value表示当前成员的值，done对应的布尔值表示当前的数据的结构是否遍历结束
    - 当遍历结束的时候返回的value值是undefined，done值为false

- 原生具备Iterator接口的数据(可用for...of遍历)

- 扩展理解

  - 当数据结构上部署了Symbol.iterator接口，该数据就是可以用for of遍历
  - 当使用for of去遍历目标数据的时候，该数据会自动去找Symbol.iterator属性（Symbol.iterator属性指向对象的默认遍历器方法）
    - Array
    - arguments
    - set容器
    - map容器
    - String
    - ……

  ```javascript
  // 模拟指针对象(遍历器对象)
  function myIterator(arr){// Iterator接口
  let nextIndex = 0 // 记录指针的位置
    return{
      next: function(){// 遍历器对象
        return nextIndex < arr.length ? {value: arr[nextIndex++], done: false} : {value: undefined, done: true}
      }
    }
  }
  // 准备一个数据
  let arr =[1,4,65,'abc']
  
  let iteratorObj = myIterator(arr)
  console.log(iteratorObj.next()) // {value: 1, done: false}
  console.log(iteratorObj.next()) // {value: 4, done: false}
  console.log(iteratorObj.next()) // {value: 65, done: false}
  console.log(iteratorObj.next()) // {value: "abc", done: false}
  console.log(iteratorObj.next()) // {value: undefined, done: true}
  
  // 将iterator接口部署到指定的数据类型上，可以使用for of去循环遍历
  // 数组、字符串、argument、set容器、map容器
  for(let i of arr){
    console.log(i)
  }// 1 4 65 abc
  
  let str = 'abcdefg'
  for(let i of str){
    console.log(i)
  }// a b c d e f g
  
  function fun(){
    for(let i of arguments){
      console.log(i)
    }
  }
  fun(1,4,5,'abc') // 1 4 5 abc
  
  // let obj = {username:'kobe', age: 39}
  // for(let i of obj){
  //   console.log(i)
  // }// Uncaught TypeError: obj is not iterable 不可迭代
  ```
  
  

### 10、Generator函数

- 概念

  - ES6提供的解决异步编程的方案之一
  - Generator函数是一个状态机，内部封装了不同状态的数据
  - 用来生成遍历器对象
  - 可暂停函数(惰性求值)，yield可暂停，next方法可启动。每次返回的是yield后的表达式结果

- 特点

  - function 与函数名之间有一个星号

  - 内部用yield表达式来定义不同的状态

    例如：

    ```javascript
    function* generatorExample(){
        let result = yield 'hello'  // 状态值为hello
        yield 'generator'  // 状态值为generator
    }
    ```

  - generator函数返回的是指针对象，而不会执行函数内部逻辑

    ```javascript
    function* generatorExample(){
        console.log('开始执行')
        let result = yield 'hello'  // 状态值为hello
        yield 'generator'  // 状态值为generator
    }
    generatorExample() // 调用并不会执行函数内部逻辑
    ```

  - 调用next方法函数，内部逻辑开始执行，遇到yield表达式停止，返回`{value: yield后的表达式结果/return后的返回结果(如果没写，返回undefined),done: boolean值(后面还有返回false，没有返回true)}`

    ```javascript
    function* generatorExample(){
        console.log('开始执行')
        let result = yield 'hello'  // 状态值为hello，会执行，停止 测试yield console.log('会执行')
        console.log('下次调用next执行')
        yield 'generator'  // 状态值为generator
        console.log('下次调用next执行')
        return '返回的结果'
    }
    let MG = generatorExample() // 返回的是指针对象
    console.log(MG.next()) // 执行，遇到yield停止
    console.log(MG.next('可以拿到这个值')) // 再次调用next，往下执行，可以传参
    console.log(MG.next()) // 再次调用next，往下执行，返回true
    ```

  - 再次调用next方法会从上一次停止时的yield处开始，直到最后

  - yield语句返回结果通常为undefined，当调用next方法时传参内容会作为启动时yield语句的返回值

  - 补充

    - 对象的Symbol.iterator属性，指向遍历器对象

    ```javascript
    let obj = {username:'kobe', age: 39}
    obj[Symbol.iterator] = function* myTest(){
        yield 1
        yield 2
        yield 3
    }
    for(let i of obj){
      console.log(i)
    }
    ```

    - 案例
      - 需求
        - 发送ajax请求获取新闻内容
        - 新闻内容获取成功后再次发送请求，获取对应的新闻评论内容
        - 新闻内容获取失败则不需要再次发送请求
      - 启动服务器——进入es_server目录，cmd输入命令`node bin/www`

    ```javascript
    // 要比使用Promise更好
    function getNews(url){
      $.get(url, function(data){ // 前面引入了jQuery
        console.log(data)
        let url = 'http://localhost:3000' + data.commentsUrl
        SX.next(url) // 放在这里也可以往下移，并且这里参数传输更方便
      })
    }
    function* sendXml(){
      let url = yield getNews('http://localhost:3000/news?id=3') // 如果这里出错，后面评论也不会再执行了
      yield getNews(url)
    }
    // 获取遍历器对象
    let SX = sendXml()
    SX.next()
    ```

    

​		



## 四、模块化

### 1、理解

* 什么是模块?

  * 将一个复杂的程序依据一定的规则(规范)封装成几个块(文件), 并进行组合在一起
  * 块的内部数据/实现是私有的, 只是向外部暴露一些接口(方法)与外部其它模块通信
* 一个模块的组成

  * 数据--->内部的属性
  * 操作数据的行为--->内部的函数
* 模块化

  * 编码时是按照模块一个一个编码的, 整个项目就是一个模块化的项目
* 模块化的进化过程

  * 全局function模式 : 

    * 编码: 全局变量/函数
    * 问题: 污染全局命名空间, 容易引起命名冲突/数据不安全

![全局变量](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591870404488.png)

* namespace模式 : 

  * 编码: 将数据/行为封装到对象中
  * 解决: 命名冲突(减少了全局变量)
  * 问题: 数据不安全(外部可以直接修改模块内部的数据)

![Namespace](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591870416611.png)

* IIFE模式/增强

  * IIFE : 立即调用函数表达式--->匿名函数自调用

  * 编码: 将数据和行为封装到一个函数内部, 通过给window添加属性来向外暴露接口


![IIFE](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591870442007.png)

* 引入依赖: 通过函数形参来引入依赖模块

  ```
  (function(window, module2){
    var data = 'atguigu.com'
    function foo() {
       module2.xxx()
       console.log('foo()'+data)
    }
    function bar() {
       console.log('bar()'+data)
    }
    
    window.module = {foo}
  })(window, module2)
  ```

  ![IIFE增强](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591870456267.png)

* 模块化好处

  ![模块化好处](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591870477012.png)

  * 避免命名冲突(减少命名空间污染)
  * 更好的分离, 按需加载
  * 更高复用性
  * 高可维护性

* 页面引入加载script

  ![引入js](https://cdn.jsdelivr.net/gh/wallleap/cdn/img/pic/illustration/1591871174402.png)

  * 问题
    * 请求过多
    * 依赖模糊
    * 难以维护

* 模块化规范

  * **CommonJS**

    * Node.js : 服务器端

    * Browserify : 浏览器端    也称为js的打包工具

    * 基本语法:

      * 定义暴露模块 : exports

        ```
        exports.xxx = value
        module.exports = value
        ```

        引入模块 : require

        ```
        var module = require('模块名/模块相对路径')
        ```

    * 每个文件都可以当作一个模块

    * 引入模块发生在什么时候?

      * Node : 运行时, 动态同步引入
      * Browserify : 在运行前对模块进行编译/转译/打包的处理(已经将依赖的模块包含进来了), 
            运行的是打包生成的js, 运行时不存在需要再从远程引入依赖模块

  * **AMD **: 浏览器端，模块的加载时异步的

    * require.js

    * 基本语法

      * 定义暴露模块: define([依赖模块名], function(){return 模块对象})

      * 引入模块: require(['模块1', '模块2', '模块3'], function(m1, m2){//使用模块对象})

      * 配置: 

        ```
        require.config({
          //基本路径
          baseUrl : 'js/',
          //标识名称与路径的映射
          paths : {
            '模块1' : 'modules/模块1',
            '模块2' : 'modules/模块2',
            'angular' : 'libs/angular',
            'angular-messages' : 'libs/angular-messages'
          },
          //非AMD的模块
          shim : {
            'angular' : {
                exports : 'angular'
            },
            'angular-messages' : {
                exports : 'angular-messages',
                deps : ['angular']
            }
          }
        })
        ```

  * CMD(通用模块定义) : 浏览器端，模块加载是异步的；模块使用时才会加载执行

    * sea.js

    * 基本语法

      * 定义暴露模块: 

        ```
        define(function(require, module, exports){
          通过require引入依赖模块
          通过module/exports来暴露模块
          exports.xxx = value
        })
        ```

      * 使用模块seajs.use(['模块1', '模块2'])

  * **ES6**

    * ES6内置了模块化的实现，依赖模块需要编译打包处理

    * 基本语法

      * 定义暴露模块 : export

        * 暴露一个对象: 

          ```
          export default 对象
          ```

        * 暴露多个: 

          ```
          export var xxx = value1
          export let yyy = value2
          
          var xxx = value1
          let yyy = value2
          export {xxx, yyy}
          ```

      * 引入使用模块 : import

        * default模块:

          ```
          import xxx  from '模块路径/模块名'
          ```

        * 其它模块

          ```
          import {xxx, yyy} from '模块路径/模块名'
          import * as module1 from '模块路径/模块名'
          ```

    * 问题: 所有浏览器还不能直接识别ES6模块化的语法  

    * 解决:

      * 使用Babel将ES6--->ES5(使用了CommonJS) ----浏览器还不能直接支行
      * 使用Browserify--->打包处理----浏览器可以运行




### 2、CommonJS基于服务器端（Node.js）

- 下载安装Node.js

- 创建目录结构

  - Modules

    - module1.js
    - module2.js
    - module3.js

  - app.js

  - package.json（命令创建,`npm init`,再输入包名）

    ```json
    {
        "name": "conmmonjs_node",
        "version": "1.0.0"
    }
    ```

- 下载第三方模块`npm install uniq --save`

  - package.json

    ```json
    {
        "name": "conmmonjs_node",
        "version": "1.0.0",
        "dependencies":{
        	"uniq": "^1.0.1"
    	}
    }
    ```

- 模块化编码

  - module1.js

    ```javascript
    // module.exports = value 暴露一个对象
    module.exports = {
        msg: 'module1',
        foo(){
            console.log(this.msg)
        }
    }
    ```

  - module2.js

    ```javascript
    // 暴露一个函数 module.exports = function(){}
    module.exports = fuction(){
        console.log("module2")
    }
    ```

  - module3.js

    ```javascript
    // exports.xxx = value 分别暴露
    exports.foo = function(){
        console.log('foo() module3')
    }
    exports.bar = function(){
        console.log('bar() module3')
    }
    
    exports.arr = [2, 4, 5, 2, 3, 5, 1]
    ```

  - app.js

    ```javascript
    // 将其他的模块汇集到主模块
    let uniq = require('uniq')
    
    let module1 = require('./modules/module1')
    let module2 = require('./modules/module2')
    let module3 = require('./modules/module3')
    
    module1.foo()
    
    module2()
    
    module3.foo()
    module3.bar()
    
    let result = uniq(module3.arr)
    console.log(result)
    ```

- 通过node运行app.js——`node app.js`



### 3、CommonJS基于浏览器端应用（Browserify）

- 创建项目结构

  - js

    - dist //打包生成文件的目录
    - src //源码所在的目录
      - module1.js
      - module2.js
      - module3.js
      - app.js //应用主源文件

  - index.html

  - package.json

    ```json
    {
        "name": "browserify-test",
        "version": "1.0.0"
    }
    ```

- 下载browserify

  - 全局：`npm install browserify -g`

  - 局部：`npm install browserify --save-dev`

    ```json
    {
        "name": "browserify-test",
        "version": "1.0.0",
        "devDependencies":{
            "browserify": "^14.5.0"
        }
    }
    ```

- 下载第三方模块`npm install uniq --save`

  - package.json

    ```json
    {
        "name": "browserify-test",
        "version": "1.0.0",
        "devDependencies":{
            "browserify": "^14.5.0"
        },
        "dependencies":{
        	"uniq": "^1.0.1"
    	}
    }
    ```

- 定义模块代码

  - module1.js

    ```javascript
    module.exports = {
      foo() {
        console.log('moudle1 foo()')
      }
    }
    ```

  - module2.js

    ```javascript
    module.exports = function () {
      console.log('module2()')
    }
    ```

  - module3.js

    ```javascript
    exports.foo = function () {
      console.log('module3 foo()')
    }
    
    exports.bar = function () {
      console.log('module3 bar()')
    }
    ```

  - app.js

    ```javascript
    //引用模块
    let module1 = require('./module1')
    let module2 = require('./module2')
    let module3 = require('./module3')
    
    let uniq = require('uniq')
    
    //使用模块
    module1.foo()
    module2()
    module3.foo()
    module3.bar()
    
    console.log(uniq([1, 3, 1, 4, 3]))
    ```

- 打包处理js：`browserify js/src/app.js -o js/dist/bundle.js`

- 页面使用引入

  - index.html

    ```html
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>broserify测试</title>
    </head>
    <body>
    <script src="js/dist/bundle.js"></script>
    </body>
    </html>
    ```

    

### 4、AMD规范

#### （1）NoAMD

- 项目结构

  - js
    - alerter.js
    - dataService.js
  - app.js
  - test1.html

- 文件内容

  - dataService.js

    ```javascript
    // 定义一个没有依赖的模块
    (function(win){ // 形参可以和实参的名字相同，这里方便区分
        let name = 'dataservice.js'
        function getName(){
            return name
        }
        win.dataService = {getName}
    })(window) // 实参
    ```

  - alerter.js

    ```javascript
    // 定义一个有依赖的模块
    (function(window, dataService){
        let msg = 'alerter.js'
        function showMsg(){
            alert(msg + ',' + dataService.getName())
        }
        window.alerter = {showMsg}
    })(window, dataService) // 依赖dataService
    ```

  - app.js

    ```javascript
    (function (alerter){
        alerter.showMsg()
    })(alerter)
    ```

  - test1.html

    ```html
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Modular Demo: 未使用AMD(require.js)</title>
    </head>
    <body>
    <script src="./js/dataService.js"></script> 
    <script src="./js/alerter.js"></script> 
    <script src="./app.js"></script> // 下面的分别依赖上面的模块
    </body>
    </html>
    ```



#### （2）AMD（require.js）

1. 下载require.js, 并引入

  * 官网: http://www.requirejs.cn/
  * github : https://github.com/requirejs/requirejs
  * 将require.js导入项目: js/libs/require.js 

2. 创建项目结构

- js
  - libs
    - require.js
  - modules
    - alerter.js
    - dataService.js
  - main.js
- index.html

3. 定义require.js的模块代码

  * dataService.js

    ```javascript
    // 定义没有依赖的模块
    define(function () {
      let msg = 'dataService.js'
    
      function getMsg() {
        return msg.toUpperCase()
      }
      // 暴露模块
      return {getMsg}
    })
    ```

  * alerter.js

    ```javascript
    // 定义有依赖的模块
    define(['dataService', 'jquery'], function (dataService, $) {
      let msg = 'alerter.js'
    
      function showMsg() {
        $('body').css('background', 'gray')
        alert(dataService.getMsg() + ', ' + msg)
      }
    
      return {showMsg}
    })
    ```

4. 应用主(入口)js：main.js

   ```javascript
   (function () {
       //配置
       require.config({
           //基本路径 出发点在根目录下
           baseUrl: "js/",
           //模块标识名与模块路径映射
           paths: {
               "alerter": "modules/alerter",
               "dataService": "modules/dataService",
           }
       })
       //引入使用模块
       require( ['alerter'], function(alerter) {
           alerter.showMsg()
       })
   })()
   ```

5. 页面使用模块：index.html

```html
<script data-main="js/main" src="js/libs/require.js"></script>
```







---

6. 使用第三方基于require.js的框架(jquery)

  * 将jquery的库文件导入到项目: 

    * js/libs/jquery-1.10.1.js

  * 在main.js中配置jquery路径

    ```javascript
    paths: {
        'jquery': 'libs/jquery-1.10.1'  // jQuery定义的返回AMD模块名为小写
    }
    ```

  * 在alerter.js中使用jquery

    ```javascript
    define(['dataService', 'jquery'], function (dataService, $) {
        var name = 'xfzhang'
        function showMsg() {
            $('body').css({background : 'red'})
            alert(name + ' '+dataService.getMsg())
        }
        return {showMsg}
    })
    ```







---

7. 使用第三方不基于require.js的框架(angular/angular-messages)

  * 将angular.js和angular-messages.js导入项目

    * js/libs/angular.js
    * js/libs/angular-messages.js

  * 在main.js中配置

    ```javascript
    (function () {
      require.config({
        //基本路径
        baseUrl: "js/",
        //模块标识名与模块路径映射
        paths: {
          //第三方库
          'jquery' : 'libs/jquery-1.10.1',
          'angular' : 'libs/angular',
          'angular-messages' : 'libs/angular-messages',
          //自定义模块
          "alerter": "modules/alerter",
          "dataService": "modules/dataService"
        },
        /*
         配置不兼容AMD的模块
         exports : 指定导出的模块名
         deps  : 指定所有依赖的模块的数组
         */
        shim: {
          'angular' : {
            exports : 'angular'
          },
          'angular-messages' : {
            exports : 'angular-messages',
            deps : ['angular']
          }
        }
      })
      //引入使用模块
      require( ['alerter', 'angular', 'angular-messages'], function(alerter, angular) {
        alerter.showMsg()
        angular.module('myApp', ['ngMessages'])
        angular.bootstrap(document,["myApp"])
      })
    })()
    ```

  * 页面:

    ```html
    <form name="myForm">
      用户名: <input type="text" name="username" ng-model="username" ng-required="true">
      <div style="color: red;" ng-show="myForm.username.$dirty&&myForm.username.$invalid">用户名是必须的</div>
    </form>
    ```





### <font color=lightgray>5、CMD规范</font>

1. 下载sea.js, 并引入

  * 官网: http://seajs.org/
  * github : https://github.com/seajs/seajs
  * 将sea.js导入项目: js/libs/sea.js 

2. 创建项目结构

  ```
  |-js
    |-libs
      |-sea.js
    |-modules
      |-module1.js
      |-module2.js
      |-module3.js
      |-module4.js
      |-main.js
  |-index.html
  ```

3. 定义sea.js的模块代码

  * module1.js

    ```javascript
    // 没有依赖的模块
    define(function (require, exports, module) {
      //内部变量数据
      var data = 'atguigu.com'
      //内部函数
      function show() {
        console.log('module1 show() ' + data)
      }
    
      //向外暴露
      exports.show = show
    })
    ```

  * module2.js

    ```javascript
    define(function (require, exports, module) {
      let msg = 'module2'
      function bar(){
          console.log(msg)
      }
        module.exports = bar
      /* module.exports = {
        msg: 'I Will Back'
      } */
    })
    ```

  * module3.js

    ```javascript
    define(function(require, exports, module){
        let data = 'module3'
        function fun(){
            console.log(data)
        }
        exports.module3 = {fun}
    })
    /* define(function (require, exports, module) {
      const API_KEY = 'abc123'
      exports.API_KEY = API_KEY
    }) */
    ```

  * module4.js

    ```javascript
    define(function(require, exports, module){
        let msg = 'module4'
        // 同步引入
        let module2 = require('./module2')
        module2()
        // 异步引入
        require.async('./module3', function(module3){
            module3.module3.fun()
        })
        function fun2(){
            console.log(msg)
        }
        exports.fun2 = fun2
    })
    /*define(function (require, exports, module) {
      //引入依赖模块(同步)
      var module2 = require('./module2')
    
      function show() {
        console.log('module4 show() ' + module2.msg)
      }
    
      exports.show = show
      //引入依赖模块(异步)
      require.async('./module3', function (m3) {
        console.log('异步引入依赖模块3  ' + m3.API_KEY)
      })
    })*/
    ```

  * main.js : 主(入口)模块

    ```javascript
    define(function (require) {
      let module1 = require('./module1')
      console.log(module1.foo())
      let module4 = require('./module4')
      module4.fun2()
    })
    /*define(function (require) {
      var m1 = require('./module1')
      var m4 = require('./module4')
      m1.show()
      m4.show()
    })*/
    ```

4. index.html:

  ```
  <!--
  使用seajs:
    1. 引入sea.js库
    2. 如何定义导出模块 :
      define()
      exports
      module.exports
    3. 如何依赖模块:
      require()
    4. 如何使用模块:
      seajs.use()
  -->
  <script type="text/javascript" src="js/libs/sea.js"></script>
  <script type="text/javascript">
    seajs.use('./js/modules/main')
  </script>
  ```


​       





### <font color=red>6、ES6-Babel-Browserify使用教程</font>

1. 定义package.json文件

  ```json
{
    "name" : "es6-babel-browserify",
    "version" : "1.0.0"
}
  ```

2. 安装babel-cli, babel-preset-es2015和browserify // cli——command line interface

  * `npm install babel-cli browserify -g`
* `npm install babel-preset-es2015 --save-dev `
* preset 预设（将es6转换成es5的所有插件打包）

3. 定义.babelrc文件（babel run control）

   ```bash
   {
    "presets": ["es2015"]
   }
   ```

4. 编码

  * js/src/module1.js

    ```JavaScript
    // 暴露模块 分别暴露
    export function foo() {
      console.log('module1 foo()');
    }
    export let bar = function () {
      console.log('module1 bar()');
    }
    export const DATA_ARR = [1, 3, 5, 1]
    ```

  * js/src/module2.js

    ```JavaScript
    // 统一暴露——常规暴露
    let data = 'module2 data'
    
    function fun1() {
      console.log('module2 fun1() ' + data);
    }
    
    function fun2() {
      console.log('module2 fun2() ' + data);
    }
    
    export {fun1, fun2}
    ```

  * js/src/module3.js

    ```JavaScript
    // 默认暴露：可以暴露任意数据类型，暴露什么数据类型接收到的就是什么数据
    // export default value
    export default() =>{
        console.log('我是默认暴露的箭头函数')
    } // 只能暴露一个default，因此暴露对象
    /* export default {
      name: 'Tom',
      setName: function (name) {
        this.name = name
      }
    } */
    ```

  * js/src/app.js

    ```JavaScript
    // 引入其他的模块
    // 语法： import xxx from '路径'
    import {foo, bar} from './module1'
    import {DATA_ARR} from './module1'
    import {fun1, fun2} from './module2'
    
    import module3 from './module3'
    /* import person from './module3' */
    
    // 安装 npm install jquery@1
    import $ from 'jquery'
    
    $('body').css('background', 'red')
    
    foo()
    bar()
    console.log(DATA_ARR);
    fun1()
    fun2()
    
    module3()
    /* person.setName('JACK')
    console.log(person.name); */
    ```

5. 编译

  * 使用Babel将ES6编译为ES5代码(但包含CommonJS语法) : `babel js/src -d js/lib`
  * 使用Browserify编译js : `browserify js/lib/app.js -o js/lib/bundle.js`

6. 页面中引入测试

  ```html
  <script type="text/javascript" src="js/lib/bundle.js"></script>
  ```

7. 引入第三方模块(jQuery)
   1). 下载jQuery模块: 

   * `npm install jquery@1 --save` // @后的是版本，1代表`1.x.x`中的最新版本

   2). 在app.js中引入并使用

   ```
   import $ from 'jquery'
   $('body').css('background', 'red')
   ```







## 五、ES7

### 1、async函数(源自ES2017)

- 概念：真正意义上去解决异步回调的问题，同步流程表达异步操作

- 本质：Generator的语法

- 语法：

  ```javascript
  async function foo(){
  	await 异步操作;
      await 异步操作;
  }
  ```

- 特点：

  - 不需要像Generator去调用next方法，遇到await等待，当前的异步操作完成就往下执行
  - 返回的总是Promise对象，可以用then方法进行下一步操作
  - async取代Generator函数的`*`，await取代Generator的yield
  - 语义上更为明确，使用简单，暂时没有任何副作用

  ```javascript
  // async基本使用
  async function foo(){
    return new Promise(resolve => {
      // setTimeout(function(){
      //   resolve()
      // }, 2000)
      // 可以写成下方这种
      setTimeout(resolve, 2000)
    })
  }
  async function test(){
    console.log('开始执行', new Date().toTimeString())
    await foo()
    console.log('执行完毕', new Date().toTimeString())
  }
  test()
  
  
  // async里await返回值
  function test2(){
    return 'xxx'
  }
  async function asyncPrint(){
    /* let result = await test2()
    console.log(result) // 普通函数没有返回值
    */
    /*
    let result = await Promise.resolve()
    console.log(result) // Promise对象成功状态返回undefined
    */
    let result = await Promise.resolve('promise')
    console.log(result) // Promise对象成功状态传参返回参数 promise
    result = await Promise.reject('失败了……')
    console.log(result) // 失败状态，返回出错，且能将参数返回 Uncaught (in promise) 失败了……
  
  }
  asyncPrint()
  ```

  仍是获取新闻内容案例

  ```javascript
  // async比generator又更简单
  async function getNews(url){
    return new Promise((resolve, reject) => {
      $.ajax({ // 前面已经引入jQuery
        method: 'GET',
        url,  // 这是ES6中简写
        /* success: function(data){
          resolve()
        },
        error: function(error){
          reject() 
        }*/
        // 简写
        success: data => resolve(data),
        error: error => reject(error)
        
      })
    })
  }
  async function sendXml(){
    let result = await getNews('http://localhost:3000/news?id=7')
    console.log(result) // {id: "7", title: "news title1...", content: "news content1...", commentsUrl: "/comments?newsId=7"}
    result = await getNews('http://localhost:3000' + result.commentsUrl)
    console.log(result)
  }
  sendXml()
  ```

  改进一下，由于这种写法error并不会显示错误信息

  ```html
  <script src="./jquery-3.1.0.min.js"></script>
  <script>
    // async比generator又更简单
    async function getNews(url){
      return new Promise((resolve, reject) => {
        $.ajax({
          method: 'GET',
          url,  // 这是ES6中简写
          /* success: function(data){
            resolve()
          },
          error: function(error){
            reject() 
          }*/
          // 简写
          success: data => resolve(data),
          // error: error => reject(error)
          error: error => resolve(false) // 不用reject，而是返回false
        })
      })
    }
    async function sendXml(){
      let result = await getNews('http://localhost:30010/news?id=7')
      console.log(result) // {id: "7", title: "news title1...", content: "news content1...", commentsUrl: "/comments?newsId=7"}
      if(!result){ // 出错就弹窗
        alert('暂时没有新闻……')
      }
      result = await getNews('http://localhost:3000' + result.commentsUrl)
      console.log(result)
    }
    sendXml()
  </script>
  ```

  



### 2、指数运算符(幂): `**`

`console.log(3 ** 3)`



### 3、`Array.prototype.includes(value) `: 判断数组中是否包含指定value

```javascript
let arr = [1,2,3,'abc']
console.log(arr.includes('a'))
```



* **区别方法的2种称谓**
  * 静态(工具)方法
    * Fun.xxx = function(){}
  * 实例方法
    * 所有实例对象 : Fun.prototype.xxx = function(){} //xxx针对Fun的所有实例对象
    * 某个实例对象 : fun.xxx = function(){} //xxx只是针对fun对象 