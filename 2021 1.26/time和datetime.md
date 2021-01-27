# `time`和`datetime`

[TOC]

## 1.`time`模块

#### 		1. `time.time()`   获取当前时间戳

```python
In [2]: time.time()
Out[2]: 1610627217.1869385
```

#### 		2.`time.localtime()`  以结构化时间的格式返回当前时间

```python
In [3]: time.localtime()
Out[3]: time.struct_time(tm_year=2021, tm_mon=1, tm_mday=14, tm_hour=20, tm_min=27, tm_sec=24, tm_wday=3, tm_yday=14, tm_isdst=0)
```

#### 		3.` time.strftime("%Y %m %d %X",time.localtime())`  把结构化时间,按照自定格式输出

```python
In [4]: time.strftime("%Y %m %d %X",time.localtime())
Out[4]: '2021 01 14 20:28:56'
```

#### 		4.`time.strptime('2021 01 14 20:28:56',"%Y %m %d %X")`  把字符串时间转化为结构化时间

```python
In [5]: time.strptime('2021 01 14 20:28:56',"%Y %m %d %X")
Out[5]: time.struct_time(tm_year=2021, tm_mon=1, tm_mday=14, tm_hour=20, tm_min=28, tm_sec=56, tm_wday=3, tm_yday=14, tm_isdst=-1)
```

## 2.`datetime`模块

```python
from datetime import *
```

#### 		1.`datetime.today()`   获取今天的时间

```python
In [7]: datetime.today()
Out[7]: datetime.datetime(2021, 1, 14, 20, 34, 29, 749425)
```

#### 		2.`datetime.now()`  获取现在时间

```python
In [8]: datetime.now()
Out[8]: datetime.datetime(2021, 1, 14, 20, 34, 38, 275236)
```

#### 		3.`timedelta(days = 1)`   表示时间间隔

```python
In [9]: datetime.today() - timedelta(days = 1)
Out[9]: datetime.datetime(2021, 1, 13, 20, 35, 29, 824186)
```



