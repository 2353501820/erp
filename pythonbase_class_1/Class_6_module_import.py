# -*-coding: utf-8 -*-
# @time     :2020-7-21 14:35
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_6_module_import.py
# @software :PyCharm
# import Class_6_module_faction


# print(Class_6_module_faction.cube(10))
# print(Class_6_module_faction.square(10))
# print(Class_6_module_faction.num_abs(-20))


# 模块
# 定义：1.模块好比工具包2.每个以拓展名.py结果的文件都是一个模块3.全局变量、函数、类都是模块能够提供给外界直接使用的工具4.可重用代码

# 模块名：1.标识符可以用字母、数字、下划线组成2.不能以数字开头3.不能与关键字重名4.不能与系统内置的模块、函数、类重命名5.建议不要用下划线开头6.建议不要用中文（如果以数字开头，pycham无法导入）

# 模块导入方式：
# 1.import导入 （import 模块名1,模块名2）导入模块时每个导入应该独占一行(规范)，导入之后通过模块名.来使用模块所提供的工具——全局变量、函数、类
# 2.as指定别名 如果模块的名字太长，可以使用as指定模块的名称，以方便在代码中的使用（import 模块名 as 模块别名）模块别名应符合大驼峰命名法
# import Class_6_module_faction as Mo_f
# print(Mo_f.square(10))
# 3.from ... import 导入 1)导入部分工具2)可以使用 from ... import 3)import模块名是一次性把模块中的所有工具全部导入，并且通过模块名/别名访问
# 从模块导入某一工具 from ...模块名 import 工具名 导入之后 1)不需要通过模块名2)可以直接使用模块所提供的工具——全局变量、函数、类
# 如果两个模块存在同名函数，那么后导入模块的函数会覆盖掉先导入的函数，应统一写在代码的顶部更容易及时发现冲突，一旦发现冲突，可以使用as关键字给其中一个工具起一个别名
# from ... improt * 从模块中导入所有工具 from 模块名 import * 注意，这种方式不推荐使用，因为函数重名没有任何提示，出现问题不好排查
# from Class_6_module_faction import cube
#
# print(cube(10))
# 需要导入多个函数可以用括号，中间用逗号分隔
from Class_6_module_faction import (
cube,
square,
num_abs
)
print(num_abs(-10))

# 模块的搜索顺序：
# 1.在导入模块时，搜索当前目录指定模块名的文件，如果有就导入2.如果没有再搜索系统目录3.sys.path4.每个模块都有一个内置属性_file_可以查看模块的完整路径（给文件起名时不要和系统的模块文件重名）
# 原则：每个py文件都应该是可以被导入的，一个独立的Python文件就是一个模块，在导入文件时，文件中所有没有任何缩进的代码都会被执行一遍
# 实际开发场景：在实际开发场景中，没一个模块都是独立开发的，大多都有专人负责，开发人员通常会在模块下方增加一些测试代码（仅在模块内使用，而被导入到其他文件中不需要执行）
# _name_属性：测试模块的代码只在测试情况下被运行，而在被导入时不会执行，_name_是一个内置属性，如果被其他文件导入的，_name_就是模块名，如果是当前执行的程序_name_是_main_
# if __name__ == '__main__':

# 包
# 概念：1.包是一个包含多个模块的特殊目录2.目录下有一个特殊的文件_init_.py3.包名的命名方式和变量名一致，小写字母+ _   好处：使用import包名 可以一次性导入包中所有的模块


# os模块
# os模块有许多方法让我们通过代码实现创建，删除和更改目录
# os.getcwd():getcwd()方法显示当前的工作路径，只具体到路径，不具体到文件
# os.path.join(a,b):连接两个部分的路径，组成一个完整的路径
# os.mkdir(路径名字):在某个目录下创建一个新目录
# os.rmdir(路径名字):删掉一个目录
# os.listdir():获取当前路径下的目录列表
# os.path.isdir:判断当前文件是否是目录， 返回布尔值
# os.path.isfile：判断当前文件是否是文件， 返回布尔值

import os

# 操作系统名称
print(os.name)

# 当前路径
print(os.getcwd())

# 系统环境变量
print(os.environ)

# 创建文件夹，已存在会报错
# os.mkdir("test1")

