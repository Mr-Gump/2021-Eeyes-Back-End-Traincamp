#!/usr/bin/python3
# PyMYSQL 连接 MySQL 数据库
# pip3 install PyMySQL
 
import pymysql

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';

db = pymysql.connect(host="localhost", port=3306,database='myemployees',user = 'root',password='888888')

try:

    # 使用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SHOW TABLES;'''
        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)
        result = cursor.fetchall()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally: 
    # 关闭数据库连接
    db.close()

 
print (f"Result {result} ")
