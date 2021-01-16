# -*-coding: utf-8 -*-
# @time     :2020-5-13 16:42
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_4_if_while_for.py
# @software :PyCharm


# if
# 定义：1.如果条件满足才能做某件事情2.如果条件不满足，就做另一件事情或者什么也不做

# 基本语法
#if 要判断的条件：
#   条件成立时，要做的事情     代码缩进用一个Tab键，或者四个空格（注意不要Tab和空格混用）

"""
if 判断条件：
     条件满足执行的逻辑
继续往下执行



if 判断条件：
    条件满足执行的逻辑
else:
    条件不满足执行的逻辑
继续往下执行



if 判断条件一：
    条件一满足执行的逻辑
elif判断条件二：
    条件二满足执行的逻辑
else:
    条件条件一和条件二都不满足执行的逻辑
继续往下执行
"""

# 1.定义年龄变量
# age = int(input("你多少岁?"))
# 2.判断是否为18岁
# 3.如果满足条件，提示可以进网吧
# 4.如果条件不满足，提示你未成年，不可以进入
# if age <= 18 and age >= 70:
#     print("可以进网吧")
# else:
#     print("你未成年，不可以进入")
# 求三个整数的最大值
# num_1 = int(input("请输入第一个数字："))
# num_2 = int(input("请输入第二个数字："))
# num_3 = int(input("请输入第三个数字："))
# if num_1 > num_2:
#     max_num = num_1
# else:
#     max_num = num_2
# if max_num < num_3:
#     max_num = num_3
# print("你输入的最大数字是：{}".format(max_num))

# if 的进阶语句  elif
# 定义：1.如果希望再增加一些条件，条件不同，需要执行的代码也不同时，就可以使用elif2.elif和else都必须if联合使用3.可以将if、else、elif以及各自缩进的代码看出一个完成的代码块
# 1.定义holiday_name字符串变量来记录节日名称
# 2.如果是情人节应该买玫瑰/看电影
# 3.如果是平安夜应该吃苹果/吃大餐
# 4.如果是生日应该买蛋糕
# 5.其他的日子只要有爱每天都想过节
# holiday_name = input("请输入节日：")
# if holiday_name == "情人节":
#     print("情人节应该买玫瑰/看电影")
# elif holiday_name == "平安夜":
#     print("平安夜应该吃苹果/吃大餐")
# elif holiday_name == "生日":
#     print("生日应该买蛋糕")
# else:
#     print("只要有爱,每天都想过节")

# if嵌套
# 定义：1.elif的应用场景是：同时判断多个条件，所有的条件是平级的2.使用if进行条件判断，如果希望在条件成立的执行语句中再增加条件判断，就可以使用if嵌套3.语法格式除了缩进以外和之前没有区别
# 1.定义布尔值变量has_ticket表示是否有车票
# 2.定义整型变量knife_length表示刀的长度，单位：厘米
# 3.首先检查是否有车票，如果有才允许进行安检
# 4.安监时需要检查刀的长度，判断是否超过20厘米，如果超过20厘米，提示刀的长度不允许上车；如果不超过20厘米，安检通过
# 5.没有车票，不允许进门
# has_ticket = bool(int(input("是否有车票(0代表没有，1代表有)：")))
# if has_ticket:
#     knife_length = int(input("检查刀的长度："))
#     print("请进")
#     if knife_length <= 20:
#         print("安检通过")
#     else:
#         print("您携带的刀的长度是{}厘米，超过20厘米不允许上车".format(knife_length))
# else:
#     print("没有车票，不允许进门")


# 循环
# 定义：1.顺序-从上到下，顺序执行代码2.分支-根据条件判断，决定执行代码的分支3.循环-让特定代码重复执行



# while循环
# 定义：指定的代码重复执行
# 打印5遍hello python
# 1.定义计数器
i = 1   #指定初始值

while i <= 5:
    print("hello,python")
    i += 1   #修改计数器

print("循环结束后i = {}".format(i))



#死循环：忘记在循环内部修改循环的判断条件，导致循环持续执行，程序无法终止！



#循环计算
# 在程序开发中，通常会遇到利用循环重复计算的要求，遇到这种情况可以：1.在while上方定义一个变量，用于存放最终计算结果2.在循环内部，每次循环都用最新的计算结果，更新之前定义的变量
# 计算0-100之间所有数字的累计求和结果
# 1.定义一个最终结果的变量
result = 0
# 2.定义一个计数器
b = 0
# 3.定义循环条件

while b <= 100:
    result = result + b
    b = b + 1
print(result)
print("循环结束后b = {}".format(b))

