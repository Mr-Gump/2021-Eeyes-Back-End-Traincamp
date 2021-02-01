## 制作一个抢红包小程序,即输入人数和金额,打印每个红包的金额


```python
from random import *

def redbag(ren, qian):
    renlist = []
    rand = []
    qianlist = []
    a = 1
    for i in range(ren):
        renlist.append(a)
        a = a + 1
        rand.append(random())
    for i in range(ren):
        qianlist.append(round(qian * rand[i] / sum(rand), 2))
    return renlist, qianlist

r = float(input('人数：'))
if r != int(r) or r <= 0:
    print(f'不存在{r}个人')
    exit()
else:
    r = int(r)
q = float(input('钱数：'))
if q*100 < r:
    print(f'{r}个朋友分{int(q*100)}分，给点面子行不行?')
    exit()

renlist, qianlist = redbag(r, q)

for i in range(r):
    print(f'第{renlist[i]}个红包的金额为：{qianlist[i]}')
```

    人数：59
    钱数：87
    第1个红包的金额为：2.24
    第2个红包的金额为：1.68
    第3个红包的金额为：2.35
    第4个红包的金额为：2.15
    第5个红包的金额为：0.09
    第6个红包的金额为：1.89
    第7个红包的金额为：0.43
    第8个红包的金额为：2.71
    第9个红包的金额为：1.95
    第10个红包的金额为：2.14
    第11个红包的金额为：1.54
    第12个红包的金额为：0.14
    第13个红包的金额为：0.97
    第14个红包的金额为：1.29
    第15个红包的金额为：0.79
    第16个红包的金额为：2.08
    第17个红包的金额为：2.12
    第18个红包的金额为：1.38
    第19个红包的金额为：1.4
    第20个红包的金额为：1.26
    第21个红包的金额为：1.31
    第22个红包的金额为：1.32
    第23个红包的金额为：1.9
    第24个红包的金额为：0.45
    第25个红包的金额为：0.14
    第26个红包的金额为：2.48
    第27个红包的金额为：0.99
    第28个红包的金额为：0.5
    第29个红包的金额为：0.37
    第30个红包的金额为：1.45
    第31个红包的金额为：1.63
    第32个红包的金额为：1.04
    第33个红包的金额为：0.89
    第34个红包的金额为：1.82
    第35个红包的金额为：2.4
    第36个红包的金额为：2.08
    第37个红包的金额为：0.44
    第38个红包的金额为：0.91
    第39个红包的金额为：1.97
    第40个红包的金额为：1.57
    第41个红包的金额为：1.22
    第42个红包的金额为：0.89
    第43个红包的金额为：1.38
    第44个红包的金额为：2.36
    第45个红包的金额为：1.11
    第46个红包的金额为：2.86
    第47个红包的金额为：0.71
    第48个红包的金额为：2.26
    第49个红包的金额为：1.6
    第50个红包的金额为：2.34
    第51个红包的金额为：2.32
    第52个红包的金额为：2.6
    第53个红包的金额为：0.81
    第54个红包的金额为：0.9
    第55个红包的金额为：0.75
    第56个红包的金额为：2.32
    第57个红包的金额为：1.63
    第58个红包的金额为：2.17
    第59个红包的金额为：0.51


## 随便给一个文件夹路径,统计里面文件种类和对应数量,并输出  `os.walk`


```python
import os

def count_type(path):
    a={}
    for root, dirs, files in os.walk(path):
        for i in files:
            a.setdefault(os.path.splitext(i)[1], 0)
            a[os.path.splitext(i)[1]] += 1
    return a

path = input('请输入文件夹路径:')
print(count_type(path))
```

    请输入文件夹路径:D:\QQ消息记录\923107995\FileRecv\1
    {'.pdf': 18, '.doc': 2, '.md': 1, '.docx': 2, '.xlsx': 1, '.7z': 2, '.zip': 2, '.pptx': 1}


## 在给定的文件中匹配给定样式的所有字符串并打印


