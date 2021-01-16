# -*-coding: utf-8 -*-
# @time     :2020-6-2 16:16
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_5_function.py
# @software :PyCharm
# 函数！！！！！
# 含义：1.把具有独立功能的代码块组织为一个小模块，在需要的时候调用2.定义函数--封装独立的功能，调用函数--享受封装的成果3.提高编写的效率、代码的重用4.让程序更小、模块化
# 格式：
'''
def 函数名():
"""
注释信息
"""
函数封装的代码
...
函数名称应符合标识符命名规则：1.见名知意2.由字母、数字、下划线组成3.不能以数字开头4.不能与关键字重名
'''


def say_hello():
    """
    greet,say hello!
    :return:
    """
    print("来唱首歌吧！")


print("你好")
say_hello()   #函数在定义的时候不会执行，只有在调用的时候才会执行，调用函数一定要加()，具体操作方法为：函数名+()
print("春天在哪里呀\n春天在哪里\n...")

# debug
# 1.F8 Step Over可以单步执行代码，会把函数调用看作是一行代码直接执行2.F7 Step Into可以单步执行代码，如果是函数，会进入函数内部


# 函数的文档注释
# 1.给函数添加注释：在函数定义的下方，使用连续的三对引号2.在连续的三对引号之间编写对函数的说明文字3.使用函数名._doc_可以查看注释4.在函数调用位置，使用Ctrl+Q可以查看函数的说明信息
# 注意：因为函数相对比较独立，函数定义的上方和下方，应和其他代码（包括注释）保留两个空行
# print(say_hello.__doc__)


# 传参-----------------定义函数时，形参定义的顺序为：位置参数，默认参数，可变参数（默认参数一定要放在位置参数后面，而可变参数的位置没有强制性，一般为最右侧）
# 调用函数时，实参的传递顺序为：位置参数（可以由序列类型拆包生成），关键字参数（可以由字典类型拆包生成），调用优先按照传参顺序调用


def two_num_mulpitly(num_1,num_2):   #定义的时候是形参
    """
    two number mulpitly
    :return:
    """
    # num_1 = 30
    # num_2 = 15
    result = num_1 * num_2
    print("{} * {} = {}".format(num_1,num_2,result))


two_num_mulpitly(30,14)   # 调用的时候是实参


# 位置参数：实参和形参一一对应


# 关键字参数：为参数指定名称
two_num_mulpitly(num_1=14,num_2=30)   # 关键字等号两边不需要空格


# 默认参数：1.给参数指定默认值2.例：列表sort()默认参数是reverse3.简化函数的调用4.调用函数时，如果没有传入缺省参数的值，则在函数内部使用指定的参数默认值5.将常见的值设置为参数的缺省值，从而简化函数调用


def two_num_mulpitly_2(num_1,num_2 = 10,num_3 = 12):   # 必须保证带有默认值的缺省参数在参数列表末尾
    """
    two number mulpitly
    :return:
    """
    result = num_1 * num_2 * num_3
    print("{} * {} * {} = {}".format(num_1,num_2,num_3,result))


two_num_mulpitly_2(14)


# 可变参数
# 定义：一个函数能够处理的参数个数是不确定的时候，就可以使用多值参数
# Python有两种多值参数：1.参数名前面加一个* 可以接收元组2.参数名前面加两个* 可以接收字典
# 一般在给多值参数命名时习惯使用以下两种名字：1.*args--存放元组的参数 2.**kwargs--存放字典的参数（args是arguments的缩写，有变量的含义；kw是keyword的缩写，kwargs可以记忆为键值对参数）
# 拆包：如果希望将一个元组变量（字典变量）直接传递给args（kwargs）就可以使用拆包来简化参数的传递，方式为：在元组变量（字典变量）前加一个*（加两个**）


def params_1(*params):
    """
params is Variable parameters
    :return:
    """
    print("params为{}".format(params))
    print("类型：{}".format(type(params)))


params_1("静宝",2.5,"girl")   # *params打包为元组，这里存放的是位置参数


def params_2(*params,**kw_params):
    """
params is Variable parameters
kw_params is Variable position parameters
    :return:
    """
    print("params2为{}".format(params))
    print("类型：{}".format(type(params)))

    print("kw_params2为{}".format(kw_params))
    print("类型：{}".format(type(kw_params)))


params_2("静宝",2.5,"girl",hobby = "宝儿玩好不")   # **kw_params打包为字典，这里存放的是关键字参数，关键字参数不能出现在位置参数前面


