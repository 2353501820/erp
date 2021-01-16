# -*-coding: utf-8 -*-
# @time     :2020-3-31 15:45
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_3_sequence_list_tuple_dict.py
# @software :PyCharm


# 序列
# 定义：1.他的成员不是有序排列的2.可以通过偏移量访问他的成员3.不是Python中指定的数据类型4.仅仅是多种类型所支持的统一操作
# 组成：字符串、列表、元祖等
# 支持的操作：例如：定义一个包含12生肖的字符串
shengxiao = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# 1.通过索引获取指定位置上的元素
print(shengxiao[3])
# 2.切片操作（[1:]）
print(shengxiao[3:4])
# 3.成员关系操作符(in或not in)
print("牛" in shengxiao)
print("mao" not in shengxiao)
# 4.链接操作符(+)
new_shengxiao = shengxiao + "猫"
print(new_shengxiao)
# 5.重复操作符(*)
print(new_shengxiao * 3)
# 6.支持遍历(for、list)从头到尾依次从序列中获取数据，在循环内部针对每一个元素，执行相同的操作
# for item in new_shengxiao;
#     print(item)
# 7.能求长度
print(len(new_shengxiao))
print("*" * 100)
# 8.支付的内置函数all any enumerate len list max min sorted sum


# 列表
# 定义：1.一串数据2.用[]定义，数据之间使用“,”分隔3.为序列类型，支持序列的所有操作4.使用最频繁的数据类型，在其他语言中通常叫做数组
a = [1,2,3]
print(type(a))
print(list("hello"))
print("*" * 100)
# 列表相关操作
b_var = "python is good"
c_var = ["字符串",18,True,None,18,b_var,["可以","嵌套","多种","类型","包括字符串、数字、布尔值、空、变量、嵌套列表..."]]
print("源列表\n",c_var)
# 1.修改列表
# c_var[1] = 17
# print("修改后的列表：\n",c_var)
# 2.通过切片来赋值
# c_var[2:4] = [False,25]
# print("修改后的列表：\n",c_var)
# 3.插入元素（append会把插入的数据当做一个整体插入列表）
c_var.append(["列表中插入的字符串","字符串"])
print(c_var)
# extend 将序列类型的数据扩充到列表中（expend会把数据类型拆开插入列表）
c_var.extend(["序列的组成由字符串",["列表，元祖"]])
print(c_var)
# insert在指定位置插入数据
c_var.insert(5,True)
print(c_var)
# 4.删除元素
# del根据索引（元素所在位置）来删除，可以用切片删除指定位置的元素，也可以del 列表删除整个列表
del c_var[7]
print(c_var)
# remove删除第一个出现的元素，针对元素
c_var.remove(18)   #删除第一个18的元素
print(c_var)
# pop返回的是你弹出的那个数值,可以通过clear来清空列表
print(c_var.pop(1))
print(c_var)
# print(c_var.clear())
# print(c_var)
# count计算元素数量
print(c_var.count("字符串"))
# 列表排序
d_var = [5,1,90,26,65,47]
# d_var.sort()    #sort默认增序
# d_var.sort(reverse=True)   #降序
# d_var.reverse()   #倒置
# print(d_var)

# all所有元素都为True结果才为True,空序列为True
print(all(c_var))
print(all(d_var))
# any序列里只要有一个元素为True则为True
print(any(c_var))



# 元组
# 定义：1.不可修改的序列2.用于储存一串信息，数据之间使用“,”分隔3.元组用“()”定义4.元组为序列类型，支持所有的序列操作5.元组的索引从0开始
#创建元组1.括号+元素2.元素用逗号分开3.只有括号
# t = ("hello",5,2,0,True,["py",13,14])
# t_1 = "hello","python"
# t_2 = ()
# print(type(t_2))
t_3 = ("python",)  #一个元素的时候需要逗号","
print(t_3)
t_4 = (1,2,[3,4])   #元组中可以插入列表，虽然不会报错但尽量不要使用可变元素
print(t_4)
print(t_4.count(1))   #元组中出现的次数
print(t_4.index(1))   #元组中出现的位置
print("我喜欢 %s " %  t_3)   #元组会在字符串格式化的时候会使用到

"""
元组和列表间的联系
1.列表中最好保存，数据类型相似的数据。元组中保存不同类型的数据
2.由于元组为不可变类型，在遍历的时候，速度更快
3.可以作为dict字典的key，列表不可以
4.由于元组为不可变类型，可以进行写保护（保证数据不会修改）
5.列表和元组之间的转换
list(元组)
tuple(列表)
"""



