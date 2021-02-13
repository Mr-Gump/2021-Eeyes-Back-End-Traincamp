

# `MySQL`

[TOC]

## 一、数据库   

关系型数据库   非关系型数据库

`Oracle`  贵|支持服务|稳定,高校   MySQL SQLServer   DB2  MongoDB Access  MariaDB

Reddis

Cluster  集群

### 1.常见概念

1. `DB`：数据库，存储数据的容器
2. `DBMS`：数据库管理系统，又称为数据库软件或数据库产品，用于创建或管理DB
3. `SQL`：结构化查询语言，用于和数据库通信的语言，不是某个数据库软件特有的，而是几乎所有的主流数据库软件通用的语言

### 2.`MySQL`

 ![“Mysql”的图片搜索结果](https://upload.wikimedia.org/wikipedia/zh/6/62/MySQL.svg)

#### 2.1 背景

+ 前身属于瑞典的一家公司，MySQL AB
+ 08年被sun公司收购
+ 09年sun被oracle收购

#### 2.2 `MySQL`登录和退出

3306   80  25  22  3389  21  443

+ 登录：`mysql 【-h 主机名 -P 端口号】 -u用户名 -p密码`
+ 退出：`exit`或`ctrl+C`

#### 2.3 查看字符集

```sql
SHOW VARIABLES LIKE "CHARACTER%";  
SHOW VARIABLES LIKE "COLLATION_%";
```

#### 2.4 **`utf8` 和 `utf8mb64` 

+ `utf8`比`utf8mb64`占用字节少
+ `utf8mb64`可以用来存储特殊字符和表情

![image-20210117190632555](C:\Users\24246\AppData\Roaming\Typora\typora-user-images\image-20210117190632555.png)

## 二.`SQL`语言  `Structured Query Language`

创建 增删改查

#### 1.按照功能划分

| 划分 |     功能     |     主要负责     |
| :--: | :----------: | :--------------: |
| DQL  | 数据查询语言 |      查数据      |
| DDL  | 数据定义语言 | 创建，删除库\|表 |
| DML  | 数据操作语言 |  增，删数据，改  |
| TCL  | 事务控制语言 |    事务，视图    |



## 三、`SQL`语法

### 1.`DQL`语法

#### 1.1 基础查询

##### 1.1.1 语法

print

```sql
select 查询列表
from 表名;
```



##### 1.1.2 特点

1. 查询列表可以是字段、常量、表达式、函数，也可以是多个
2. 查询结果是一个虚拟表

##### 1.1.3 示例

1. 查询单个字段
    `select 字段名 from 表名;`
2. 查询多个字段
    `select 字段名，字段名 from 表名;`
3. 查询所有字段
    `select * from 表名`
4. 查询常量
    `select 常量值;`
    注意：字符型和日期型的常量值必须用单引号引起来，数值型不需要
5. 查询函数
    `select 函数名(实参列表);`
6. 查询表达式
    `select 100/1234;`
7. 起别名
    ①as
    ②空格
8. 去重
    `select distinct 字段名 from 表名;`

##### 1.1.4 补充

1. 做加法运算
    `select 数值+数值;` 直接运算
    `select 字符+数值;`先试图将字符转换成数值，如果转换成功，则继续运算；否则转换成0，再做运算
    `select null+值;`结果都为null
2. `concat`函数
    功能：拼接字符
    `select concat(字符1，字符2，字符3,...);`
3. `ifnull`函数
    功能：判断某字段或表达式是否为null，如果为null 返回指定的值，否则返回原本的值
    `select ifnull(commission_pct,0) from employees;`
4. `isnull`函数
    功能：判断某字段或表达式是否为null，如果是，则返回1，否则返回0

#### 1.2 条件查询

##### 1.2.1 语法

```sql
select 查询列表
from 表名
where 筛选条件
```



##### 1.2.2 筛选条件的分类

1. 简单条件运算符   `<` `=` `<>` `!=` `>=` `<=`  `<=>`安全等于
2. 逻辑运算符
    `&&` `and`
    `||` `or`
    `!`  `not`
3. 模糊查询
    `like`:一般搭配通配符使用，可以判断字符型或数值型
    通配符：`%`任意多个字符，`_`任意单个字符
4. `between and`
    `in`
    `is null` /`is not null`：用于判断`null`值

##### 1.2.3 `is null`   .VS.  `<=>`

 

|           | 普通类型的数值 | null值 | 可读性 |
| :-------: | :------------: | :----: | :----: |
| `is null` |       ×        |   √    |   √    |
|   `<=>`   |       √        |   √    |   ×    |

#### 1.3 排序查询

##### 1.3.1 语法

```sql
select 查询列表
from 表
where 筛选条件
order by 排序列表 【asc|desc】
```

##### 1.3.2 特点

1. `asc` ：升序，如果不写默认升序
2.  `desc`：降序
3. 排序列表 支持 单个字段、多个字段、函数、表达式、别名
4. `order by`的位置一般放在查询语句的最后（除`limit`语句之外）

#### 1.4 常见函数

##### 1.4.1 语法

```sql
select 函数名(实参列表);
```

##### 1.4.2 字符函数

```sql
concat:连接
substr:截取子串
upper:变大写
lower：变小写
replace：替换
length：获取字节长度
trim:去前后空格
lpad：左填充
rpad：右填充
instr:获取子串第一次出现的索引
```

##### 1.4.3 数学函数

```sql
ceil:向上取整
round：四舍五入
mod:取模
floor：向下取整
truncate:截断
rand:获取随机数，返回0-1之间的小数
```

##### 1.4.4 日期函数

```sql
now：返回当前日期+时间
year:返回年
month：返回月
day:返回日
date_format:将日期转换成字符
curdate:返回当前日期
str_to_date:将字符转换成日期
curtime：返回当前时间
hour:小时
minute:分钟
second：秒
datediff:返回两个日期相差的天数
monthname:以英文形式返回月
```

##### 1.4.5 其他函数

```sql
version 当前数据库服务器的版本
database 当前打开的数据库
user当前用户
password('字符')：返回该字符的密码形式
md5('字符'):返回该字符的md5加密形式
```

##### 1.4.6 流程控制函数

```sql
if(条件表达式，表达式1，表达式2)：

case情况1
case 变量或表达式或字段
when 常量1 then 值1
when 常量2 then 值2
...
else 值n
end

case情况2
case 
when 条件1 then 值1
when 条件2 then 值2
...
else 值n
end
```

##### 1.4.7 分组函数

```sql
select max(字段) from 表名
max 最大值
min 最小值
sum 和
avg 平均值
count 计算个数
```



#### 1.5 分组查询

##### 1.5.1 语法

```sql
select 分组函数，分组后的字段
from 表
【where 筛选条件】
group by 分组的字段
【having 分组后的筛选】
【order by 排序列表】
```

##### 1.5.2 `where` 和`having`

|            | 关键字   | 筛选的表     | 位置           |
| ---------- | -------- | ------------ | -------------- |
| 分组前筛选 | `where`  | 原始表       | `group by`前面 |
| 分组后筛选 | `having` | 分组后的结果 | `group by`后面 |



#### 1.6 连接查询

##### 1.6.1 内连接

```sql
select 查询列表
from 表1 别名
【inner】 join 表2 别名 on 连接条件
where 筛选条件
group by 分组列表
having 分组后的筛选
order by 排序列表
limit 子句;
```



##### 1.6.2 外连接

```sql
select 查询列表
from 表1 别名
left|right|full【outer】 join 表2 别名 on 连接条件
where 筛选条件
group by 分组列表
having 分组后的筛选
order by 排序列表
limit 子句;
```



##### 1.6.3交叉连接

```sql
select 查询列表
from 表1 别名
cross join 表2 别名;
```



#### 1.7 分页查询

##### 1.7.1 语法

```sql
select 查询列表
from 表
limit 【offset，】size;
```

#### 1.8 联合查询

##### 1.8.1 语法

```sql
查询语句1
union 【all】
查询语句2
union 【all】
...
```



### 2.`DML`语法

#### 2.1 插入

##### 2.1.1 语法

```sql
一、方式一
insert into 表名(字段名,...) values(值,...);

二、方式二
insert into 表名 set 字段=值,字段=值,...;
```



##### 2.1.2 对比

1. 方式一支持一次插入多行，语法如下：
    `insert into 表名【(字段名,..)】 values(值，..),(值，...),...;`
2. 方式一支持子查询，语法如下：
    `insert into 表名
    查询语句;`

#### 2.2 修改

##### 2.2.1 语法

```sql
update 表名 set 字段=值,字段=值 【where 筛选条件】;
```



#### 2.3 删除

##### 2.3.1 语法

```sql
方式一：使用delete
delete from 表名 【where 筛选条件】【limit 条目数】
方式二：使用truncate
truncate table 表名
```

##### 2.3.2 区别

1. `truncate`删除后，如果再插入，标识列从1开始
      `delete`删除后，如果再插入，标识列从断点开始
2. `delete`可以添加筛选条件
     `truncate`不可以添加筛选条件
3. `truncate`效率较高
4. `truncate`没有返回值
    `delete`可以返回受影响的行数
5. `truncate`不可以回滚
    `delete`可以回滚

### 3.`DDL`语言

#### 3.1 库的管理

##### 3.1.1 创建库

```sql
create database 【if not exists】 库名【 character set 字符集名】;
```

##### 3.1.2 修改库

```sql
alter database 库名 character set 字符集名;
```

##### 3.1.3 删除库

```sql
drop database 【if exists】 库名;
```

#### 3.2 表的管理

##### 3.2.1 创建表

```sql
create table 【if not exists】 表名(
	字段名 字段类型 【约束】,
	字段名 字段类型 【约束】,
	。。。
	字段名 字段类型 【约束】 
)
```

##### 3.2.2 修改表

```sql
1.添加列
alter table 表名 add column 列名 类型 【first|after 字段名】;
2.修改列的类型或约束
alter table 表名 modify column 列名 新类型 【新约束】;
3.修改列名
alter table 表名 change column 旧列名 新列名 类型;
4 .删除列
alter table 表名 drop column 列名;
5.修改表名
alter table 表名 rename 【to】 新表名;
```

##### 3.2.3 删除表

```sql
drop table【if exists】 表名;
```

##### 3.2.4 复制表

```sql
1、复制表的结构
create table 表名 like 旧表;
2、复制表的结构+数据
create table 表名 
select 查询列表 from 旧表【where 筛选】;
```

#### 3.3 数据类型

##### 3.3.1 数值型

1. 整型 `INT(8)`  不够位数用0填充
2. 浮点型
    1. 定点数：`FLOAT(M,D)`
    2. 浮点数:`DECIMAL(M,D)`

##### 3.3.2 字符型

`char`：固定长度的字符，写法为char(M)，最大长度不能超过M，其中M可以省略，默认为1
`varchar`：可变长度的字符，写法为varchar(M)，最大长度不能超过M，其中M不可以省略

##### 3.3.3 日期型

+ `year`年
+ `date`日期
+ `time`时间
+ `datetime` 日期+时间                
+ `timestamp` 日期+时间         

#### 3.4 常见约束

##### 3.4.1 常见约束

+ `NOT NULL`：非空，该字段的值必填
+ `UNIQUE`：唯一，该字段的值不可重复
+ `DEFAULT`：默认，该字段的值不用手动插入有默认值
+ `CHECK`：检查，mysql不支持
+ `PRIMARY KEY`：主键，该字段的值不可重复并且非空  `unique+not null`
+ FOREIGN KEY：外键，该字段的值引用了另外的表的字段

##### 3.4.2 创建表时添加约束

```sql
create table 表名(
	字段名 字段类型 not null,#非空
	字段名 字段类型 primary key,#主键
	字段名 字段类型 unique,#唯一
	字段名 字段类型 default 值,#默认
	constraint 约束名 foreign key(字段名) references 主表（被引用列）
)
```

##### 3.4.3 修改表时添加或删除约束

```sql
1、非空
添加非空
alter table 表名 modify column 字段名 字段类型 not null;
删除非空
alter table 表名 modify column 字段名 字段类型 ;

2、默认
添加默认
alter table 表名 modify column 字段名 字段类型 default 值;
删除默认
alter table 表名 modify column 字段名 字段类型 ;
3、主键
添加主键
alter table 表名 add【 constraint 约束名】 primary key(字段名);
删除主键
alter table 表名 drop primary key;

4、唯一
添加唯一
alter table 表名 add【 constraint 约束名】 unique(字段名);
删除唯一
alter table 表名 drop index 索引名;
5、外键
添加外键
alter table 表名 add【 constraint 约束名】 foreign key(字段名) references 主表（被引用列）;
删除外键
alter table 表名 drop foreign key 约束名;
```

##### 3.4.4 自增长列

```sql

一、创建表时设置自增长列
create table 表(
	字段名 字段类型 约束 auto_increment
)

二、修改表时设置自增长列
alter table 表 modify column 字段名 字段类型 约束 auto_increment

三、删除自增长列
alter table 表 modify column 字段名 字段类型 约束 
```



### 4.`TCL`语言

#### 4.1 事务

##### 4.1.1 定义

> 事务：一条或多条sql语句组成一个执行单位，一组sql语句要么都执行要么都不执行

##### 4.1.2 特点（`ACID`）

|  性质  |                           解释                           |
| :----: | :------------------------------------------------------: |
| 原子性 |    一个事务是不可再分割的整体，要么都执行要么都不执行    |
| 一致性 | 一个事务可以使数据从一个一致状态切换到另外一个一致的状态 |
| 隔离性 |      一个事务不受其他事务的干扰，多个事务互相隔离的      |
| 持久性 |         一个事务一旦提交了，则永久的持久化到本地         |

##### 4.1.3 事务的使用步骤

```sql
①开启事务
set autocommit=0;
start transaction;#可以省略

②编写一组逻辑sql语句
注意：sql语句支持的是insert、update、delete

设置回滚点：
savepoint 回滚点名;

③结束事务
提交：commit;
回滚：rollback;
回滚到指定的地方：rollback to 回滚点名;
```

##### 4.1.4 事务的隔离

并发问题

+ 脏读：一个事务读取了其他事务还没有提交的数据，读到的是其他事务“更新”的数据
+ 不可重复读：一个事务多次读取，结果不一样
+ 幻读：一个事务读取了其他事务还没有提交的数据，只是读到的是 其他事务“插入”的数据

隔离级别

| 隔离级别                   | 脏读 | 不可重复读 | 幻读 |
| -------------------------- | :--: | :--------: | :--: |
| `read uncommitted`读未提交 |  ×   |     ×      |  ×   |
| `read committed`读已提交   |  √   |     ×      |  ×   |
| `repeatable read`可重复读  |  √   |     √      |  ×   |
| `serializable` 串行化      |  √   |     √      |  √   |

设置隔离级别

```sql
set session|global transaction isolation level 隔离级别;
```



### 5.其他







