# Chapter 6 — 形式化关系查询语言
## 6.1 关系代数
关系代数是一种过程化查询语言，它包括一个运算的集合，这些运算以一个或两个关系作为输入，产生另一个新的关系作为结果。

### 6.1.1 基本运算
1. **选择运算**选出满足给定谓词的元组，用$\boldsymbol{\sigma}$来表示选择，将谓词写作$\sigma$的下标。

    - 例如选择关系*instructor*属于*Physics*的那些元组：

        <center>$\sigma_{dept\_name="Physics"}(instructor)$</center>
    
    - 通常在谓词中进行比较，使用的是$=, \not=, <, \leq, >, \geq$。另外可以使用连词$and(\land), or(\lor), not(\lnot)$。
    - 关系代数中的术语选择与SQL中的关键词*select*具有不一样含义，它对应与SQL中的*where*。
2. **投影运算**也是一元运算，它选择出我们希望的属性，并去重。投影用$\Pi$表示，在结果中出现的属性作为$\Pi$的下标。列出所有教师的*ID*、*name*和*salary*，而不关心*dept_name*：
    
    <center>$\Pi_{ID,name,salary}(instructor)$</center>
    
3. 可以把多个关系代数运算组合成一个**关系代数表达式**。
4. **并运算**用符号$\cup$，必须保证做运算的关系是相容的，要使运算$r \cup s$有意义，要求以下两个条件同时成立：
    - 关系$r$和$s$必须是同源的，即它们的属性数目必须相同。
    - 对所有的$i$，$r$的第$i$个属性必须和$s$的第$i$个属性的域相同。

5. **差运算**使得我们可以找出在一个关系中而不在另一个关系中的那些元组。形式为$r - s$。差运算也要满足相容性。
6. **笛卡尔积运算**，标准形式为$r_1 \times r_2$。
    - 它的关系模式是两个参与运算的关系模式的串联。
    - 假设$r_1$中有$n_1$个元组，$r_2$中有$n_2$个元组，$r_1 \times r_2$中有$n_1 \times n_2$个元组。
7. **更名运算**可以为关系附上另外的名字，利用$\rho$表示，下标表示用以更换的名字。

    - 返回表达式*E*的结果，并把名字$x$赋给它：

        <center>$\rho_x(E)$</center>

     - 更名运算的另一种形式，假设*E*是$n$元的，返回表达式*E*的结果，并赋给它名字，同时将各属性更名为$A_1, A_2, ..., A_n$：
     
        <center>$\rho_{x(A_1, A_2, ..., A_n)}(E)$</center>
        
    - 更名运算可以用来让同一个关系自己和自己的连接。

### 6.1.2 关系代数的形式化定义
1. 关系代数的基本表达式是如下二者之一：
    - 数据库中的一个关系
    - 一个常数关系

2. 关系代数中的一般表达式是由更小的子表达式构成的，设$E_1$和$E_2$是关系代数表达式，则以下这些都是关系代数表达式：

    - $E_1 \cup E_2$
    - $E_1 - E_2$
    - $E_1 \times E_2$
    - $\sigma_P(E_1)$
    - $\Pi_S(E_1)$
    - $\rho_x(E_1)$

### 6.1.3 附加的关系代数运算
1. **集合交运算**，用符号$\cap$连接两个关系，也要求满足关系的相容性等价形式如下：

    <center>$r \cap s = r - (r - s)$</center>
    
2. **自然连接运算**，用$\Join$来连接，设$r(R)$和$s(S)$是两个关系，自然连接的等价定义为：

    <center>$r \Join s = \Pi_{R \cup S}(\sigma_{r.A_1=s.A_1\land r.A_2=s.A_2\land ... \land r.A_n=s.A_n}(r \times s))$</center>
    
    其中$R \cap S = \{A_1, A_2, ..., A_n\}$。
    
3. **赋值运算**用$\gets$表示，与程序语言中的赋值类似，例如：

    <center>$temp1 \gets R \times S \\
                    temp2 \gets \sigma_{r.A_1=s.A_1\land r.A_2=s.A_2\land ... \land r.A_n=s.A_n}(temp1) \\
                    result = \Pi_{R \cup S}(temp2)$</center>
                    
    赋值的执行不会使得把某个关系显示给用户看，关系变量可以在后续的表达式中使用。
    
4. **外连接运算**是对连接运算的扩展，对输入的两个关系先进行自然连接，然后如果是**左外连接**(⟕)就取出左侧关系中不匹配的那些元组，再用空值填充来自右侧关系的属性。**右外连接**(⟖)则取出右侧关系的不匹配元组，用空值填充左侧属性。**全外连接**(⟗)则是上两种情况的合并。

### 6.1.4 扩展的关系代数运算
1. **广义投影**：通过允许在投影列表中使用算术运算和字符串函数来对投影进行扩展。运算形式为：

    <center>$\Pi_{F_1,F_2,...,F_n}(E)$</center>
    
    其中*E*是任意关系代数表达式，而$F_1, F_2, F_n$中的每一个都是涉及常量以及*E*的模式中的属性的算术表达式，它们可以使用表达式的+, -, *, /等代数运算。
    
2. **聚集**：聚集函数的输入值是一个汇集（多重集），将单一值作为结果返回。

    - 比如希望找出所有教师的工资总和：

        <center>$\mathcal{G}_{\boldsymbol{sum}(salary)}(instructor)$</center>
        
    - 有时想对输入进行去重，可以将**distinct**附加在函数名后（如**count-distinct**）。
    - 如果是给多分组聚集，比如"求出每个系的平均工资"：

        <center>$_{dept\_name}\mathcal{G}_{\boldsymbol{average}(salary)}(instructor)$</center>
        
    - **聚集运算**$\mathcal{G}$通常的形式为：

        <center>$_{G_1,G_2,...,G_n}\mathcal{G}_{F_1(A_1),F_2(A_2),...,F_m(A_m)}(E)$</center>
        
