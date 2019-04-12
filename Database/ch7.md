#Chapter 7 — 数据库设计和E-R模型
## 7.1 设计过程概览
### 7.1.1 设计阶段
设计数据库基本要遵循以下步骤：
1. **数据需求分析**：最初阶段需要完整地刻画未来数据库用户的数据需求。
2. **选择模型**：设计者选择数据模型，并采用数据模型的概念将这些需求转化为数据库的概念模式。
3. **功能需求规格说明**：用户描述将在数据上进行的各类操作（或事务）。
4. **抽象数据模型到数据库实现的转换**：
    - **逻辑设计阶段**：设计者将高层概念模式映射到将使用的数据库系统的实现数据模型上。
    - **物理设计阶段**：指明数据库的物理特征，包括文件组织格式和索引结构的选择。

### 7.1.2 设计选择
1. 使用**实体（entry）**这个术语来只是所有可明确识别的个体。
2. 设计一个数据库模式的时候，必须避免两个主要的缺陷：

    - **冗余**：一个不好的设计可能会重复信息，信息的冗余表达最大问题是当对一条信息进行更新但没有将这条信息的所有拷贝都更新时，就会产生**数据不一致**问题。
    - **不完整**：一个不好的设计可能会使得企业机构的某些方面难于甚至无法建模。例如只有对应开课的实体，但没有课程这个实体的话，就会面临有些还没有开的新课程信息无法存储。

3. 不仅要避免不好的设计，还必须从大量好的设计里面选择一个，选择应根据实际的需求。

## 7.2 E-R模型
**实体-联系（E-R）模型**的提出旨在方便数据库的设计，它是通过允许定义代表数据库全局逻辑结构的企业模式实现的。

### 7.2.1 实体集
1. **实体**是现实世界中可区别于所有其他对象的一个"事物"或"对象"。
2. **实体集**是相同类型即具有相同性质（或属性）的一个实体集合。术语实体集的**外延**来指属于实体集的实体的实际集合。
3. 实体通过一组**属性**来表示，属性是实体集中每个成员所拥有的描述性性质。
4. 每个实体的每个属性都有一个值。
5. 数据库包括一组实体集，每个实体集包括任意数量的相同类型的实体。

### 7.2.2 联系集
1. **联系**是指多个实体间的相互联系。
2. **联系集**是相同类型的联系的集合，正规地说，联系集是$n \geq 2$个（可能相同的）实体集上的数据关系。如果$E_1, E_2, ..., E_n$为实体集，那么联系集$R$是

    <center>$\{(e_1, e_2, ..., e_n) | e_1 \in E_1, e_2 \in E_2, ..., e_n \in E_n\}$</center>
    
    的一个子集，而$(e_1, e_2, ..., e_n)$是一个联系。
3. 实体集之间的关联称为参与，也就是说，实体集$E_1, E_2, ..., E_n$**参与**联系集$R$。
4. 实体在联系中扮演的功能称为实体的**角色**。一般不指定，但对于**自环的**联系集需要用显示的角色名来指明实体是如何参与联系实例的。
5. 联系也可以具有**描述性属性**。
6. 给定联系集中的一个联系实例必须是由其参与实体唯一标识的，而不必使用描述属性。
7. 参与联系集的实体集的数目称为联系集的**度**。

### 7.2.3 属性
1. 每个属性都有一个可取值的集合，称为该属性的**域**，或者**值集**。
2. 正规地说，实体集的属性是将实体集映射到域的函数。
3. E-R模型中的属性可以按照如下属性的类型来划分：

    - **简单和复合属性**：简单属性就是不能划分为更小的部分，复合属性则是可再划分，例如属性*name*可以设计为包括*first_name*、*middle_name*和*last_name*的复合属性。
    - **单值和多值属性**：单值属性只能对应一个值，而多值属性可以对应多个值，比如一个老师可能有有多个phone_number。
    - **派生属性**：这类属性的值可以从别的相关属性火实体派生出来，例如instructor实体集具有age属性，这个属性可以通过当前日期和date_of_birth属性计算出来。

4. 当实体在某个属性上没有值时使用空值（null），表示"不适用"。


## 7.3 约束
### 7.3.1 映射基数
1. 映射基数表示一个实体通过一个联系集能关联的实体个数。
2. 对于二元联系集，映射基数必然是以下情况之一：
    - 一对一
    - 一对多
    - 多对一
    - 多对多

### 7.3.2 参与约束
如果实体集E中的每个实体都参与到联系集R的至少一个联系中，则称E**全部**参与R，否则是**部分**参与。

### 7.3.3 码
1. 一个实体的属性的值必须可以唯一标识该实体。一个实体集不允许存在两个实体对于所有属性都具有完全相同的值。
2. 可套用第二章中的超码、候选码、主码等概念。
3. 联系集R的超码有以下两种情况：

    - R没有属性：$pk(E_1) \cup pk(E_2) \cup ... \cup pk(E_n)$
    - R有属性：$pk(E_1) \cup pk(E_2) \cup ... \cup pk(E_n) \cup \{a_1, a_2, ..., a_n\}$

4. 联系集的主码结构依赖于联系集的映射基数：
    - 如果是多对多，主码是两个实体集主码的并。
    - 如果是多对一或一对多，则选择"一"的主码作为联系集主码。
    - 如果是一对一则任选一个实体集的主码作为联系集主码。

### 7.4 从实体集中删除冗余属性
联系集有可能会导致不同实体集中的属性冗余，并需要将其从原始的实体集中删除。

## 7.5 E-R图
**E-R图**可以图形化地表示数据库的全局逻辑结构。

### 7.5.1 基本结构
E-R图包括以下几个主要的构件：

- **分成两部分的矩形**代表实体集。
- **菱形**代表联系集。
- **未分割的矩形**代表联系集的属性，构成主码的属性以下划线标明。
- **线段**将实体集连接到联系集。
- **虚线**将联系集属性连接到联系集。
- **双线**显示实体集在联系集中的参与度。
- **双菱形**代表连接到弱实体集的标志性联系集。

### 7.5.2 映射基数
箭头指向"一"的实体集，"多"则无箭头，只是普通实线线段。

### 7.5.3 复杂的属性
如下图所示：
![](media/15464271571864.jpg)
### 7.5.4 角色
在连线上标注：

![](media/15464272490879.jpg)
### 7.5.5 非二元的联系集

非二元的联系集通常也能转化为二元联系集：

![](media/15464273832701.jpg)

### 7.5.6 弱实体集
1. **弱实体集**是指没有足够的属性形成主码的实体集。
2. 弱实体集必须与另一个称作**标识**或**属主实体集**的联系集关联才能有意义。