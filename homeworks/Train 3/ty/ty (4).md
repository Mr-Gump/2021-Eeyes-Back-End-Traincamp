```python
1.制作一个模拟微信抢红包小程序,即输入人数和金额,打印每个红包的金额,要求运行100000次后,每个人平均抢红包金额相同(即实现公平)
```


```python
from random import *

people=int(input('the number of people'))
money 1=int(input('the number of money'))
    money = money 1* 100
    result = []
    rest = money
#随机取数
    for i in range(people - 1):
        current = randint(1, (rest / (people - i + 1) )* 2)
#将随机数加给result
        result.append(current * 0.01, 2)
        rest = rest - current
#将最后一个人的值加给result
        result.append(rest)
print(result)




#File "C:/Users/田野/PycharmProjects/pythonProject/try one.py", line 4
    money 1=int(input('the number of money'))
          ^
SyntaxError: invalid syntax
    
但是我没有弄明白为什么是无效的索引啊
```


```python
2.随便输入一个文件夹路径,统计里面文件种类和对应数量,并输出 tips:os.walk
```


```python
import os
from pathlib import Path
dir_name=input('文件夹目录')
types={}
#浏览文件夹
for root,dirs,files in os.walk(dir_name):
    for filename in files:
#识别后缀   
     suffix=Path(filename).suffix 
       if suffix=='':
            continue
#增加文件类型的数量
        if suffix in types:
            types[suffix]+=1
#添加新的文件类型
        else:
            types.append(suffix)
            types[suffix]=1
    print(types)

    
#我操作了几次都没有报错，但在文件夹中包含含有后缀的文件时都出现了如下情况啊
文件夹目录homework

Process finished with exit code 0

```


```python
3.在给定的文件 data.txt 中匹配给定样式的所有字符串并打印
字符串样式为在含有answer=true的每一行中
例如:
s21.analyse=null;s21.answer=true;s21.content="<p><img src=\"http://edu-image.nosdn.127.net/025741D866237C8AE2872BDE6DBAE944.jpg?imageView&thumbnail=890x0&quality=100\"  /></p>";s21.id=243994065627587;s21.selectCount=null;
提取content的内容
在这个例子中,即提取
<p><img src=\"http://edu-image.nosdn.127.net/025741D866237C8AE2872BDE6DBAE944.jpg?imageView&thumbnail=890x0&quality=100\"  /></p>
注:data.txt不许复制或移动位置
```


```python
['<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u591C\\u89C6\\u6280\\u672F</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u8FDC\\u8DDD\\u79BB\\u5149\\u5B66\\u63A2\\u6D4B\\u6280\\u672F</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6FC0\\u5149\\u63A2\\u6D4B</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u591A\\u5149\\u8C31\\u63A2\\u6D4B</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u8B66\\u6212\\u96F7\\u8FBE</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u8D85\\u89C6\\u8DDD\\u96F7\\u8FBE</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA7\\u89C6\\u96F7\\u8FBE</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u76F8\\u63A7\\u9635\\u96F7\\u8FBE</span></span></p>',
 '<p><span style=\\"color: black; font-family: \\u5B8B\\u4F53; font-size: 12px;\\"  >\\u5FAE\\u6CE2-&gt;\\u7EA2\\u5916\\u6CE2-&gt;\\u53EF\\u89C1\\u5149-&gt;\\u65E0\\u7EBF\\u7535\\u6CE2</span></p>',
 '<p><span style=\\"color: black; font-family: \\u5B8B\\u4F53; font-size: 12px;\\"  >\\u53EF\\u89C1\\u5149-&gt;\\u7EA2\\u5916\\u6CE2-&gt;\\u5FAE\\u6CE2-&gt;\\u65E0\\u7EBF\\u7535\\u6CE2</span><span id=\\"_baidu_bookmark_start_512\\"  style=\\"line-height: 0px; display: none;\\"  >\\u200D</span></p>',
 '<p><span style=\\"color: black; font-family: \\u5B8B\\u4F53; font-size: 12px;\\"  >\\u7EA2\\u5916\\u6CE2-&gt;\\u53EF\\u89C1\\u5149-&gt;\\u5FAE\\u6CE2-&gt;\\u65E0\\u7EBF\\u7535\\u6CE2</span></p>',
 '<p><span style=\\"color: black; font-family: \\u5B8B\\u4F53; font-size: 12px;\\"  >\\u53EF\\u89C1\\u5149-&gt;\\u7EA2\\u5916\\u6CE2-&gt;\\u65E0\\u7EBF\\u7535\\u6CE2-&gt;\\u5FAE\\u6CE2</span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4EFB\\u4F55\\u7269\\u4F53\\u5BF9\\u7535\\u78C1\\u6CE2\\u90FD\\u6709\\u4E00\\u5B9A\\u7684\\u53CD\\u5C04\\u4F5C\\u7528\\uFF0C\\u53CD\\u5C04\\u7A0B\\u5EA6\\u53D7\\u7269\\u4F53\\u7279\\u6027\\u548C\\u7535\\u78C1\\u6CE2\\u6CE2\\u957F\\u5F71\\u54CD\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E0D\\u540C\\u7269\\u4F53\\u5BF9\\u76F8\\u540C\\u6CE2\\u957F\\u7535\\u78C1\\u6CE2\\u7684\\u53CD\\u5C04\\u80FD\\u529B\\u76F8\\u540C\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E0D\\u540C\\u7269\\u4F53\\u5BF9\\u540C\\u4E00\\u6CE2\\u957F\\u7684\\u7535\\u78C1\\u6CE2\\u53CD\\u5C04\\u80FD\\u529B\\u4E0D\\u76F8\\u540C\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u540C\\u4E00\\u7269\\u4F53\\u5BF9\\u4E0D\\u540C\\u6CE2\\u957F\\u7684\\u7535\\u78C1\\u6CE2\\u53CD\\u5C04\\u80FD\\u529B\\u4E0D\\u76F8\\u540C\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6C14\\u8C61\\u6761\\u4EF6</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u76EE\\u6807\\u7684\\u7279\\u5F81\\u4FE1\\u606F</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u76D1\\u89C6\\u7684\\u89D2\\u5EA6</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u5730\\u5F62\\u5730\\u7269</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u653B\\u51FB\\u4E00\\u4F53\\u5316</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u901F\\u5EA6\\u4E0A\\u5B9E\\u65F6\\u5316</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u76EE\\u7684\\u975E\\u519B\\u4E8B\\u5316</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u624B\\u6BB5\\u4E0A\\u7684\\u7EFC\\u5408\\u5316</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u88AB\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u4F18\\u70B9\\u5BB9\\u6613\\u9690\\u853D\\u81EA\\u8EAB\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u88AB\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u4F18\\u70B9\\u63A2\\u6D4B\\u6548\\u679C\\u975E\\u5E38\\u597D\\uFF0C\\u7F3A\\u70B9\\u5BB9\\u6613\\u66B4\\u9732\\u81EA\\u5DF1\\u3002</span></span></p>',
 '<p><span id=\\"_baidu_bookmark_start_640\\"  style=\\"line-height: 0px; display: none;\\"  >\\u200D</span><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E3B\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u7F3A\\u70B9\\u5BB9\\u6613\\u66B4\\u9732\\u81EA\\u5DF1\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E3B\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u4F18\\u70B9\\u5BB9\\u6613\\u9690\\u853D\\u81EA\\u8EAB\\uFF0C\\u7F3A\\u70B9\\u4FA6\\u5BDF\\u6548\\u679C\\u5DEE\\u3002</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u672F\\u4FA6\\u5BDF</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u7565\\u4FA6\\u5BDF</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u6597\\u4FA6\\u5BDF</span></span></p>',
 '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u5F79\\u4FA6\\u5BDF</span></span></p>']
```