## 6.2 元组关系演算
1. 元组关系演算是**非过程化的**查询语言。
2. 它只描述所需信息，而不给出获得该信息的具体过程。
3. 元组关系演算中的查询表达为：
    
    <center>$\{ t | P(t)\}$</center>
    
    也就是它是所有使谓词$P$为真的元组$t$的集合。
4. 我们用t[A]表示元组t在属性A上的值。

### 6.2.1 查询示例

1. 比如"找出所有工资在80000美元以上的教师ID、name、dept_name和salary"：

    <center>$\{t|t\in instructor \land t[salary] > 80000\}$</center>
    
2. 如果想要投影，即不需要表中所有的属性，需要引入"存在"，表示"关系r中存在元组t使谓词Q(t)为真"：

    <center>$\exists\,t \in r(Q(t))$</center>
    
4. 可以用如下方式表示投影，比如"找出工资大于80000美元的所有教师的ID"：

    <center>$\{t|\exists\,s \in instructor(t[ID]=s[ID] \land s[salary] > 80000)\}$</center>
    
5. 涉及到多个表时，比如"找出位置在Waston楼的系中的所有教师姓名"：

    <center>$\{t|\exists\,s \in instructor(t[name]=s[name] \\
                               \qquad \land \exists\,u \in department(u[dept\_name]=s[dept\_name] \\
                                \qquad \land u[building]="Waston"))\}$</center>
                                
6. 公式$P \Rightarrow Q$表示"P蕴含Q"，即"如果P为真，则Q必然为真"。$P \Rightarrow Q$逻辑上等价于$\lnot P \lor Q$。

7. 引入全程量词，用$\forall$表示，"对关系r中所有的元组t，Q均为真"：

    <center>$\forall t \in r(Q(t))$</center>
    
8. 查询"所有选择了生物系全部课程的学生"，用描述性语言说"它是所有满足如下条件的学生(即(ID)上的元组t)的集合：对关系course中的所有元组u，如果u在dept_name属性上的值是'Biology'，那么在关系takes中一定存在一个包含该学生ID以及该课程course_id的元组"：

    <center>$\{t|\exists\,r\in student(r[ID]=t[ID]) \land \\
                        \qquad \forall\, u \in course(u[dept\_name]="Biology" \Rightarrow \\
                        \qquad \exists\, s \in takes(t[ID]=s[ID] \\
                        \qquad \land s[course\_id]=u[course\_id]))\}$</center>
                        
### 6.2.2 形式化定义
1. 上述元组关系表达式中，P是一个公式，公式中可以出现多个元组变量。如果元组变量不被$\exists$或$\forall$修饰，则称为**自由变量**，否则称为**受限变量**。
2. 公式由*原子*构成，原子可以是如下形式之一：

    - $s \in r$，其中s是元组变量而r是关系（不允许使用$\notin$运算符）。
    - $s[x]\ \Theta\ u[y]$，其中s和u是元组变量，x是s的属性，y是u的属性，$\Theta$是比较运算符。
    - $s[x]\ \Theta\ c$，与上类似，c是x域中的一个常量。
    
    利用原子构造公式的规则：
    
    - 原子是公式。
    - 如果$P_1$是公式，那么$\lnot\, P_1和(P_1)$也都是公式。
    - 如果$P_1$和$P_2$是公式，那么$P_1 \lor P_2、P_1 \land P_2$和$P_1 \Rightarrow P_2$也都是公式。
    - 如果$P_1(s)$是包含自由元组变量s的公式，且r是关系，则

        <center>$\exists\, s \in r(P_1(s))和\forall\, s \in r(P_1(s))$</center>
        
        也都是公式。
        
## 6.3 域关系演算
### 6.3.1 形式化定义
1. 域关系演算中的表达式形式如下：

    <center>$\{<x_1, x_2, ..., x_n > | P(x_1, x_2, ..., x_n)\}$</center>
    
    其中$x_1, x_2, ..., x_n$代表域变量。和元组关系演算的情况一样，P代表由原子构成的公式。
    
2. 原子形式如下：

    - $<x_1, x_2, ..., x_n> \in r$，其中r是n个属性上的关系，而$x_i$是域变量或常量。
    - $x \Theta y$，其中x和y是域变量，$\Theta$是比较运算符。
    - $x \Theta c$，其中c是x作为域变量的那个属性域中的常量。

3. 公式构造规则：

    - 原子是公式。
    - 如果$P_1$是公式，那么$\lnot P_1和(P_1)$也都是公式。
    - 如果$P_1和P_2$是公式，那么$P_1 \lor P_2、P_1 \land P_2和P_1 \Rightarrow P_2$也都是公式。
    - 如果$P_1(x)$是x的一个公式，其中x是自由域变量，则

        <center>$\exists\, x(P_1(x))和\forall\, x(P_1(x))$</center>
        
        也都是公式。
        
4. 把$\exists\, a, b, c(P(a, b, c))$作为$\exists\,a(\exists\, b(\exists\, c(P(a, b, c))))$的简写。

### 6.3.2 查询例子
1. 找出工资在80000美元以上的教师ID、name、dept_name和salary：

    <center>$\{<i, n, d, s>|<i, n, d, s> \in instructor \land s > 80000\}$</center>
    
2. 找出工资大于80000美元的所有教师的姓名：

    <center>$\{<i>|<i, n, d, s> \in instructor \land s > 80000\}$</center>
