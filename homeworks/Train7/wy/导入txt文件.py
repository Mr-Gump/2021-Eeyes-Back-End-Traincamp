# copy别人的

import pymysql
import json
# 读txt文件
f = open('2017_storage.txt')
data = f.readlines()

# 连接数据库，获取游标
con = pymysql.connect(host='10.206.131.83', port=3306, user='skyaiduser', password='skyaid8.6', db='skyaid_webservice', charset='utf8')
cur = con.cursor()

# 执行sql语句
for line in data:

    A = line.strip('\n').split('|')
    # print(A)  # 这是未去掉空格的列表

    A2 = []
    for a in A:
        b = a.strip(' ')
        A2.append(b)
    # print(A2)  # 这是去掉空格之后的列表

    s = {'kbids': A2[1:]}  # 转成字典
    # print(s)

    a_json = json.dumps(s)
    # print(a_json)  # 转成json字符串

    sql = "insert into support_search_keyword_pattern(keyword,kbid_array,create_date)values(\"%s\",'%s',now())"
    sql1 = sql % (A2[0], a_json)
    # print(sql1)

    cur.execute(sql1)
    con.commit()

cur.close()
con.close()
