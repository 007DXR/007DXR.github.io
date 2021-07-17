# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:09:29 2021

@author: DEER
"""

import sqlite3
#创建与数据库的连接
conn = sqlite3.connect('2011-2021天气汇总.db')
curs = conn.cursor()
# #创建关系表
# curs.execute('''
# CREATE TABLE if not exists favorites(id INTEGER, title TEXT, PRIMARY KEY(id))
#         ''')
# #清空表中已有内容
# curs.execute('''DELETE FROM favorites''')
#提交操作
# conn.commit()

#构建SQL语句

SQL = "CREATE TABLE if not exists 江苏(data,weather,temperature,wind);"
curs.execute(SQL)
query = "INSERT INTO 江苏 VALUES(?,?,?,?)"
#从csv文件向表格中导入数据
for line in open('./output/南京.csv'):
    line = line.strip('\n')
    fields = line.split(',')
    curs.execute(query,fields)
    
print('insert data sucessfully')
conn.commit()

#执行查询，检查数据是否插入成功
curs.execute('SELECT *FROM 江苏')
print(curs.fetchall())
print ("Operation done successfully")
#关闭数据库
conn.close()