```python
import os
from pathlib import Path
dir_name=input('文件夹目录')
types={}
#浏览文件夹
for root,dirs,files in os.walk(dir_name):
    for filename in files:
#识别后缀   
     suffix=Path(filename).suffix 
       if suffix=='':
            continue
#增加文件类型的数量
        if suffix in types:
            types[suffix]+=1
#添加新的文件类型
        else:
            types.append(suffix)
            types[suffix]=1
    print(types)

```


```python
4.手动实现mysplit函数,要求具有和split完全一样的功能
```


```python
#明确字符串与对应字符
def my_split(string,pattern):
    result=[]
    start_loc=0
    end_loc=0
#判断字符    
for i in string:
        end_loc+=1
        if i==pattern:
#将字符串切割，放入result            
result.append(string[start_loc:end_loc-1])
            start_loc=end_loc
    result.append(string[start_loc:end_loc])
    return  result


```


```python
5.数列
```


```python
n=input('the line')
line1=[1]
line2=[1,1]
line0=line2
for i in range(2,n):
    linei=[]
#添加第一个值
    linei.append(1)
#循环多组相加得到中间值
    for j in range(len(line0)-1):
        linei.append(line0[j]+line0[j+1])

#添加最后一个值
    linei.append(1)
    line0=linei
print(linei)

```


```python
6.井字棋
```


```python
import sys
# 落子
def insert_chess(chess,target,player):
    chess[int(target[0])-1][int(target[1])-1]=player
# 打印棋盘
def print_chess(chess):
    for line in chess:
        for i in line:
            print(chess_type[i],end='')
        print()
# 判断胜负
def judge_chess(chess):
    flag=0
    for line in chess:
        if line[0]==line[1] and line[2]==line[1]:
            if line[0]==1:
                flg=1
            elif line[0]==2:
                flg=2


    for i in range(3):
        if chess[0][i]==chess[1][i] and chess[2][i]==chess[1][i]:
            if chess[1][i]==1:
                flag=1
            elif chess[1][i]==2:
                flag=2


    if chess[0][0]==chess[1][1] and chess[2][2]==chess[1][1]:
        if chess[0][0]==1:
            flag=1
        elif chess[0][0]==2:
            flag=2
    elif chess[2][0]==chess[1][1] and chess[2][0]==chess[0][2]:
        if chess[1][1]==1:
            flag=1
        elif chess[1][1]==2:
            flag=2


    if flag==0:
        print('暂无人获胜')
    elif flag==1:
        print('player1获胜')
        sys.exit()
    else:
        print('player2获胜')
        sys.exit()





# 录入玩家信息
player1=input('a')
player2=input('b')
chess_type={0:'',1:'a',2:'b'}
chess=[]
for i in range(3):
    chess.append([0,0,0])

# 交替落子
while True:
    player1_target=input('player1落子位置').split('.')
    #打印棋盘，判断胜负
    insert_chess(chess,player1_target,1)
    print_chess(chess)
    player2_target=input('player2落子位置').split('.')
    #打印棋盘，判断胜负
    insert_chess(chess, player2_target, 2)
    print_chess(chess)



```
