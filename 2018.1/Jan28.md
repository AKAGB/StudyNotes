# JavaScript的面向对象

Author: Dream_hh

Date: 2018-1-28

------

## 一、面向对象(OOP)

关于面向对象在学习C++、Java还有Python等语言的时候都有过接触，面向对象的核心在于三个层次，即**封装**、**继承**和**多态**。这三个概念这里不再过多解释，都是些基本概念。JavaScript的OOP和之前说的三种语言有些许不同（前三个主要基于类和对象，而JS是基于原型这个概念），主要应该掌握如何去写代码，以及初步了解JavaScript的OOP的原理。


## 二. JS的OOP

### 1. 构造函数

前面已经讲过对象是如何构建的，如果我想把它放进函数里该怎么做呢？我们很自然的会想到用这样的方法（以一个`Person`对象为例）：

```javascript
function createPerson(name) {
    var obj = {};
    obj.name = name;
    obj.greeting = function () {
        alert('Hi! I\'m ' + this.name + '.');
    };
    return obj;
}

// 创建一个 name 为　xiaoming　的对象
var xiaoming = createPerson('xiaoming');
```

但这种方法可能过于冗长了，JavaScript有一种更简洁的写法：

```javascript
function Person(name) {
    this.name = name;
    this.greeting = function() {
        alert('Hi! I\'m ' + this.name + '.');
    };
}

// 创建一个 name 为　xiaoming　的对象
var xiaoming = new Person('xiaoming');
var xiaohong = new Person('xiaohong');
```

这个构造函数就相当于别的语言的`class`（事实上后来JS也出了一种`class`的写法，这个后面会讲），虽然它的本质还是`function`，可以用`typeof`查看。注意到它的调用方式是关键字`new`后面加上函数。

这里创建了两个对象，`xiaoming`和`xiaohong`是两个对象，它们的`name`属性和`greeting()`方法是相互独立的，换句话说，它在内存里开了存储这两个对象的空间。

另外还有其他构造对象的方法，比如`Object.create(obj)`方法，它会基于obj对象返回一个具有相同属性和方法的对象，但这个方法只能在较新的浏览器中使用。

### 2. 对象原型(prototype)

在了解继承之前，必须要先知道什么是原型，JavaScript是一种**基于原型的语言(prototype-based language)**。每一个对象都拥有一个**原型对象**，对象以它的原型为模板，继承原型的方法和属性，注意这里的描述，原型本身其实也是一个对象，因此原型对象也拥有原型，这样就形成了一条链状结构，我们称这条链为**原型链**。

传统的OOP语言，它们是构造一个类(class)，然后基于类创建了对象，对象会复制类中所有的属性和方法。但在JavaScript中并非如此，它是在对象和构造函数(`constructor function`)建立了链接，对象实例的属性和方法其实是定义在构造器的`prototype`属性（构造函数的`prototype`属性其实就是对象实例的原型对象）上，而非对象本身，比如说当调用对象实例的方法时，由于它本身并没有这个方法的定义，JS会沿着原型链逐一向上查找有没有该方法，当查到它的构造函数的`prototype`属性（即原型对象）有该方法时就会调用，否则继续沿着原型链查找。
