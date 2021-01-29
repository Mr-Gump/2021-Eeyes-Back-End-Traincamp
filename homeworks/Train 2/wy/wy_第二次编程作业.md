## 1.制作一个抢红包小程序，及输入人数和金额，打印每个红包的金额


```python
def rob_red_pocket (people,money) :
    import random
    l = []
    for i in range(people) :
        l.append(round (random.uniform(0.01,money - sum(l)) , 2))
        print (l[i])

people = 10  #int(input('多少人抢红包：'))
money = 20  #int(input('抢多少钱？'))
rob_red_pocket (people,money)
```

## 2.随便给一个文件夹路径统计里面文件种类和对应数量


```python
# ····
```

## 3.在给定的文件中匹配给定样式的所有字符串并打印


```python
import re
File = open("data.txt","r",encoding='utf-8')
s = a.read()
File.close()
p = re.compile(r"(.*)\[([^\[\]]*)\](.*)")
p.findall(string)
```


## 4.mysplite


```python
s = 'a,b,c'
print (s.split(',')) #人家的函数

def my_split(c):  #wy的函数
    A = []
    B = ""
    for Character in s :
        if Character == c :
            A.append(B)
            B = ""
        else :
            B += Character
    A.append(B)
    print(A)

my_split(',')
```