def params_3(*params,**kw_params):
    """
params is Variable parameters
kw_params is Variable position parameters
    :return:
    """
    print("params3为{}".format(params))
    print("类型：{}".format(type(params)))

    print("kw_params3为{}".format(kw_params))
    print("类型：{}".format(type(kw_params)))


a_type = ("静宝",2.5,"girl")
b_type = {"hobby": "宝儿玩好不"}
# params_3(a_type,b_type)   # 这里如果是写a_type,b_type则代表*params(位置参数)，**kw_params是空的
params_3(*a_type,**b_type)   # params_3("静宝",2.5,"girl",hobby= "宝儿玩好不")这种方法适用于位置参数非常多，可以先把位置参数拆出来

# 字典的拆包
a_dict = {"name": "静宝","age": 2.5}
# a,b = a_dict
# print(a,b)   # 拆包为key
# a,b = a_dict.items()
# print(a,b)   # 拆包为元组
(a,aa),(b,bb) = a_dict.items()
print(a,aa,b,bb)


# 拓展
# 计算一串数字的和


# def sum_num(*args):
#     """
#     a lot of numbers adding
#     :param args:
#     :return:
#     """
#     sums = 0
#     for i in args:
#         sums = sums + i
#     print("结果为：{}".format(sums))
#
#
# one_str = input("请输入数字，用逗号分隔：")
# one_list = one_str.split(",")
# kong_list = []
# for t in one_list:
#     kong_list.append(int(t))
# # one_pop = (10,19)
#
#
# # sum_num(*one_pop)
# sum_num(*kong_list)


# 函数的返回值
# 定义：1.一个函数执行结束后告诉调用者一个结果2.返回值是函数完成工作后，最后给调用者的一个结果3.使用return关键字可以返回结果4.函数调用一方，可以使用变量来接收函数的返回结果
# （return表示返回，后续代码都不会被执行）
# 1.如果函数没有return，默认返回None2.如果函数return，返回的数目为1，则返回某个对象3.如果函数return，返回多个值，且以逗号分开，则返回tuple元组
# return的值可以别的地方用，赋值也可以，判断也可以，打印就只能打印


def twonums_multi(first_num,second_num):
    """
    two number multiple
    :param first_num:
    :param second_num:
    :return:
    """
    return first_num, second_num, first_num * second_num   # 如果函数没有return，默认返回None,如果函数return，返回多个值，且以逗号分开，则返回tuple元组(10,20,200)


one_num = 10
two_num = 20
result = twonums_multi(one_num, two_num)
pass


# 函数的嵌套调用
# 定义一个外层函数


def outer():
    """
    外层函数
    :return:
    """
    print("*" * 50)
    print("这是外层函数")


# 函数定义的时候是不会执行的
# 定义一个内层函数


def inner():
    """
    内层函数
    :return:
    """
    print("-" * 50)
    print("这是内层函数")

    outer()   # 内层函数中调用外层函数，执行完外层函数后会回到调用处继续往下执行！


inner()   # 执行内层函数，函数一定要先定义再调用


# 局部变量和全局变量
# 引出概念：1.调用函数时会创建了一个新的命名空间，供函数中的代码块使用2.在函数内部通过赋值语句定义的变量是在这个内部作用域（局部命名空间）中执行的，不影响外部（全局）作用域内同名的变量
# 局部变量：在内部作用域（局部命名空间）中定义的变量
# 全局变量：在外部作用域（全局命名空间）中定义的变量

# 案例


def manual_fn():
    """
    define function manually
    :return:
    """
    lemon = 1   # 这里的lemon相当于一个局部变量，只作用于这个函数内部，如果外部想用这个局部变量的话就使用return
    return lemon
    print(111111)   # 在函数内return后面的代码都不会执行


lemon =10   # 所有在函数外部定义的变量是全局变量
manual_fn()
print(lemon)


# 案例二
lemon_1 = 50


def manual_fn2(lemon_1):   # 局部变量的命名和全局变量的命名可以重复不报错，但不建议这样做会有波浪线
    """
    define function2 manually
    :return:
    """
    print(lemon_1)
    return lemon_1


print("调用前:{}".format(lemon_1))
# manual_fn2(100)
lemon_1 = manual_fn2(100)
print("调用后:{}".format(lemon_1))


# 案例三
lemon_2 = 30


