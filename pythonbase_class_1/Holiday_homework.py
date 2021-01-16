# -*-coding: utf-8 -*-
# @time     :2020-7-8 15:14
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :holiday_homework.py
# @software :PyCharm
# 假期小测试
# 简答题
# 1.注释是用来做什么的?注释分几类?分别如何定义?
# 注释的用途：a、提示、防遗忘b、给程序添加说明信息c、特殊含义，指定编码
# 注释分为：两类 a、单行b、多行
# 定义：
#    a、单行
#    # 这是一条注释
#     程序上方
#     程序右侧
#    b、多行：
#     """
#     '''
# 2.变量的命名应当符合什么规则
# 1)不能用关键字命名2)不能用数字和下划线开头3)只能使用字母、数字、下划线（我自己做的）
# a、由 字母、下划线 和 数字 组成
# b、不能以数字开头
# c、不能与关键字重名
# d、建议不要与内置函数或者累重名，不然会覆盖原始内置函数的功能
# e、区分大小写
# f、如果 变量名 需要由 二个 或 多个单词 组成时，每个单词都使用小写字母，单词与单词之间使用 _下划线 连接（标准答案）
# 3.Python中关键字有哪些?请至少写出10个
# for in function while and print range def if elif else pass randint break continue is or None True False
# 4.变量的类型有哪些?
# 数字类型：int float 布尔型(True、False) 复数型
# 非数字类型： 字符串 元组 列表 字典
# 5.如何查看变量的内存地址、变量的类型以及如何比较两个变量值的大小?
# id type ==
# 6.数字类型的字符串(如：“123”)与数字类型之间如何相互转换?
# int float   str
# 7.字符串与列表之间如何相互转换?
# 字符串转换为列表 str.split("")   列表转换为字符串"".join列表
# 8.布尔类型与数字类型之间如何相互转换?
# 布尔转换为数字：int() float()
# 数字转换为布尔：bool()
# 9.Python中的运算符有哪些种类?
# 逻辑运算 比较运算 赋值运算 算术运算
# 10.Python中逻辑运算符有哪些?它们之间有什么区别?
# and 两真为真，一假为假 or 一真为真，两假为假 not 两假才为真
# 11.序列类型是Python中指定的类型吗?属于序列类型的数据类型有哪些?
# 不是 仅是多种类型所支持的统一操作
# 12.序列类型支持哪些操作?
# 通过索引获取值(index) 切片 成员关系操作符(in or not in) 连接操作(+) 重复操作(*) 支持遍历(for list) 能求长度(len) 支持内置函数(all any list len max min sum)
# 13.字典支持序列中的哪些操作
# 成员运算(not in 、in)，支持遍历(for list)求长度(键值对的个数) 支持内置函数(all any list len)
# 14.range支持序列中的哪些操作
# 不可变序列类型 通过索引获取值 切片 成员运算 支持遍历 能求长度 支持内置函数(all any list len)
# 15.有哪些方法可以修改列表中的某个元素呢?
# 索引：列表[index] = value
# 切片：列表[start_index:end_index] = value
# 16.列表中的append和extend的区别
# append会当做一个数据整体插入列表 extend会拆分数据类型插入列表
# 17.元组和列表之间如何相互转换?
# list()  tuple()
# 18.获取字典中的某个值，有喇几种方法?有什么区别?
# 字典.key 通过[]获取不存在的值会报错keyerror   字典.get(key)通过get获取不存在的值会现实None
# 19.如何将一个字典的键、值键值对分别转化为元组?
# 拆包(a,b),(c,d)=字典.items  print(a,b,c,d)
# tuple(字典.keys())
# tuple(字典.values())
# tuple(字典.items())
# 20.我们学过的、不可变类型有哪些?可变类型有哪些?
# 可变：列表 字典 不可变：元组 整型 浮点型 字符串 布尔
# 21.Python中是用什么方法来进行输出操作的?它有哪些常用的参数呢?
# print end sep
# 换行：end = \t
# sep默认为空格，可以更换 例：sep = "#"
# 22.程序执行的流程有哪几种?
# 顺序：默认为顺序执行(从上到下) 分支：if  循环：for、while
# 23.for和while的区别?
# for 支持遍历 循环次数已知，推荐使用 while 循环次数不确定
# 24.局部变量和全局变量有什么区别?
# 局部变量作用于函数内部的作用域 全局变量作用于外部作用域

# 编程题
# 1.编写如下程序
# 使用while循环实现输出2-3+4-5+6...+100的和
i = 2   # 定义一个循环变量
result = 0   # 定义一个变量用于保存结果
while i <= 100:   # for i in range(2,101):
    if i % 2 == 0:
        result += i
    else:
        result -= i
    i = i + 1
print(result)
# 2.编写如下程序
# 用户输入考试成绩，当分数高于90(包含90)时打印A：否则如果分数高于80(包含80)时打印B；否则如果当分数高于70(包含)时打印C：否则如果当分数高于60(包含60)时打印D：其他情况就打印E
grade_score = float(input("请输入你的考试分数："))
if grade_score >= 90:
    print("A")
elif grade_score >= 80:
    print("B")
elif grade_score >= 70:
    print("C")
elif grade_score >= 60:
    print("D")
else:
    print("E")
# 3.编写如下程序
# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番(例如：需要几年10000才能变成20000)
own_money = float(input("你的本金为："))
total_money = own_money * 2   # 定义变量用于保存总钱数
year = 1   # 定义用于计算年份
while own_money < total_money:
    # own_money = (own_money * 0.0352) + own_money
    own_money *= (0.0352 + 1)
    year = year + 1
print("定期利率为3.52%，需要{}年才能让定期存款连本带息的翻一番".format(year))
# 4.编写如下程序
# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出提示：
# a.1!等于1
# b.2!等于1*2
# c.3!等于1*2*3
# d.n!等于1*2*3*...*n
# n = int(input("请输入一个非负的数字："))    # 负数不算阶乘


# factorial = 1
# number = int(input("请输入你计算阶乘的数字："))
# if number < 0:
#     print("{}! 没有阶乘".format(number))
# elif number == 0:
#     print("{}! 等于1".format(number))
# else:
#     for i in range(1, number + 1):
#         factorial *= i
#     print("{}! 等于{}".format(number, factorial))


def is_int(int_num):
    """
    check whether int_num is integer!
    :param int_num:
    :return:
    """
    if isinstance(int_num,str):   # 判断是否为字符串类型，isinstance就是判断传给我的第一个参数是否是第二个类型
        if int_num.isdigit():    # 判断是否为数字类型的字符串
            return True
        else:
            return False
    elif isinstance(int_num,int):   # 判断是否为整数类型
        return True
    else:
        return False


def factorial_num(one_num):
    """
    count one_nums factorial
    :param one_num:
    :return:
    """
    factorial = 1
    if one_num < 0:
        print("{}为负数，没有阶乘".format(one_num))
        return None
    elif one_num == 0:
        return 1
    else:
        for item in range(1,one_num + 1):
            # result_1 *= item
            factorial = factorial * item
        return factorial


input_num = input("请输入一个正整数")
if is_int(input_num):
    input_num = int(input_num)
    print("{}的阶乘为{}".format(input_num,factorial_num(input_num)))
else:
    print("输入的{}有误，请输入一个正整数".format(input_num))
# 字符串.replace(".","","1")   相当于把.替换为空只替换一个
# 20190408的作业讲解后面老师讲的作业好像没做过，有空研究一下，网址是：https://blog.csdn.net/bacong6585/article/details/102365412/
