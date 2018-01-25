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

(2). `for...of`循环，它是用于`iterable`类型。
