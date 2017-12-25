# HTML&CSS学习

data: 2017-12-3

author: dreamgqk

----------

## 一、CSS选择器

### 1. 标签选择器

前面用过了，比较简单这里不做特别说明。

### 2. 类选择器

可以用类名做选择器，即**类选择器**，比如有这么一个标签：

`<p class="guarantee">...</p>`

一个`class`(这里类名叫做`guarantee`)可能包含了很多的标签，如果想让这些标签有一个统一的样式，可以这样写：

```css
.guarantee {
    ...
}
```

即用 **.classname** 作为选择器的名字。

### 3. ID选择器

我们知道`class`属性可以把标签分到一个组里，而`id`属性是标签的唯一标识，所以当我们想给某一个标签单独使用特殊样式的时候，理所应当想到`id`属性，这就是所谓的**ID选择器**。比如：

`<p id="test">...</p>`

那么ID选择器为：

```css
#test {
    ...
}
```

### 4. 子孙选择器

语法也很简单，用空格分隔开父元素和子孙元素。比如有这样的HTML:

```html
<body>
    ...
    <h2>..</h2>
    <div id="example">
        <h2>..</h2>
    </div>
    ...
</body>
```

如果相对`<div>`里面的`<h2>`元素选择而不影响`<div>`外的`<h2>`，这时候就可以用到子孙选择器了，用法如下：

```css
div h2 {
    ...
}
```

父元素和子孙元素之间用空格分开，但这样有个问题，如果刚好有别的`<div>`下也有`<h2>`，而你又不想在那里用相同的样式该怎么做呢，当然继续套用前面类选择器和ID选择器的规则，这里以`id="example"`为例:

```css
#example h2 {
    ...
}
```

上面那些都是对子孙进行选择，如果只想对直接的孩子选择，那么可以这样：

```css
#example>h2 {
    ...
}
```

### 5. 还有更多的一些选择器（其中包括最重要的伪类选择器）在后面

再复杂一点，如果是对某个子标签的子孙选择，比如刚刚的`#example`下有一个`<blockquote>`孩子，我只想对他里面的`<h2>`进行选择，则：

```css
#example blockquote h2 {
    ...
}
```

## 二、`<div>`和`<span>`元素

这两个东西其实就像是C语言里面的结构体，对于一些基本的数据用struct进行定制成一个新的数据类型，我认为`div`和`span`可能也有一些这样的思想在里面，对于一些基本的标签，如果你认为他们是归属于某一个逻辑结构，即对你的HTML文件进行一些逻辑分区（有结构感的去看待它，而不只是把它看成一个一个的基本标签，如果了解过类和对象或者结构体这种东西应该会觉得这是一件很自然的事）。`<div>`和`<span>`的区别在于，前者是块元素，后者是内联元素。

### 1. `<div>`元素

举个简单的例子，比如在一个宠物店的一个网页上，有各种标题段落，有关于猫的、狗的等等，和猫相关的标题、段落、图片等元素你可以认为他们是一个逻辑结构，就可以用一个`<div>`标签把它们全部包含起来，为了表示可以加上`id`属性，狗的相关元素也可以这么做，那么这个HTML页面就会变成这个样子：

```html
    ...
    <body>
        ...
        <div id="pets">
            <div id="cats">
                <!-- 一些标题、段落或图片 -->
            </div>

            <div id="dogs">
                <!-- 一些标题、段落或图片 -->
            </div>
        </div>
        ...
    </body>
    ...
```

当然如果还有更高的层次的逻辑结构也可以继续用`<div>`，比如上面的`<div id="pets">`把包含了dogs和cats，当然也不要滥用`<div>`，否则会使页面的结构更加复杂。

### 2. `<span>`元素

基本用法与`<div>`元素一样，只不过它是内敛元素。比如我想对一个段落中的某些文字选择同样的样式，如果有办法对他们划分为一个类的标签就好了，所以就有了`<span>`。

比如有如下HTML代码：

```html
<ul>
    <li>Buddha Bar, Claude Challe</li>
    <li>When It Falls, Zero 7</li>
    <li>Earth 7, L.T.J. Bukem</li>
    <li>Le Roi Est Mort, Vive Le Roi!, Enigma</li>
    <li>Music for Airports, Brian Eno</li>
</ul>
```

这是一个列表，逗号前是CD，后面是艺术家，如果想让CD斜体，艺术家加粗，这时候就要用到`<span>`来对他们“包装”。

如下：

```html
<ul>
    <li><span class="cd">Buddha Bar</span>, <span class="artist">Claude Challe</span></li>
    <li><span class="cd">When It Falls</span>, <span class="artist">Zero 7</span></li>
    <li><span class="cd">Earth 7</span>, <span class="artist">L.T.J. Bukem</span></li>
    <li><span class="cd">Le Roi Est Mort</span>, <span class="artist">Vive Le Roi!, Enigma</span></li>
    <li><span class="cd">Music for Airports</span>, <span class="artist">Brian Eno</span></li>
</ul>
```

