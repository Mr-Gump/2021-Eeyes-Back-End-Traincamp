# MARKDOWN 的使用

## 一 首先先在“偏好设置”进行设置，以便使用

严格模式关闭后似乎会更方便一点，但感觉好像不是很严谨？

## 二 代码块

```markdown
使用
​```
......(输入的内容)
​```
第一个``` 后的字符串为代码的语言（似乎可以不写？）
若为一行代码 可使用`...`
```

## 三 标题

```markdown
## 标题
```

+“空格”表示标题的书写，且最多六级标题，#的数量表示了标题的级数

## 四 删除线

```markdown
~~这句话是最标准的十二个字~~ 
```

在字符串的首尾分别加上 ~~（双波浪号，英文键盘）

e.g.

~~这句话是最标准的十二个字~~ 

## 五 斜体&加粗

```markdown 
*斜体*
**加粗**
***斜体+加粗***
```

*斜体*

**加粗**

***斜体+加粗***

## 六 下划线

```markdown
<u>就这</u> (快捷键 ctrl+u)
```

<u>就这？</u>

## 七 文字样式设置

### 高亮

```markdown
==闪闪==
```

​	==闪闪==

### 文字样式

``` markdown
<font face="黑体">我是黑体字</font> 
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=3 face="黑体">color=#0099ff size=3 face="黑体"</font> 
<font color=#00ffff size=4>color=#00ffff size=4</font>
<font color=gray size=5>color=gray size=5</font>
```

<font face="黑体">我是黑体字</font> 
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=3 face="黑体">color=#0099ff size=3 face="黑体"</font> 
<font color=#00ffff size=4>color=#00ffff size=4</font>
<font color=gray size=5>color=gray size=5</font>



## 八 下标

```markdown
H~2~O
```

H~2~O

## 九 上标

```markdown
面积 m^2^
```

m^2^

## 十 表情

```markdown
:smile:
```

:smile:

## 十一 表格

```markdown
name | price 
--- |--- 
liushanshan | 187
*也可以使用ctrl+t来插入*
```

| name        | price |
| ----------- | :---- |
| liushanshan | 187   |

==**注：通过冒号（：）在第二行的左/右/都有 来进行左/右对齐/居中**==

## 十二 引用

```markdown 
> 时间不在于你拥有多少，而在于你怎样去使用
>>力量本身并不可怕，可怕的是他的主人 
```



> 时间不在于你拥有多少，而在于你怎样去使用
>
> > 力量本身并不可怕，可怕的是他的主人

## 十三 列表

### 无序列表（==“*” “+” “-“==+空格）

```markdown
符号/数字. +空格
* 哈哈哈    
* 23333
```

* 哈哈哈    
* 23333

### 有序列表（==数字.==+空格）

```markdown
1. 你
2. 我
```

1. 你
2. 我

## 十四 分隔线

``` markdown
***
---
___
```

***

---

___

## 十五 跳转

### 外部跳转

``` markdown 
[B站](https://www.bilibili.com)
```

[B站](https://www.bilibili.com)

### 内部跳转（仅用于标题）

```markdown
[十二 引用](# (十二 引用) )
```

[十二 引用](# (十二 引用) )

### 自动链接

```markdown
<https://www.baidu.com>
```

<https://www.baidu.com>

## 十六 图片 ==直接粘贴就行==

```markdown
![image-20210121011823002](C:\Users\92512\AppData\Roaming\Typora\typora-user-images\image-20210121011823002.png)
```

![image-20210121011823002](C:\Users\92512\AppData\Roaming\Typora\typora-user-images\image-20210121011823002.png)

## 十七 主题

在“主题”部分改就可以了，会影响页面布局及观看细节

## 十八 复选框

``` markdown
- [x] 交付
- [] 交付
```

- [x] 交付

- [ ] 交付

