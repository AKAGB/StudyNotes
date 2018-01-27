# 续JavaScript语法入门

## 二、JavaScript基本语法

### 4. 循环

这里不再赘述条件判断语句，和C、java等语言的一致，事实上循环也基本相同，最基本的`for`、`while`、`do...while`循环是一样的，这里补充３种不太相同的：

(1). `for...in`循环，这个循环用于迭代对象的**所有属性**，比如：


```javascript
> var a = {
    name: 'javascript',
    score: 15,
    func: function () {
        console.log('Hello, world!');
    }
};
undefined
> for (var i in a) {
    console.log(i);
    }
name
score
func
undefined
> for (var i in a) {
    console.log(a[i]);
    }
javascript
15
[Function]
undefined
```

对于`Array`来说属性就是它的下标（在没有人为添加属性的前提下）。

(2). `for...of`循环，它是用于`iterable`类型。与`for...in`的区别在于它用于遍历的变量直接就是每个变量而非下标，比如：

```javascript
> var a = ['a', 'b', 'c'];
undefined
> for (var i in a) {
... console.log(a[i]);
... }
a
b
c
undefined
> for (var i of a) {
... console.log(i);
... }
a
b
c
undefined
```

(3). `forEach`方法，需要传入一个三参数的函数，如下：

```javascript
> var a = ['a', 'b', 'c'];
undefined
> a.forEach(function (element, index, array) {
    // element: 指向当前元素
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
    });
a, index = 0
b, index = 1
c, index = 2
undefined
```

### 5. 函数

(1). 定义函数（以绝对值函数为例），有多种形式：

```javascript
function abs(x) {
    if (x >= 0) {
        return x;
    }
    else {
        return -x;
    }
}
```

或者：

```javascript
var abs = function (x) {
    if (x >= 0) {
        return x;
    }
    else {
        return -x;
    }
}
```

还有种类似与`python`里的lambda表达式的定义方式，这里成为箭头函数，箭头前为参数，箭头后为函数体或返回值：

```javascript
var fn = x => x * x;
```

多参数时，用括号括起来：

```javascript
(x, y) => {
    return x * x + y * y;
}
```

如果想返回的是对象，则要用小括号括起来：

```javascript
x => ({foo : x})
```

(2). 参数：

`javascript`的函数接收的参数可以和定义的参数数量的不一样，这可能是和其他一些语言的区别，比如在`C`或`java`中这么做可能会报错，在`javascript`中可以执行，以上面定义的`abs`函数为例子：

```javascript
> function abs(x) {
        if (x >= 0) {
            return x;
        }
        else {
            return -x;
        }
    }
undefined
> abs(-10);
10
> abs(-10, 'haha');
10
> abs();
NaN
```

`javascript`有一个`arguments`参数，在函数内部使用，指向函数接收的所有参数的列表：

```javascript
> function foo(x) {
    console.log('x = ' + x);
    for (var i = 0; i < arguments.length; i++) {
        console.log('arg ' + i + ' : ' + arguments[i]);
    }
}
undefined
> foo(1, 2, 4, 5);
x = 1
arg 0 : 1
arg 1 : 2
arg 2 : 4
arg 3 : 5
undefined
```

`javascript`还有一个`rest`参数，用于存放剩余参数：

```javascript
> function foo(x) {
... console.log('x = ' + x);
... for (var i = 0; i < arguments.length; i++) {
..... console.log('arg ' + i + ' : ' + arguments[i]);
..... }
... }
undefined
> foo(1, 2, 4, 5);
x = 1
arg 0 : 1
arg 1 : 2
arg 2 : 4
arg 3 : 5
undefined
> function foo(a, b, ...rest) {
... console.log('a = ' + a);
... console.log('b = ' + b);
... console.log(rest);
... }
undefined
> foo(1,2,3,4,5);
a = 1
b = 2
[ 3, 4, 5 ]
undefined
> foo(1);
a = 1
b = undefined
[]
undefined
```

### 6. 正则表达式

关于正则表达式这里想说的不多，因为现在还不怎么会用到，要用到的时候再查就好了，现在只是掌握了最基本的定义方法：

```javascript
var reg1 = /^\w{3,9}$/;

// test用来匹配字符串，参数是要匹配的字符串
reg1.test('123456');        // true
```
