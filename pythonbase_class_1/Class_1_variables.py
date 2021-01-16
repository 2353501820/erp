# -*-coding: utf-8 -*-
# @time     :2020-3-17 11:45
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_1_variables.py
# @software :PyCharm
print("hello,python!很高兴认识你")  # 代码右侧的注释需要加两个空格同时井号后面也需加个空格
# 代码上方的注释要加一个空格
"""
三个单引号或者三个单引号代表多行注释

大多数是用在类的说明，一般写在代码上方
"""
print(40000 -1200 -3980)

# 变量
sum = 40000
lili_cost = 1200
huahua_cost = 3980
print(sum - lili_cost - huahua_cost)
# 重新定义变量，华华花了3800，华华的钱直接变为3800
huahua_cost = 3800
print(sum - lili_cost - huahua_cost)

# Python关键字
import keyword
print(keyword.kwlist)

#python变量类型定义
"""
姓名：莉莉
年龄：25
工资：不到一万
体重：43.5
"""
username = "莉莉"
age = 25
pay = False
weight = 43.5

print(type(username))  # 加引号str是字符串
print(type(age))  # int是整数
print(type(pay))  # bool是布尔值
print(type(weight))  # float是浮点数（小数）