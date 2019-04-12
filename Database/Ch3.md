# Chapter 3 — SQL

## 3.1 SQL语言概览
SQL语言有以下几个部分：

- 数据定义语言（DDL）：提供定义关系模式、删除关系模式以及修改关系模式的命令。
- 数据操纵语言（DML）：提供从数据库中查询信息，以及在数据库中插入元组、删除元组、修改元组的能力。
- 完整性：DDL包括定义完整性约束的命令，保存在数据库中的数据必须满足所定义的完整性约束。破坏完整性约束的更新是不允许的。
- 视图定义：DDL包括定义视图的命令。
- 事务控制：包括定义事务开始和结束的命令。
- 嵌入式SQL和动态SQL：定义SQL语言如何嵌入到通用编程语言中。
- 授权：DDL包括定义对关系和视图的访问权限的命令。

## 3.2 SQL数据定义
1. SQL标准支持多种固有类型：固定长度字符串char(n)，可变长度字符串varchar(n)，整数类型int，小整数类型smallint，定点书numeric(p,d)（p位数字，d位在小数点右侧），浮点数和双精度浮点数real/double precision，精度至少为n的浮点数float(n)。
2. 基本模式定义，利用`create table`命令定义SQL关系，通用形式是：

    ```sql
    Create table r 
        (A1 D1,
        A2 D2,
        ...,
        An Dn,
        <完整性约束1>,
        ...,
        <完整性约束k>,
        );
    ``` 
3. 常见的完整性约束：
    - **primary key**(Aj1, Aj2, ..., Ajm)：声明由属性Aj1，Aj2，...，Ajm构成的主码。
    - **foreign key** (Ak1, Ak2, ..., Akn) **references**：声明表示关系中任意元组在属性(Ak1, Ak2, ..., Akn)上的取值必须对应于关系s中的某元组在主码属性上的取值。
    - **not null**：一个属性上的**not null**约束表明在这个属性上不允许空值。
4. 插入元组：**insert into** r **values** (...)。
5. 删除元组：**delete from** r **where** [谓词]。
6. 删除表：**drop table** r。
7. 为已有关系添加属性：**alter table** r **add** A D，A为属性名，D为域。
8. 从关系中删除属性：**alter table** r **drop** A。

## 3.3 SQL查询的基本结构

### 3.3.1 单关系查询
1. 标准形式：

```sql
select A
from r
where P
```
2. SQL允许结果中出现重复，可以用**distinct**显式去重，也可以用**all**显式不去重。
3. **select**子句可以带含有+、-、*、/运算符的算术表达式。
4. **where**子句允许我们只选出那些在**from**子句的结果关系中满足特定谓词的元组。

### 3.3.2 多关系查询
1. 标准形式：

```sql
Select A1, ..., An
From r1, ..., rm
Where P
```
Ai表示属性，ri表示关系，P表示谓词。
2. **select**子句用于列出查询结果中所需要的属性。
3. **from**子句是一个查询求值中需要访问的关系列表，它定义的是关系的笛卡尔积。
4. **where**子句是一个作用在**from**子句中关系的属性上的谓词，用来限制笛卡尔积所建立的组合。

### 3.3.3 自然连接
1. SQL支持自然连接运算，**自然连接（natural join）**所用语两个关系，并产生一个关系作为结束。
2. 自然连接只考虑那些在两个关系模式中都初心啊的属性上取值相同的元组对。
3. 标准形式：

```sql
select A1, ..., An
from r1 natural join r2 natural join ... natural join rm
where P;
```

4. 用户也可以指定让哪些属性相等，而非所有相同属性都相等：

```
Select A1, ..., An
From r1 join r2 using (Aj1, Aj2, ..., Ajm)
Where P
```

## 3.4 附加的基本运算
### 3.4.1 更名运算
1. **as**可以用来给table或属性更名，一般来说有两种作用，一是用一个短的别名，而是更换角色。
2. **as**可以省略，即直接用空格分开原名和别名。

### 3.4.2 字符串运算
1. 判断相等（=），无视大小写，但可以在数据库系统的设置里改。
2. 串联、提取子串、计算字符串长度等可以在数据库系统手册中查看。
3. 用**like**操作符来实现字符串模式匹配，**模式是大小写敏感的**，以下特殊字符描述模式：
    - 百分号（%）：匹配任意子串。
    - 下划线（_）：匹配任意一个字符。
4. 使用**escape**关键字**定义**转义字符。
5. 使用**not like**搜索不匹配项。

### 3.4.3 select子句中的属性说明
1. 可以用*表示所有的属性，如`select instructor.*`或`select *`。

