```python
1.背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加
```


```python
class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.animals=[]
    def add(self,animal):
        if animal in self.animals:
            print(f'无法重复添加')
        else:
            self.animals.append(animal)
            animal_kind=animal.__class__.__name__
            setattr(self,animal_kind,animal)
class Animal(object):
    kind_dict={'小':0,'中等':1,'大':2}
    def __new__(cls, *args):
        if cls.__name__=='Animal':
            print('不可实例化')
        else:
            return  super().__new__(cls)
    def __init__(self,kind,shape,chara):
        self.kind=kind
        self.shape=Animal.kind_dict[shape]
        self.chara=chara
    @property
    def is_fierce0(self):
        if self.shape>=1 and self.kind=='食肉'and self.chara=='凶猛':
            return True
        else:
            return False
class Cat(Animal):
    sound='miao'
    def __init__(self,name,kind,shape,chara):
        super().__init__(kind,shape,chara)
        self.name=name
    @property
    def pet(self):
        if self.is_fierce==True
            return False
        else:
            return True
class Dog(Animal):
    sound='wang'
    def __init__(self,name,kind,shape,chara):
        super().__init__(kind,shape,chara)
        self.name=name
    @property
    def pet(self):
        if self.is_fierce==True
            return False
        else:
            return True


```


```python
2.用面向对象的方法实现井字棋
```


```python
import sys
class Player(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def gen_point(self):
        loc = input(f'player {self.name} , please enter a point like 1,2 :')
        return Point.pre_gen(loc, self.mark)
class Point(object):
    chess_type = {0: '-', 1: 'X', 2: "O"}
    def __init__(self, x, y, mark):
        self.x = x
        self.y = y
        self.mark = mark
    @classmethod
    def pre_gen(cls, pre_str, mark):
        x = int(pre_str.split(',')[0]) - 1
        y = int(pre_str.split(',')[1]) - 1
        return cls(x, y, mark)
class Chess(object):
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([0, 0, 0])
    def print_chess(self):
        for line in self.board:
            for i in line:
                print(Point.chess_type[i], end=' ')
            print()
    def insert_to_chess(self, point):
        if point.x > 2 or point.y > 2:
            print('落子位置超出棋盘,落子无效!')
            sys.exit()
        if self.board[point.x][point.y] != 0:
            print('落子位置有其他落子,落子无效')
            sys.exit()
        self.board[point.x][point.y] = point.mark
        self.print_chess()
        if self.judge() == 1:
            print('player1获胜')
            sys.exit()
        elif self.judge() == 2:
            print('player2 获胜')
            sys.exit()
    def judge(self):
        flag = 0
        for line in self.board:
            if line[0] == line[1] and line[2] == line[1]:
                if line[0] == 1:
                    flag = 1
                elif line[0] == 1:
                    flag = 2
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i]:
                if self.board[0][i] == 1:
                    flag = 1
                elif self.board[0][i] == 2:
                    flag=2
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1]:
            if self.board[0][0] == 1:
                flag = 1
            elif self.board[0][0] == 2:
                flag = 2
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            if self.board[1][1] == 1:
                flag = 1
            elif self.board[1][1] == 2:
                flag = 2
        return flag
if __name__ == '__main__':
    player1 = Player('ty', 1)
    player2 = Player('gwh', 2)
    chess = Chess()
    print('-----比赛开始-------')
    while True:
        current_point = player1.gen_point()
        chess.insert_to_chess(current_point)
        current_point = player2.gen_point()
        chess.insert_to_chess(current_point)
        
```


```python
3.用自己的话分析一下动物园题目,并说明你认为的难点及其解决方法
```


```python
1.难以理解的问题
 animal_kind=animal.__class__.__name__
            setattr(self,animal_kind,animal)
我理解的class前后的下划线是魔术方法，但是我不是很能理解这句代码啊
2.难点
  @property
    def pet(self):
        if self.is_fierce==True
            return False
因为我不知道 if self.is_fierce==True中的等号右边可以直接写True,以及很多基础语法的使用，导致有一些想法但是难以用代码实现
```


```python
4.面向对象的方法实现时钟
```


```python
#定义钟表及其属性
class Clock(object):
    def __init__(self,second,minute,hour):
        self.second=second
        self.minute=minute
        self.hour=hour
#运行函数
    def run(self):
        self.second += 1
        if self.second==60:
            self.second=0
            self.minute += 1
            if self.minute==60:
                self.minute=0
                self.hour += 1
                if self.hour==24:
                    self.hour=0
#打印函数
    def print(self):
        return f"({self.hour}:{self.minute}:{self.second})"
```


```python
5.面向对象的方法实现坐标点
```


```python
#设置点
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

#点位置改变的方法
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy


#点的距离
    def distence(self,numberx,numbery):
        return ((self.x-numberx)**2+(self.y-numbery)**2)**0.5

#打印
    def __str__(self):
        return f"({self.x},{self.y})"

#测试
    point = Point(1,2)
    print(point)
    point.move(2,1)
    print(point)
    print(point.distence(4,3))


```


```python
6.思考并尝试用面向对象的思想描述生活中的某个问题,复杂度不限,如:排队问题,游戏对战等
```


```python
#幸运锦鲤活动

import random

#选号
class all_number(object):
    def __init__(self,number):
        self.name=number
        
#抽出二位幸运锦鲤

    def lucky_number(self,number):
        self.luck_number=[]
        luck_number1=random.randint(number)
        luck_number2=random.randint(number)
        while True:
            if luck_number1==luck_number2:
                luck_number2=random.randint(number)
        self.luck_number.append(luck_number1,luck_number2)

        
#打印锦鲤

    def result(self,luck_number):
        return f"{self.luck_number}"
    
```


```python

```