# 字典
# 定义：1.除列表外最灵活的数据类型2.可以用来储存多个数据以键值对{key:value}的形式3.用{}定义4.使用键值对存储数据之间用逗号","分隔，键key是索引，值value是数据，键和值之间使用":"分开
# 键必须是唯一的，值可以是任意数据类型，但键只能使用不可变类型（字符串、数字、元组）
one_dict = {1:"hello",2:["python",True],"name":"静宝","age":2,"high":86.5}
print(one_dict[2])
# 字典相关操作
# 1.求长度 len
print(len(one_dict))   # 键值对的个数
# 2.获取某个值
print(one_dict["name"])   # 通过[]获取不存在的值会报错keyerror
print(one_dict.get("age"))   # 通过get获取不存在的值会现实None
print(one_dict.get("motto","开心就好"))   # 指定一个默认值，然后在控制台返回默认值
# 3.获取所有keys
print(one_dict.keys())
print(list(one_dict.keys()))   # 将所有的keys转化为列表
# 4.获取所有values
print(one_dict.values())
print(list(one_dict.values()))
# 获取所有的字典
print(one_dict.items())
print(list(one_dict.items()))   # 会把字典中所有的值变为元组汇总在列表中
# 5.修改值
one_dict["age"] = 2.5   # 把要修改的key取出来重新赋值
print(one_dict)
# 6.拼接两个字典 update
two_dict = {"motto":"开心就好",("hobby",):"看动漫"}
one_dict.update(two_dict)
print(one_dict)
# 7.删除指定的键值对 del pop
one_dict.pop(("hobby",))   # 删除键值对只需要删除key就行了
del one_dict[1]
print(one_dict)
# 删除最后一个键值对 popitem
one_dict.popitem()
print(one_dict)
# 清空 clear
one_dict.clear()
print(one_dict)



# 作业
# 1.在控制台依次提示用户输入姓名、网名、年龄、性别、爱好、座右铭(可以用%，format来格式化显示)
# name = input("请输入您的姓名：")
# age = int(input("请输入您的年龄："))
# sex = input("请输入您的性别：")
# hobby = input("请输入您的爱好：")
# motto = input("请输入您的座右铭：")
# print("*" * 50)
# print("个人信息展示")
# print("姓名（网名）：{}".format(name))
# print("年龄：{}".format(age))
# print("性别：{}".format(sex))
# print("爱好：{}".format(hobby))
# print("座右铭：{}".format(motto))
# print("*" * 50)

# 2.Python中的序列类型有哪些？支持哪些操作？
# 字符串、列表、元组
# 切片，求长度len，连接+，重复*，索引，遍历
# 3.编写代码，用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，打印输出“周末”（提示：可以使用序列中任何一种类型）
# week = ("周一","周二","周三","周四","周五","周末","周末")
# number = int(input("请输入数字1-7："))
# print("今天是：{}".format(week[number - 1]))
# 4.列表中append和extend方法的区别，请举例说明
# f_var = [1,2,3]
# f_var.append(("加一",1))  #append会把数据作为一个整体加入到列表中
# f_var.extend(("加一",1))  #extend会把数据拆分成原有的数据类型加入到列表中
# print(f_var)
# 5.删除如下列表中的"矮丑穷",写出你能想到的所有方法
# keyou_info = ["可优",18,"男","矮丑穷",["高","富","帅"],True,None,"Always Be Coding"]
# del keyou_info[3]
# keyou_info.remove("矮丑穷")
# print(keyou_info.pop(3))
# print(keyou_info)
# 6.元组和列表有什么区别，分别应用在哪些场景
# 元组不可修改，列表可修改 元组可以作为字典的key值 元组因为不可修改遍历的时候更快 列表保存相似的数据结构，元组保存不同的数据结构
# 7.创建元组有哪些方式
# 空括号  逗号  括号+逗号
# 8.定义两个字典用于表述你的个人信息
# 第一个字典存放你的这些信息：姓名，性别，年龄，身高
a_dict = {"姓名":"静宝","性别":"女","年龄":2,"身高":86}
# 第二个字典存放你的其他信息：性格，爱好，座右铭
b_dict ={"性格":"活泼","爱好":"机器猫","座右铭":"宝儿玩好不"}
# a)将两个字典合并为第三个字典之后，打印出来b)觉得自己很年轻，可以去整个容（修改年龄，）然后露个脸（打印出来）c)对你的座右铭很感兴趣，请将其取出来d)字典支持的序列类型的哪些操作，尝试一下
a_dict.update(b_dict)
print(a_dict)
a_dict["年龄"] = 2.5
print(a_dict["年龄"])
print(a_dict.get("座右铭"))
# 求长度len 获取[],get  修改[]= 连接update 删除pop del[] popitems clear