然后就能用CSS对它们的样式进行修改了。

## 三、混合样式表

所谓混合样式表就是引入了多个样式表。

### 1. 冲突解决方案

前面其实也看到过，如果对一个标签有多个选择器，就有可能产生冲突，这是它就需要有一个优先级。这里的层次更高一点，如果在多个css文件中都对某一个标签进行了选择，如果发生了冲突，该如何确定优先级呢？根据引入样式表的顺序，即`<link>`标签的顺序。比如有corproate.css、beverage.css、lounge-seattle.css三个样式表，而在html文件中按照如下顺序引入：

```html
<link type="text/css" href="corproate.css" rel="stylesheet">
<link type="text/css" href="beverage.css" rel="stylesheet">
<link type="text/css" href="lounge-seattle.css" rel="stylesheet">
```

如果他们三个对同一个标签都进行了选择，并且某些属性发生了冲突（没冲突的属性就直接使用），对于冲突的属性优先级为：lounge-seattle.css > beverage.css > corproate.css。所以对于混合样式表来说，**顺序** 是非常重要的。一般来说，越早引入的样式表应该越通用。

这里介绍的是当没有任何条件或条件满足的情况下的优先级。但如果我对引入的样式表有特殊要求呢？即在不同情况下使用不同样式表，继续往下。

### 2. 面向设备的样式表

有时候使用混合样式表可能是因为想针对不同的设备有不同的样式，比如PC、笔记本、平板电脑、手机或打印机，专业的说法这叫做**CSS媒体查询**。这里提供两种方法进行选择，这里只做简单介绍，详细内容参考[CSS媒体查询](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Media_queries)。

比如我想选择设备是计算机屏幕且最大宽度为800px的设备。有如下两种做法：

(1). `<link>`的`media`属性。

`<link rel="stylesheet" media="screen and (max-width: 800px)" href="example.css">`

(2). 样式表中的`@media`。

```css
@media screen and (max-width: 800px) {
    /*这里是样式的定义*/
}
```

这两种做法是等价的，但一般来讲会选择第一种，因为第二种可能会让css文件变得更加复杂。

这里再具体讲一下刚刚那些值的含义，`media`或`@media`后面的那一串可以看作是逻辑表达式，即当逻辑表达式的值为true时就选择这个css。

看到了有`and`，它是与逻辑运算符，当然还有或(用逗号`,`而不是`or`)、非(`not`)。关于有哪些媒体特征（刚刚出现的`screen`和`(max-width: 800px)`）可以去看刚刚给的网址，里面的说明比较详细。

## 四、CSS属性补充：

记得前面讲的设置盒子几个部分的属性，比如内边距的`padding-left`、`padding-right`等就可以写出上下左右四个属性，一个一个写可能会觉得太过于冗长，其实这些属性往往都有一些简写。参考[CSS的简写属性](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Shorthand_properties)。

(1). `background`属性

background 学了4个属性，它的简写不考虑顺序，比如：

```css
.example {
    background-color:    #a7cece;
    background-image:    url(images/background.gif);
    background-repeat:   no-repeat;
    background-position: top left;
}
```

把它们简写为：

```css
.example {
    background: #a7cece url(images/background.gif) no-repeat top left;
}
```

(2). `font`属性

font 的5个属性：

```css
.example {
    font-style:  italic;
    font-weight: bold;
    font-size:   .8em;
    line-height: 1.2;
    font-family: Arial, sans-serif;
}
```

虽然它依然不用考虑顺序，但尽量按照这个简写结构：`font: font-style font-variant font-weight font-size/line-height font-family`

前三个和`line-height`是可选的，前三个的顺序并不重要，但必须出现在`font-size`之前。之前并没有了解过`font-variant`，不过它很简单，自己测试下就可以了，给个链接[CSS font-variant 属性](http://www.w3school.com.cn/cssref/pr_font_font-variant.asp)。回到我们的例子，他可以简写为：

```css
.example {
    font: italic bold .8em/1.2 Arial, sans-serif;
}
```

(3). `border`属性

依旧是用一个例子，它不考虑属性之间顺序：

```css
.example {
    border-width: 1px;
    border-color: gray;
    border-style: solid;
}
```

简写为：

```css
.example {
    border: 1px solid gray;
}
```

(4). `margin`和`padding`属性：

顺序是从上右下左，其实`border-radius`也可以简写，只不过是从左上角开始顺时针。

```css
.example {
    margin-top:    10px;
    margin-right:  9px;
    margin-bottom: 8px;
    margin-left:   7px;
}
```

简写后：

```css
.example {
    margin: 10px 9px 8px 7px;
}
```

`padding`和`border-radius`同理，实际上还有一些规则关于他们部分属性值相同的简写，但我觉得有点复杂了其实没必要记，除了全相同的情况，比如4个外边距全是10px，那么可以简写为：

```css
.example {
    margin: 10px;
}
```