### 3.4.4 排序
1. 使用**order by**子句默认使用升序，例如：

```sql
Select name 
From instructor
Where dept_name='Physics'
Order by name
```

2. 用**desc**表示降序，**asc**表示升序。如`order by name desc`。

### 3.4.5 where子句谓词
1. 可以用=、<>、<、>、<=、>=等运算符。
2. 可以用and、or、not逻辑连词。

## 3.5 集合运算
1. 使用**r1 union r2**表示并运算，将两个关系模式相同的表合并，并自动去重。如果想保留重复，就要使用**r1 union all r2**。
2. 使用**r1 interest r2**表示交运算，自动去重，如果想保留重复就用**r1 interect all r2**。
3. 使用**r1 except r2**表示差运算，同上，可加**all**不去重。

## 3.6 空值

1. 数据库中的逻辑值有3种：*true*, *false*, *unknown*。
2. and, or, not的运算规则和以前一样。
3. **is null**所用的值为空则为true，否则为false。**is not null**同理。

## 3.7 聚集函数
### 3.7.1 基本聚集

- 平均值：**avg**。
- 最小值：**min**。
- 最大值：**max**。
- 总和：**sum**。
- 计数：**count**。

如果不加**group by**则是对所有的元组聚集。

### 3.7.2 分组聚集
**group by**子句的作用是按照属性分组，把属性值相同的元组聚成一个元组，因此要求select子句中的属性只能是**group by**中的属性或聚集函数。

### 3.7.3 having子句
**having**子句是针对**group by**子句的谓词，所以必须在有**group by**的时候使用，且与select类似，任何在having中出现的属性除了聚集函数，必须要在group by子句中出现。

### 3.7.4 对空值和布尔值的聚集
1. 对空值的处理原则：除了**count(*)**外所有的聚集函数都忽略空值。规定空集的count运算返回0，其他运算返回空值。
2. 布尔值有两个聚集函数**some**和**every**。

## 3.8 嵌套子查询
1. 子查询是嵌套在另一个查询中的**select-from-where**表达式。
2. 子查询嵌套在**where**子句中，通常用于对集合的成员资格、集合的比较以及集合的基数进行检查。

### 3.8.1 集合成员资格
1. 连接词**in**测试元组是否在集合中的成员，集合是由**select**子句产生的一组值构成的。**not in**反之。
2. 标准形式：

```sql
select ...
from ...
where (A1, ..., An) in (select (A1, ..., An)
                    from ...
                    where ...)
```

3. **in**和**not in**也可以用于枚举集合：

```sql
Select ...
From ...
Where A in (a1, ..., an)
```

### 3.8.2 集合的比较
1. 短语"至少比某一个要大"在SQL中用"**>some**"来表示：

```sql
Select ...
From ...
Where A > some(select A
                            From ...
                            Where ...)
```

2. 短语"比所有的都大"在SQL中用"**>all**"来表示，用法与上同。
3. **>=all, <=all, <all, <>all, >= some, <=some, <some, <>some**同理。

### 3.8.3 空关系测试
1. **exists**在作为参数的子查询返回非空时返回**true**。
2. 来自外层查询的一个相关名称可以用在**where**子句的子查询中，使用了来自外层查询相关名称的子查询被称作**相关子查询**。
3. **not exists**模拟集合的包含操作。可将"关系A 包含关系B"写成"**not exists(B except A)**"，可用逻辑运算推导出这个结果。

### 3.8.4 重复元组存在性测试
**unique**结构用于检测子查询是否有重复元素，如果有则返回true。**not unique**反之。

### 3.8.5 from子句中的子查询
1. 由于任何**select-from-where**表达式的返回结果是关系，所以在SQL中子查询可以出现在任何关系可以出现的位置。
2. **from**子句嵌套的子查询中不能使用来自**from**子句其他关系的相关变量。

### 3.8.6 with子句
**with**子句提供定义临时关系的方法，这个定义只能对包含**with**子句的查询有效。例子：

```sql
With max_budget (value) as 
    (Select max(budget)
    From department)
Select budget
From department, max_budget
Where department.budget = max_budget.value
```

### 3.8.7 标量子查询
SQL允许子查询出现在返回单个值的表达式能够出现的任何地方（例如select子句中），只要该子查询只返回包含单个属性的单个元组，这样的子查询称为**标量子查询**。

## 3.9 数据库的修改
### 3.9.1 删除
标准形式：

```sql
Delete from r
Where P;
```

### 3.9.2 插入
标准形式：

```sql
Insert into r
    Values(a1, a2, ..., an)
```

### 3.9.3 更新
标准形式：

```sql
Update r
Set A = a
Where P
```
