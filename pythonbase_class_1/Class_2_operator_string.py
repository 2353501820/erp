# -*-coding: utf-8 -*-
# @time     :2020-3-18 15:41
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :class_2_operator_string.py
# @software :PyCharm
# 运算符
print(5 / 2)  # 一个/ 除
print(5 // 2)  # 两个// 取整
print(5 % 2)  # % 取余
print(int(2.5))  # int可以把小数转化为整数
print(float(2))  # int可以把整数转化为小数

# 比较运算符
# true false
a = 5
b = 8
print(a == b)
print(a >= b)
print(a <= b)
print(5 <= 8.8)  # 整数和浮点数可以直接比较
a = "小小"  # 整数和字符串不可以直接比较
b = "小小马"
print(a == b)  # 字符串可以和字符串直接比较，因为系统会将字符串转化为ascii码


# 查看ascii码
print(ord("a"))
print(ord("b"))

# ascii码转化为字符串
print(chr(97))
print(chr(98))


# 逻辑运算符
"""
and 一假必假，两真才真
or 一假为真，两假才假
not 以假乱真，取反
"""
print((1 == 1) and (1 > 2))
print((1 == 1) and (1 < 2))
print((1 == 1) or (1 > 2))
print((1 != 1) or (1 > 2))
print(1 == 1)
print(not(1 == 1))


# 赋值运算符
first_num = 10
second_num = 20
print(first_num + second_num)  # 变量是最简单的赋值

second_num += 20  # 这个语句相当于second_num = second_num + 20
print(second_num)
"""
同理
second_num -= 20  这个语句相当于second_num = second_num - 20
second_num *= 20  这个语句相当于second_num = second_num * 20
second_num /= 20  这个语句相当于second_num = second_num / 20
second_num //= 20  这个语句相当于second_num = second_num // 20 取整
second_num %= 20  这个语句相当于second_num = second_num % 20 取余
second_num **= 20  这个语句相当于second_num = second_num ** 20 幂赋值

运算符的优先级(从上到下)
**幂运算
* / % //乘、除、取余、取整
+ - 加、减
< <= > >=比较运算符
== 1= 等于运算符
= += -= *= /= %= **= //= 赋值运算符
not or and 逻辑运算符
总结：1.先乘除后加减 2.同级运算，运算符是从左至右计算的 3.可以使用（）调整计算优先级
"""
# 从年份判断生肖
shengxiao = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
birthday_year = 1994
suoying = birthday_year % 12
print(suoying)
print(shengxiao[suoying])  # 字符串从左至右是0 1 2 3....索引是2，字符串取的是第三位。通过[]符号能取出字符串对应的索引值

# 字符串取值正序0 1 2 3 .....
# 字符串取值倒序-1 -2 -3 .....
# 如python 正序，最高值-1 能取到5 倒序 最低值 能取到-6（算个数）
liru = "python"
print(liru[5])  # 取n
print(liru[-6])  # 取p



# 字符串的切片
# 格式[开始索引:结束索引:步长]，结束索引取不到需-1取前一位
print(liru[0:4])  # 取pyth
print(liru[:4])  #开始索引如果为0，可以为空
print(liru[-6:-1])
print(liru[:6:2])  # 默认步长为1，隔断取pto，步长为2，每隔2个取一个
print(liru[::2])# 开始索引和结束索引是指向从头至末尾 可以都为空
print(liru.islower())  # 内置方法：判断这个字符串是否是小写
print(liru.startswith('p'))  # 判断这个字符串是否是p开头
print(liru.endswith('se'))  # 判断这个字符串是否是se结尾
# index 和 find类似，find是检查字符串从开头到结尾有没有包含其指定字符，是返回开始索引值，否则返回-1
# index如果没有包含会报错
# 替换 字符串.replace(old_str,new_str,num=字符串.count(old))   把字符串中的ord_str替换成new_str，如果num指定，则替换不超过num次
print(liru.replace('p','php'))
# 去除空白符 .strip截掉左右两边的空白字符 lstrip截左 rstrip截右
# 拆分和连接 .split(str"",num) 以str为分隔符拆分string，如果num有指定值，则仅分割num + 1 个字符串  str默认包含'\r','\t','\n'和空格
jast = '/lsi/ioei/een'
print(jast.split("/"))
# 连接join
jast = ['lsk','jdkh']
print("/".join(jast))  # 列表没有join方法，只有字符串才有
# 练习input函数
# wo = input("请输入我的值：")
# ni = input("请输入你的值：")
# wo = int(wo)
# ni = int(ni)
# print("我和你=",wo + ni )


# 格式化输出
# 定义：可以使用print函数将信息输出到控制台，如果希望输出文字的同时一起输出数据，就需要使用格式化操作符 % 或者format方法

# 占坑符 %
# 语法格式：print("格式化字符串" % 变量)    print("格式化字符串" % (变量1,变量2，....))
print("我的名字是%s"% "mary")
print("my age is % d" % 18 )
print("我喜欢 %s %s %s 这些都是我喜欢的科目" % ("english", "math","music"))
print("这三门成绩分别是 %s%% %s %.1f" % (75,95,90.5))  # 占坑符后面加两个%代表百分之多少，占坑符后面加点数字f，可以表示浮点数.2f代表两位小数

# format方法
# 把含有{}的字符串当成一个模板，通过传入参数进行格式化
# **不指定序号，会自动按顺序匹配{}{}
# **指定序号去匹配{0}{1}
# **指定同一个序号去匹配{1}{1}

# 类型
# {:s}或者{}        与%s一样输出为字符串
# {:d}、{:05d}      与%d一样输出为10进制整数
# {:f}、{:.2f}      与%f一样输出为浮点数

name_1 = "popo"
print("我叫{}".format(name_1))
age_1 = 35
print("年龄是{}".format(age_1))
hight_1 = 183.2
print("身高是{:.2f}cm".format(hight_1))
print("我的名字叫{}，我的年龄是{:d}岁，我的身高是{:.2f}cm!".format("popo",2,3))
print("我的名字叫{0}，我的年龄是{2}岁，我的身高是{2}cm!".format("popo",2,3))  # 指定序号去匹配

# 作业：1.Python中的逻辑运算符有哪些？他们有哪些区别
# and or not
# 2.如下比较运算符分别返回什么？
a = 15
b = 9
print(a == b)
print(a != b)
print(a > b)
print((a - 5) < b)
print(a >= b ** 2)
print((a + 13 - 10 * 2) <= (b // 2 * 5 + 35 % 4))
# 3.定义字符串 I'm Lemon , I Love Python automated testing! 因为里面有单引号，所以定义字符串需要用双引号
print("I'm Lemon , I Love Python automated testing!")
# 4.把website = 'http://www.python.org'中的python字符串取出来
website = 'http://www.python.org'
print(website[11:17])
print(website.split(".")[1])
# 5.将字符串后面前后的空格除去，把PHP替换为Pyton
best_language = ' PHP is best programming language in the world! '
# best_language_1 = best_language.strip()
# print(best_language_1.replace("PHP","Python"))
print(best_language.strip().replace("PHP","Python"))
# 6.演练字符串操作
"""
截取2~6位置的字符串
截取2·末尾的字符串
截取从开始·6位置的字符串
截取完整的字符串
从开始位置，每隔一个字符截取字符串
从索引3开始，每隔2取一个
截取从2·末尾-1的字符串
截取字符串末尾两个字符
字符串逆序（拓展）
"""
my_hobby = "Never stop learning!"
print(my_hobby[1:6])
print(my_hobby[1:])
print(my_hobby[:6])
print(my_hobby[:])
print(my_hobby[::1])
print(my_hobby[3::2])
print(my_hobby[1:-1])
print(my_hobby[-2:])
print(my_hobby[::-1])
#  7.去生鲜超市买橘子，收银员输入橘子的价格，单元：元/斤，收银员输入购买橘子的重量，单位：/斤，计算并且输出付款金额
price = input("输入购入橘子的价格:")
weight = input("输入购买橘子的重量:")
price =float(price)
weight = float(weight)
money = price * weight
print("橘子每斤{:.1f}元,您购买了{:.1f}斤,您一共花费{:.2f}元".format(price,weight,money))


