# `random`,`json`,`pathlib`,`os.path`

[TOC]

## 1.`random`

```python
from random import *
```

#### 		1.`random()`  生成一个0~1的浮点数

```python
In [2]: random()
Out[2]: 0.6676005721202086
```

#### 		2,`randrange()`  有范围生成随机整数

```python
In [3]: randrange(0,101,2)
Out[3]: 64
```

#### 		3.`choice()`  从列表中随机选择元素

```python
In [4]: choice([1,2,3,4,5])
Out[4]: 4
```

#### 		4.`sample()`  从列表中随机选出几个元素

```python
In [5]: sample([1,2,3,4,5],k=3)
Out[5]: [5, 3, 1]
```

## 2.`json`

#### 		1.`loads()`   读取json格式数据

```python
In [7]: json.loads('["foo",{"bar":["baz",null,1.0,2]}]')
Out[7]: ['foo', {'bar': ['baz', None, 1.0, 2]}]
```

#### 		2.`dumps()`  将json格式数据转成字符串

```python
In [8]: json.dumps("['foo', {'bar': ['baz', None, 1.0, 2]}]")
Out[8]: '"[\'foo\', {\'bar\': [\'baz\', None, 1.0, 2]}]"'
```

## 3.`pathlib`

```python
from pathlib import Path
```

#### 		1.`resolve()`   获取当前绝对路径

```python
In [2]: p = Path()
In [3]: p.resolve()
Out[3]: WindowsPath('C:/Users/24246/Desktop')
```

#### 		2.对其他路径处理

```python
In [8]: p = Path(r'C:\Users\24246\Desktop\test.txt.log')

In [9]: p.name
Out[9]: 'test.txt.log'

In [10]: p.stem
Out[10]: 'test.txt'

In [11]: p.suffix
Out[11]: '.log'

In [12]: p.suffixes
Out[12]: ['.txt', '.log']

In [13]: p.parent
Out[13]: WindowsPath('C:/Users/24246/Desktop')

In [14]: p.parents
Out[14]: <WindowsPath.parents>

In [15]: for i in p.parents:
    ...:     print(i)
    ...:
C:\Users\24246\Desktop
C:\Users\24246
C:\Users
C:\

In [16]: p.parts
Out[16]: ('C:\\', 'Users', '24246', 'Desktop', 'test.txt.log')
```

#### 4.`os.path`

```python
In [1]: from os.path import *

In [2]: abspath(r'C:\Users\24246\Desktop\a.txt')
Out[2]: 'C:\\Users\\24246\\Desktop\\a.txt'

In [3]: basename(r'C:\Users\24246\Desktop\a.txt')
Out[3]: 'a.txt'

In [4]: dirname(r'C:\Users\24246\Desktop\a.txt')
Out[4]: 'C:\\Users\\24246\\Desktop'

In [5]: exists(r'C:\Users\24246\Desktop\a.txt')
Out[5]: False
    
In [7]: isfile(r'C:\Users\24246\Desktop\a.txt')
Out[7]: False

In [8]: isdir(r'C:\Users\24246\Desktop\a.txt')
Out[8]: False

In [9]: join(r'C:\Users\24246\Desktop\a.txt','..')
Out[9]: 'C:\\Users\\24246\\Desktop\\a.txt\\..'
```

