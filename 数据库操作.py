# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 12:21:55 2017

@author: Lenovo-Y430p
"""
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='666666',charset='utf8')  
cursor = conn.cursor()
cursor.execute('drop database if exists python')
cursor.execute("""create database if not exists python""")
conn.select_db('python');
cursor.execute("""create table if not exists test(FIRST_NAME CHAR(20),
         LAST_NAME  CHAR(20),
         AGE FLOAT,  
         votage CHAR(20),
         LABEL FLOAT)""")
f = open("E:\下载\机器学习实战及配套代码\machinelearninginaction\Ch06\shuju.txt", "r")
while True:
    line = f.readline()
    if line:
        #处理每行\n
        line = line.strip('\n')
        line = line.split("\t")
        tel = str(line[0])
        province = line[1]
        city = line[2]
        call_type = line[3]
        label1=line[4]
        cursor.execute("insert into test (FIRST_NAME,LAST_NAME,AGE,votage,LABEL) values(%s,%s,%s,%s,%s)",[tel, province, city, call_type, label1])
    else:
        break
f.close()
cursor.close()
conn.commit()
conn.close()
# -*- coding: UTF-8 -*-
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost","root","666666","python" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE test SET AGE = AGE + 1 WHERE LABEL =1.0 "
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","666666","python" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM test WHERE AGE > '%d'" % (4)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()
import sys
#连接mysql，获取连接的对象
con = MySQLdb.connect('localhost', 'root', '666666', 'python');
with con:
    #仍然是，第一步要获取连接的cursor对象，用于执行查询
    cur = con.cursor()
    #类似于其他语言的query函数，execute是python中的执行查询函数
    cur.execute("SELECT * FROM test")
    #使用fetchall函数，将结果集（多维元组）存入rows里面
    rows = cur.fetchall()
    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    for row in rows:
        print (row)