# 创建多个嵌套文件夹
# os.mkdir("C:/Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\test1\test2")   # 会报错，不存在要先创建
# os.makedirs("C:/Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\test1\test2")

# 删除目录
# os.rmdir("C:/Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\test1")   # 会报错，若文件夹非空，需删除子文件夹
# os.removedirs("C:/Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\test1\test2")   # 删除多级目录文件夹，一级一级删

# 列出指定路径下的目录结构
# print(os.listdir(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1"))
# 这里发现一个非常有意思的现象 你的path目录用的是"\"Python很多时候会报错，不能转义，这时候地址可以用"/"或者加r用以区分
# 在Python中 \ 是转义符，\u表示其后是UNICODE编码，因此\User在这里会报错，在字符串前面加个 r（rawstring  原生字符串），可以避免python与正则表达式语法的冲突！

# 返回路径的文件名
# os.path.basename(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\Class_1_variables.py")

# 返回除文件名之外的路径
# os.path.dirname(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\Class_1_variables.py")

# 判断路径中文件名是否存在
# os.path.exists(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\Class_1_variables.py")   # True为存在，False为不存在

#判断路径是否是目录
# os.path.isdir(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1")   # True为是，False为否

#判断路径是否是文件
# os.path.isfile(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\Class_1_variables.py")   # True为是，False为否

# 合并
# os.path.join(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1","Class_1_variables.py")   # 根据所属的平台使用特定的符号进行拼接，苹果电脑是"/"windows是"\"

# 切割
# os.path.split(r"C:\Users\ls\PycharmProjects\python-ls_1\pythonbase_class_1\Class_1_variables.py")   # 根据路径中最后一个斜杠来进行分割，会分成basename和dirname


# 作业
# 一、必做题
# 1.什么是模块?有什么作用?
# 每个py文件都是一个模块，可以调用函数、类、全局变量，可以重用代码
# 2.模块中的哪些资源可以被调用处使用?
# 函数、类、全局变量
# 3.模块的命名规范
# 以数字、字母、下划线组成，不能以数字开头，不能与关键字重名，不能与系统内置的函数、类、关键字重名（建议不要用下划线开头，不要用中文）
# 4.模块的导入方式有哪几种?
# import path 模块名   导入模块中所有的函数、类、全局变量
# from 模块名 import 方法   导入模块中固定的函数、类、全局变量
# 5.name属性的特性?
# 测试模块的代码只在测试情况下被运行，而在被导入时不会执行，_name_是一个内置属性，如果被其他文件导入的，_name_就是模块名，如果是当前执行的程序_name_是_main_
# 6.将两个变量的值进行交换(a=100，b=200)
# a = 100
# b = 200
# a,b = b,a
# print(a,b)
# 7.包是什么?
# 8.os模块中有哪些常用的方法?用什么作用?
# os.mkdir os.rmdir os.getcwd() os.path.join(a,b) os.listdir
# 9.编写如下程序
# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# b.在每个模块中需要添加测试代码

# import pythonbase_class_1.pythonbase_import.Import_homework_faction as im_h_f
#
#
# radius = float(input("请输入圆的半径："))
# print("半径为{:.2f}的圆，面积为{}，周长为{}".format(radius,im_h_f.area_circle(radius),im_h_f.circumference_circle(radius)))
# rectangle_long = float(input("请输入长方形的长："))
# rectangle_short = float(input("请输入长方形的宽："))
# param = (rectangle_long,rectangle_short,im_h_f.area_rectangle(rectangle_long,rectangle_short),im_h_f.circumference_rectangle(rectangle_long,rectangle_short))
# print("长为{},宽为{},的长方形，面积为{},周长为{}".format(*param))
from pythonbase_class_1.pythonbase_import.Import_homework_faction import (
area_rectangle,
circumference_circle,
area_circle,
circumference_rectangle
)


radius = float(input("请输入圆的半径："))
print("半径为{:.2f}的圆，面积为{}，周长为{}".format(radius,area_circle(radius),circumference_circle(radius)))
rectangle_long = float(input("请输入长方形的长："))
rectangle_short = float(input("请输入长方形的宽："))
param = (rectangle_long,rectangle_short,area_rectangle(rectangle_long,rectangle_short),circumference_rectangle(rectangle_long,rectangle_short))
print("长为{},宽为{},的长方形，面积为{},周长为{}".format(*param))


