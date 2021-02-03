# Python数据类型与内置方法

1. ### 数值

   + **整数**（*int*）
   + **浮点数**（*float*）
   + **复数**（*comlpex*）

   P.S.   Python作为一种**`弱类型语言`**，一般情况下不需要区分**整数**和**浮点数**

2. ### 字符串（str）

   ```python
   a='dsf'
   
   b="dsf"
   
   c='''dsf'''
   
   d="""dsf"""   #c、d为加强版，可以在三引号内换行而不用加“\n”
   
   e=str('dsf')
   ```

3. ### 列表（list）

   ```python
   a=['dsf','hlb','dsf']
   
   b=['dsf',1997,'ass']
   ```

   ```python
   a='assAssinDsfdxpDggHybhlbAssassIn'
   
   len(a)                   #字符串长度
   b=a.split('d')           #以括号内东西为分割符分割字符串
   b=a.title	             #将首字母大写
   b=a.lower	             #所有字母小写
   b=a.upper	             #所有字母大写
   
   c='ass'
   d=c.replace('s','d')
   ```

   

   ```python
   a=['dsf','hlb','dsf']
   
   del a[0]                  #删除
   len(a)                    #包含元素个数
   a.remove('dsf')           #删除第一个'dsf'
   a.append('ass')           #末尾添加'ass'
   a.cuont('dsf')            #元素'dsf'的个数
   a.index('dsf')            #元素'dsf'第一次出现的位置
   
   
   b=[996,19761006,1989,1992,604,233]
   
   b.sort()                  #对b元素升序排列
   ```

   

4. ### 元组（tuple）（无法改变的列表）

   ```python
   a=('dsf','hlb')
   
   b=('dsf',1989)
   ```

5. ### 字典（dict）

   ```python
   a={'dsf':'dxp','hlb':'hyb'}
   
   b=dict(dsf='dxp',hlb='hyb',fubao=996)
   
   list=[('996','19761006——'),('18+','1992')]
   c=dict(list)
   
   
   
   zidian={}
   zidian('test')=4?????
   ```

6. ### 集合（set）（无序且不重复）

   ```python
   a={'dsf','dxp'}
   
   b=set('dsf','dxp')
   ```

### 不用查重了，我是从[菜鸟教程](https://www.runoob.com/python3/python3-string.html)查的。。。。。