# python基本数据类型的内置方法

## 一 数值

###### 整数`int`		浮点数`float`		复数`complex`

## 二 字符串

#### 定义：

> 在单引号\双引号\三引号内包含一串字符

```python
name1 = 'jason'  # 本质:name = str('任意形式内容')
name2 = "lili"  # 本质:name = str("任意形式内容")
name3 = """ricky"""  # 本质:name = str("""任意形式内容""")
```

#### 类型转换:

​		str()可以将任意数据类型转换成字符串类型，例如

```python
type(str([1,2,3])) # list->str
>>> type(str({"name":"jason","age":18})) # dict->str
<class 'str'>
>>> type(str((1,2,3)))  # tuple->str
<class 'str'>
>>> type(str({1,2,3,4})) # set->str
<class 'str'>
```

#### 操作

## 三 序列

##### 共有内置：

```python
len()	统计长度/个数
max()	min()	sum()
```

#### 字符串`string`

```python
split	分割字符串
title	将首字母大写
lower	所有字母小写
upper	所有字母大写
.replace(x,y)	用y替换x
```

#### 列表`list`

> 在[]内,用逗号分隔开多个任意数据类型的值

```python
del 	.pop()	.remove() 删除列表元素
.append	在末端增加元素
.insert 插入元素
.index	返回元素位置
.sort	升序排序
.count	返回元素出现次数
```

#### 字典`dictionary`

> 在{}内用逗号分隔开多元素，每一个元素都是key:value的形式，其中value可以是任意类型，而key则必须是不可变类型

​		```a={"a":1,"b":2}```

#### 元组`tuple`

> 元组与列表类似，也是可以存多个任意类型的元素，不同之处在于元组的元素不能修改，即元组相当于不可变的列表，用于记录多个固定不允许修改的值，单纯用于取

```python
info=dict(name='tony',age=18,sex='male')
info={'name':'tony','age':18,'sex':'male'}
```

#### 集合

>在{}内用逗号分隔开多个元素，集合具备以下三个特点：    
> 1：每个元素必须是不可变类型    
> 2：集合内没有重复的元素     
>3：集合内元素无序

```python
friends1 = {"zero","kevin","jason","egon"}
```



## 更多的使用方法可以进入以下网站学习

[python学习 day8 基本数据类型及内置方法](https://blog.csdn.net/qq_40555661/article/details/109260438)