```python
import os
import re
a = open("test.txt")
b = a.read()
content=('.*answer=true.*content="(.*)"')
p = re.compile(content)
print(p.findall(b))
```


    ['<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u591A\\u5149\\u8C31\\u63A2\\u6D4B</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u8D85\\u89C6\\u8DDD\\u96F7\\u8FBE</span></span></p>', '<p><span style=\\"color: black; font-family: \\u5B8B\\u4F53; font-size: 12px;\\"  >\\u53EF\\u89C1\\u5149-&gt;\\u7EA2\\u5916\\u6CE2-&gt;\\u5FAE\\u6CE2-&gt;\\u65E0\\u7EBF\\u7535\\u6CE2</span><span id=\\"_baidu_bookmark_start_512\\"  style=\\"line-height: 0px; display: none;\\"  >\\u200D</span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4EFB\\u4F55\\u7269\\u4F53\\u5BF9\\u7535\\u78C1\\u6CE2\\u90FD\\u6709\\u4E00\\u5B9A\\u7684\\u53CD\\u5C04\\u4F5C\\u7528\\uFF0C\\u53CD\\u5C04\\u7A0B\\u5EA6\\u53D7\\u7269\\u4F53\\u7279\\u6027\\u548C\\u7535\\u78C1\\u6CE2\\u6CE2\\u957F\\u5F71\\u54CD\\u3002</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E0D\\u540C\\u7269\\u4F53\\u5BF9\\u540C\\u4E00\\u6CE2\\u957F\\u7684\\u7535\\u78C1\\u6CE2\\u53CD\\u5C04\\u80FD\\u529B\\u4E0D\\u76F8\\u540C\\u3002</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u540C\\u4E00\\u7269\\u4F53\\u5BF9\\u4E0D\\u540C\\u6CE2\\u957F\\u7684\\u7535\\u78C1\\u6CE2\\u53CD\\u5C04\\u80FD\\u529B\\u4E0D\\u76F8\\u540C\\u3002</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6C14\\u8C61\\u6761\\u4EF6</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u76EE\\u6807\\u7684\\u7279\\u5F81\\u4FE1\\u606F</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u5730\\u5F62\\u5730\\u7269</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u653B\\u51FB\\u4E00\\u4F53\\u5316</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u901F\\u5EA6\\u4E0A\\u5B9E\\u65F6\\u5316</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-font-weight: bold; mso-font-kerning: 0pt;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4FA6\\u5BDF\\u624B\\u6BB5\\u4E0A\\u7684\\u7EFC\\u5408\\u5316</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u88AB\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u4F18\\u70B9\\u5BB9\\u6613\\u9690\\u853D\\u81EA\\u8EAB\\u3002</span></span></p>', '<p><span id=\\"_baidu_bookmark_start_640\\"  style=\\"line-height: 0px; display: none;\\"  >\\u200D</span><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u4E3B\\u52A8\\u63A2\\u6D4B\\u65B9\\u5F0F\\u7F3A\\u70B9\\u5BB9\\u6613\\u66B4\\u9732\\u81EA\\u5DF1\\u3002</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u672F\\u4FA6\\u5BDF</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u7565\\u4FA6\\u5BDF</span></span></p>', '<p><span style=\\"font-family: \\u5B8B\\u4F53; font-size: 9pt; mso-ascii-theme-font: minor-fareast; mso-fareast-theme-font: minor-fareast; mso-hansi-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;\\"  ><span style=\\"color: rgb(0, 0, 0);\\"  >\\u6218\\u5F79\\u4FA6\\u5BDF</span></span></p>']

## 手动实现`my_split`函数


```python
def my_split(string , fenge):

    result = []
    start_location = 0
    end_location = 0

    for i in string:
        end_location += 1
        if i == fenge:
            result.append(string[start_location:end_location - 1])
            start_location = end_location
    result.append(string[start_location:])

    return result

str=input('被加工文本:')
fenge=input('分割符:')

print(my_split(str , fenge))

```

    被加工文本:899556.65656.9.5.7878.78788.98989656.323231215487.45132.6
    分割符:.
    ['899556', '65656', '9', '5', '7878', '78788', '98989656', '323231215487', '45132', '6']


## 杨辉三角


```python
def njiecheng(n):
    i = 1
    k = 1
    while k <= n:
        i = i*k
        k += 1
    return i

line = [1]

n = float(input('请输入想要的杨辉三角的行数\n>>>'))
if n != int(n):
    print(f'你他娘的给我翻译翻译什么叫{n}行的杨辉三角!!!')
elif n <= 0:
    n = int(n)
    print(f'你他娘的给我翻译翻译什么叫{n}行的杨辉三角!!!')
else:
    n=int(n)
    print(line)
    for i in range(1,n):
        linei=[]
        for j in range(len(line)+1):
            linei.append(int(njiecheng(i)/(njiecheng(j)*njiecheng(i-j))))
            line = linei
        print(linei)
```

    请输入想要的杨辉三角的行数
    >>>15
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
    [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
    [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]
    [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]


#字棋还有大BUG，明天再看看