def manual_fn3():
    """
    define function3 manually
    :return:
    """
    print(lemon_2)   # 函数内部不赋值
    # lemon_2 = 11   # 这里如果先引用再定义局部变量就会报错


print("调用前:{}".format(lemon_2))
manual_fn3()   # 调用的时候先在函数（局部变量）中查看有没有定义变量，然后再到全局中查找
print("调用后:{}".format(lemon_2))


# 案例四
lemon_3 = 60


def manual_fn4():
    """
    define function4 manually
    :return:
    """
    global lemon_3   # 如果一定要在函数内部的局部变量中更改为全局变量 需要使用global（如果更改为全局变量 所有含有全局变量的程序都会更改 尽量不要在函数体内部更改）
    lemon_3 = 65   # 这里定义的话是局部变量 无法更改为全局变量
    print(lemon_3)


print("调用前:{}".format(lemon_3))
manual_fn4()
print("调用后:{}".format(lemon_3))


# 常用内置函数——range
# 定义：1.生成整数序列2.语法格式：range(stop)/range(start,stop[,step])
# 1.从start开始如果不填写，默认为0 2.到stop结束，不包括stop，只能取到stop-1，例如range(5)等价于range(0,5)  range(0,5)是[0,1,2,3,4]没有5 3.step步长默认为1,例如range(0，5)等价于range(0,5，1)



# 作业
# 1.break和continue的区别
# break是当不符合条件时立刻跳出整个循环，continue是不符合条件时，跳出当前循环
# 2.while和for循环的异同点
# while和for都可以用作循环，重复执行代码，while循环次数不确定，能用for就不用while for支持遍历，效率更高
# 3.函数有哪些特性
# 能把代码整成代码块，有封装和解封装的过程，让程序小 模块化
# 4.写出将列表反转的所有方法：将列表反转为[45,9,85,42,20,13]
a_list = [13,20,42,85,9,45]
len_a_list = len(a_list)
# a_list.reverse
a_list_1 = list(reversed(a_list))   # 这种方法可以反转任意序列类型
# a_list_1 = a_list[::-1]
print(a_list_1)
# a_list_1 = []
# for i in range(len_a_list - 1,-1,-1):
#     a_list_1.append(a_list[i])
#     print(a_list_1)
# 5.取出列表的最大值
# print(max(a_list))
max_num = a_list[0]
min_num = a_list[0]
for num in a_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num =num
print(max_num,min_num)
# 6.编写程序，用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，打印输出“周末”，如果输入0，退出循环，输入其他内容提示"输入有误，请重新输入！提示：用if和while
# while True:
#     today = int(input("请输入1-7任意数字："))
#     if today == 6 or today == 7:
#         print("今天是周末")
#     elif today == 1 or today == 2 or today == 3 or today == 4 or today == 5:
#         print("今天是工作日")
#     elif today == 0:
#         break
#     else:
#         print("您输入的数字{}不在0-7之间".format(today))

# 7.编写程序，输入一个人的身高和体重，根据BMI公式（体重除以身高的平方）计算它的BMI指数
# 一个65公斤的人，身高是1.62m，则BMI为：65 / 1.62 ** 2 = 24.8
# 低于18.5：过轻，18.5-25：正常，25-28：过重，28-32：肥胖，高于32：严重肥胖


def BMI(height,weight):
    """
    design by BMI
    :param height:
    :param weight:
    :return:
    """
    bmi_num = weight / height ** 2
    if bmi_num < 18.5:
        print("您的BMI指数为{:.1f},过轻".format(bmi_num))
    elif 18.5 <= bmi_num < 25:
        print("您的BMI指数为{:.1f},正常".format(bmi_num))
    elif 25 <= bmi_num < 28:
        print("您的BMI指数为{:.1f},过重".format(bmi_num))
    elif 28 <= bmi_num < 32:
        print("您的BMI指数为{:.1f},肥胖".format(bmi_num))
    elif  bmi_num >= 32:
        print("您的BMI指数为{:.1f},严重肥胖".format(bmi_num))


BMI(1.62,65)


# 8.编写程序，从键盘输入用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则则提示用户用户名或密码错误
# a.定义一个函数，接受用户名输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best


def verify_username_password():
    """
    Verify user name and password
    :param username:
    :param password:
    :return:
    """
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "lemon" and password == "best":
        print("登录系统成功")
    else:
        print("用户名或密码错误,请重新输入")


verify_username_password()