# 计算0-100之间所有偶数的累计求和结果
r = 0
a = 0

while a <= 100:
    if a % 2 == 0:
        r = a + r
    a = a + 1

print(r)




# break和continue
# 定义：1.break和continue是专门在循环中使用的关键字2.break某一条件满足时，退出循环，不再执行后续重复的代码3.continue某一条件满足时，不执行后续重复的代码，开始下一次循环4.break和continue只针对当前所在循环有效
# 打印0-9，遇到3 不打印
c = 0   #定义一个计数器
while 0 <= c <= 9:
    if c == 3:
        break
    print(c)
    c = c + 1
# 打印0-9，不打印3
d = 0
while 0 <= d <= 9:
    if d == 3:
        d = d + 1
        continue   #使用continue之前一定要修改计数器，不然极有可能出现死循环
    print(d)
    d = d + 1




# 作业
# 1.判断是否为闰年，提示：输入一个有效年份（如2019），判断是否为闰年，如果是闰年则打印：“2019是闰年”；否则打印“2019不是闰年”
# year = int(input("请输入一个有效年份："))
# if year % 4 == 0 and year % 100 != 0:
#     print("{}是闰年".format(year))
# elif year % 400 == 0:
#     print("{}是闰年".format(year))
# else:
#     print("{}不是闰年".format(year))

# 2.使用if语句完成剪刀石头布游戏，提示：1.提示用户输入要出的拳--石头（1）/剪刀（2）/布（3）2.电脑随机出拳3.比较胜负、显示用户胜、负还是平局
"""
电脑随机出拳
1.使用随机数，首先需要导入随机数的模块--“工具包”
import random
2.导入模块后可以直接在模块名称后敲一个.然后按Tab键，会提示该模块中包含的所有函数
random.randint(a,b),返回[a,b]之间的整数，包含a和b
例如：
random.randint(1,10)生成随机数n:1 <= n <= 10
random.randint(4,4)结果永远是4
random.randint(25,12)该语句是错误的，下限必须小于上限
"""
import random

user1 = int(input("请输入要出的拳--石头（1）/剪刀（2）/布（3）："))
# if user1 == 1:
#     user1 = "石头"
# elif user1 == 2:
#     user1 = "剪刀"
# elif user1 == 3:
#     user1 = "布"
# else:
#     print("请输入正确的数字")
computer = random.randint(1,3)
# if computer == 1:
#     computer = "石头"
# elif computer == 2:
#     computer = "剪刀"
# else:
#     computer = "布"
# print("电脑输入的是{},用户输入的是{}".format(computer,user1))
# if ((computer == "石头" and user1 == "剪刀")
#     or (computer =="剪刀" and user1 =="布")
#     or (computer == "布" and user1 == "石头")):
#     print("用户负")
# elif computer == user1:
#     print("平局")
# else:
#     print("用户胜")


user_win = ((1,2),(2,3),(3,1))
if (user1,computer) in user_win:
    print("用户胜")
elif user1 == computer:
    print("平局")
else:
    print("用户负")

# 3.分别使用while和for打印九九乘法表   print不换行print("2",end = \t)

hang = 1   #定义行
e = 0   #定义结果

while hang < 10:
    lie = 1   #定义列
    while lie <= hang:
        e = lie * hang
        # print("{}*{}={}".format(lie, hang, e),end="\t")
        print("*",end="\t")
        lie = lie + 1
    print("")
    hang = hang + 1


# 字符串中的转义字符
# 1.\\  反斜杠符号2.\'  单引号3.\"  双引号4.\n  换行5.\t  横向制表符6.\r  回车




# for循环！！！！！（1.通常循环的次数可以确定的情况下用for循环，否则用while2.能用for循环尽量不用while，因为for循环效率更高3.要做遍历的时候只能使用for循环）
# 定义：1.可以遍历任何序列类型：元组、字符串、列表、字典2.通过遍历对象的长度来控制循环次数3.遍历完毕，循环即结束

one_list = ["静宝",2,True,("是我家宝宝")]
for item in one_list:
    print(item)   #item相当于一个变量，把列表中所有的值都赋值给item

# 遍历方式
# 1.按下标遍历
index_list = [0,1]
for i in index_list:
    print(one_list[i])
# 2.直接遍历序列



# 遍历字典
# 1.只对键遍历
no_dict ={"姓名":"静宝","年龄":2,True:False}
for i in no_dict:
    print(i)
# 2.对键和值都进行遍历
for i in no_dict.items():
    print(i)
for key,value in no_dict.items():   # 定义两个变量相当于元组拆包，定义的值必须一一对应
    print("key = {},value = {}".format(key,value))




