#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_mysql.py
# author:liushen
# time:2020/12/31
# 需要使用第三方库 pymysql mysqlclient(不推荐)
import pymysql


# 1.建立连接
# host 主机 db 数据库名称 charset 编码集 cursorclass 游标类
conn = pymysql.connect(host="test.lemonban.com",user="test",password="test",db="future",port=3306,charset="utf8",cursorclass=pymysql.cursors.DictCursor)
# 2.创建游标
cursor_1 = conn.cursor()
# 3.执行sql语句
# sql = "SELECT * FROM `member` LIMIT 0,10;"
# sql_1 = "SELECT * FROM `member` WHERE LeaveAmount > 400 LIMIT 0,10;"   #sql语句中最好不要使用参数，不然很容易出现数据库注入的问题
sql_1 = "SELECT * FROM `member` WHERE LeaveAmount > %s LIMIT 0,10;"
cursor_1.execute(sql_1,args=(400,))   # 这里的args一定是序列类型
# 需要手动提交
conn.commit()
# 4.获取结果
result_1 = cursor_1.fetchone()   # 返回所有记录中的第一条记录组成的字典
result_2 = cursor_1.fetchall()   # 返回所有记录组成嵌套的字典的列表 如果先执行fetchone再执行fetchall，会少第一条
# 5.关闭连接
cursor_1.close()   # 先关游标对象
conn.close()   # 然后再关连接对象
