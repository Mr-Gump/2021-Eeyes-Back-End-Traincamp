# Python变量
1. 可以理解为一个装数据的箱子，可以修改。

2. 变量可以用`=`赋值。不要与保留字，内置函数重名，遵守规范。
   3. 也可以将表达式结果赋值给变量

   ```python
   n=10
   print(n)
   10
   #也可以用于字符串拼接
   url="http://ugg.com"
   str = "c++教程：" + url 
   ```

3. 作为弱类型语言（`py，js，php`），无须声明变量直接赋值，可以随时改变。不声明类型，不代表没有，用`type(变量)`可以查看类型

   1. `type(3*15.6)`同样可以

# 数据类型

# ![](C:\Users\HSH\Desktop\md\第一次作业\IMG_0595(20210125-105240).JPG)

1. 整数和浮点数

   1. 在计算机内部存储的方式是不同的，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差。

2. 字符串

   1. 是以单引号'或双引号"括起来的任意文本，比如`'abc'，"xyz"`等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串`'abc'`只有`a，b，c`这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如`"I'm OK"`包含的字符是`I，'，m，空格，O，K`这6个字符。

   2. 如果字符串内部既包含`'又包含"`怎么办？可以用转义字符\来标识，比如：`'I\'m \"OK\"!' `表示的字符串内容是：`I'm "OK"!`

      转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`，可以在`Python`的交互式命令行用`print()`打印字符串看看。如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，`Python`还允许用`r''`表示''内部的字符串默认不转义。

      ```python
      #普通含有转义的字符串
      text="1 E:/Code/PycharmProjects/QtDemo/ToolsList\__pycache__\start.cpython-36.pyc \r\n"
      print(text)
       
      #输出如下：
      #E:/Code/PycharmProjects/QtDemo/ToolsList__pycache__\start.cpython-36.pyc 
      #<空行>
       
      #在python中使用r来处理常量，强制不转义。
      text=r"1 E:/Code/PycharmProjects/QtDemo/ToolsList\__pycache__\start.cpython-36.pyc \r\n"
      print(text)
       
      #输出如下：
      #E:/Code/PycharmProjects/QtDemo/ToolsList__pycache__\start.cpython-36.pyc \r\n
      ```

3. 布尔值

   1. `Ture`或`False`，务必大写
   2. 其运算用`and,or,not`

4. 空值

   1. `None`不能理解为0，None不能理解为0，因为0是有意义的，而`None`是一个特殊的空值。
   
5. 数据类型转换

   | 函数                   | 说明                                                |
   | ---------------------- | --------------------------------------------------- |
   | int(x [,base ])        | 将x转换为一个整数                                   |
   | long(x [,base ])       | 将x转换为一个长整数                                 |
   | float(x )              | 将x转换到一个浮点数                                 |
   | complex(real [,imag ]) | 创建一个复数                                        |
   | str(x )                | 将对象 x 转换为字符串                               |
   | repr(x )               | 将对象 x 转换为表达式字符串                         |
   | eval(str )             | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
   | tuple(s )              | 将序列 s 转换为一个元组                             |
   | list(s )               | 将序列 s 转换为一个列表                             |
   | chr(x )                | 将一个整数转换为一个字符                            |
   | unichr(x )             | 将一个整数转换为Unicode字符                         |
   | ord(x )                | 将一个字符转换为它的整数值                          |
   | hex(x )                | 将一个整数转换为一个十六进制字符串                  |
   | oct(x )                | 将一个整数转换为一个八进制字符串                    |

6. 列表

   
   1. 可以存放不同变量
   2. 有序
   3. 从0开始计数

```python
a = [1,"hello",True]
a[0]=1
a[1]='hello'
a.append(223)#往列表里加入223
```

7. 元组，只能访问，不能改变

```python
a = (1,5,"andriod")
```

8. 字典
   1. ```a={"a":1,"b":2}```
   2. "keyi":valuei