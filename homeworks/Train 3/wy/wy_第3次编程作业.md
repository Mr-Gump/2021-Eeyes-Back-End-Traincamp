# Train3

## 1.打印杨辉三角


```python
line1 = [1]
line2 = [1 , 1]
line0 = line2

n = int(input('想打印几行杨辉三角呢？'))
print (line1)
print (line2)

for i in range(2,n):
    linei = []
    linei.append(1)
    for j in range (len(line0)-1):
        linei.append(line0[j] + line0[j+1])
    linei.append(1)
    print (linei)
    line0 = linei
```

## 2.井字棋

### --人机对战


```python
# 给出棋盘
game = [
[1,1,1],
[1,1,1],
[1,1,1]]

n = 0
# player1下0，computer下2。当直线的和等于0/6时，游戏结束
while (sum(game[0]) != 0 and sum(game[0]) != 6 
    and sum(game[1]) != 0 and sum(game[1]) != 6 
    and sum(game[2]) != 0 and sum(game[2]) != 6 

    and game[0][0]+game[1][1]+game[2][2] != 0
    and game[0][2]+game[1][1]+game[2][0] != 0
    and game[0][0]+game[1][1]+game[2][2] != 6
    and game[0][2]+game[1][1]+game[2][0] != 6      
    
    and game[0][0]+game[1][0]+game[2][0] != 0
    and game[0][1]+game[1][1]+game[2][1] != 0
    and game[0][2]+game[1][2]+game[2][2] != 0
    and game[0][0]+game[1][0]+game[2][0] != 6
    and game[0][1]+game[1][1]+game[2][1] != 6
    and game[0][2]+game[1][2]+game[2][2] != 6):

    n += 1
# 打印棋盘
    for i in game :
        print(i)
        
	print ("请用两位数坐标表示下棋的位置(如22，33，13)")
    
# Player1下棋
    Position1 = int(input("Player1下哪个位置？"))
    game[Position1//10 -1][Position1%10 -1] = 0

    if n == 5 :
        print ("平局，再来一盘吧")
        break  # 防止棋盘下满后死循环

# computer下棋
    import random
    x , y = random.randint(1,3)-1 , random.randint(1,3)-1
    while game[x][y] != 1:
        x , y = random.randint(1,3)-1 , random.randint(1,3)-1
    game[x][y] = 2

# 判定胜负
else:
    for i in game :
        print(i)
    if (sum(game[0]) == 0
    or sum(game[1]) == 0
    or sum(game[2]) == 0

    or game[0][0]+game[1][1]+game[2][2] == 0
    or game[0][2]+game[1][1]+game[2][0] == 0
    
    or game[0][0]+game[1][0]+game[2][0] == 0
    or game[0][1]+game[1][1]+game[2][1] == 0
    or game[0][2]+game[1][2]+game[2][2] == 0):
        print('Player 1 win!')
    else:
        print('电脑赢了 你个傻*')
```

### --双人游戏


```python
# 给出棋盘
game = [
[1,1,1],
[1,1,1],
[1,1,1]]

n = 0
# player1下0，playe2下2。当直线的和等于0/6时，游戏结束
while (sum(game[0]) != 0 and sum(game[0]) != 6 
    and sum(game[1]) != 0 and sum(game[1]) != 6 
    and sum(game[2]) != 0 and sum(game[2]) != 6 

    and game[0][0]+game[1][1]+game[2][2] != 0
    and game[0][2]+game[1][1]+game[2][0] != 0
    and game[0][0]+game[1][1]+game[2][2] != 6
    and game[0][2]+game[1][1]+game[2][0] != 6      
    
    and game[0][0]+game[1][0]+game[2][0] != 0
    and game[0][1]+game[1][1]+game[2][1] != 0
    and game[0][2]+game[1][2]+game[2][2] != 0
    and game[0][0]+game[1][0]+game[2][0] != 6
    and game[0][1]+game[1][1]+game[2][1] != 6
    and game[0][2]+game[1][2]+game[2][2] != 6):

    n += 1
# 打印棋盘
    for i in game :
        print(i)

	print ("请用两位数坐标表示下棋的位置(如22，33，13)")
    
# Player1下棋
    Position1 = int(input("Player1下哪个位置？"))
    game[Position1//10 -1][Position1%10 -1] = 0

    if n == 5 :
        print ("平局，再来一盘吧")
        break  # 防止棋盘下满后死循环
        

    for i in game :
        print(i)
# Player2下棋
    Position1 = int(input("Player2下哪个位置？"))
    game[Position1//10 -1][Position1%10 -1] = 2
    
# 判定胜负
else:
    for i in game :
        print(i)
    if (sum(game[0]) == 0
    or sum(game[1]) == 0
    or sum(game[2]) == 0

    or game[0][0]+game[1][1]+game[2][2] == 0
    or game[0][2]+game[1][1]+game[2][0] == 0
    
    or game[0][0]+game[1][0]+game[2][0] == 0
    or game[0][1]+game[1][1]+game[2][1] == 0
    or game[0][2]+game[1][2]+game[2][2] == 0):
        print('Player 1 win!')
    else:
        print('Player 2 win!')
```

# Train2

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
import os
from pathlib import Path

Type=dict()
#输入要浏览的文件夹路径
File = input("文件目录")
#读取文件的后缀名
for root, dirs, files in os.walk(File):
    for i in files:
        f =Path(i).suffix  
        if f in Type: 
            Type[f]=Type[f]+1 
        else:
            Type[f]=1
            
name=Type.keys()
for i in name:
    print(i,':',Type[i])
```

## 3.在给定的文件中匹配给定样式的所有字符串并打印


```python
import re
File = open("data.txt","r",encoding='utf-8')
s = File.read()
File.close()
p = re.compile(r"[\d]")
p.findall(s)
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

