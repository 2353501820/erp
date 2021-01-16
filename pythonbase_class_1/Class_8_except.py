# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_8_except.py
# author : liushen
# time : 2020/9/1 0001 21:08
---------------------------------------------------
"""

# python中的异常
# 概念：
# 1.程序在运行时，如果Python解释器遇到到一个错误，会停止程序的执行，并且提示一些错误信息，这就是异常
# 2.程序停止执行并且提示错误信息这个动作， 我们通常称之为：抛出(raise) 异常

# 捕获异常：
# 1.简单形式如果对某些代码的执行不能确定是否正确，可以增加try(尝试) 来捕获异常
# 语法格式：
# try：
# 不确定是否能正常执行的代码
# except：
# 出现错误的处理

# try尝试，下方编写不确定是否能够正常执行的代码
# except如果不是，下方编写尝试失败的代码
# 2.简单形式演练
# 不建议在不清楚逻辑的情况下捕获所有异常，有可能你隐藏了很严重的问题
# try:
# 	num = int(input("输入正整数"))
# except:
# 	print("输入错误")

# while True:
# 	try:
# 		num = int(input("输入正整数"))
# 		break
# 	except:
# 		print("输入错误")

# 3.异常类型捕获
# 在程序执行时，可能会遇到不同类型的异常，并且需要针对不同类型的异常，做出不同的响应语法如下：
# try:
# 	尝试执行的代码
# 	pass
# except 错误类型1:
#	针对错误类型1，对应的代码处理
#	pass
# except(错误类型2， 错误类型3):
# 	针对错误类型2和3.对应的代码处理
# 	pass
#except Exception as e:
# 	print("未知错误:{}".format(e))

# try:
# 	num = int(input("输入正整数"))
# 	result = 10 / num
# 	a_list = [10,20]
# 	b = a_list * a_list
# except ValueError:
# 	print("请输入正确整数")
# except ZeroDivisionError:
# 	print("除号不能为0")
# except Exception as e:   # 所有的错误（除了语法错误）都能被Exception接收
# 	print("未知错误:{}".format(e))
# else:   # else在程序没有出错的情况下会执行，else执行了 except则不会执行
# 	print("正常执行")
# finally:   # finally是程序无论有没有出错都会执行，例如：打开文件后一定需要关闭文件
# 	print("一定会被执行")


# 4.异常类型捕获演练

# 5.捕获未知错误
# 要预判到所有可能出现的错误，是有一定难度的
# 如果希望程序无论出现任何错误， 都不会因为Python解释器抛出异常而被终止， 可以再增加-except




# 作业
# 新需求：d.使用捕获异常的方式，来处理用户输入无效数据的情况

# def is_int_or_digit(num):
# 	"""
# 	判断输入的数字是否为正数
# 	:param num:
# 	:return:
# 	"""
# 	try:
# 		one_num = float(num)
# 		return True if one_num >= 0 else False
# 	except ValueError:
# 		return False
#
#
# def main():
# 	while True:
# 		# 输入橘子单价
# 		unit_price = input("请输入橘子的单价：")
# 		if not is_int_or_digit(unit_price):
# 			print("您输入的单价有误")
# 			continue
# 		break
#
#
# 	while True:
# 		orange_wight = input("请输入橘子的重量:")
# 		if not is_int_or_digit(orange_wight):
# 			print("您输入的重量{}有误".format(orange_wight))
# 			continue
# 		break
#
#
# 	# 	计算总价
# 	unit_price_fl = float(unit_price)
# 	orange_wight_fl = float(orange_wight)
# 	sum_price = unit_price_fl * orange_wight_fl
# 	print("您购买的橘子单价为{}，重量为{}，总价为{}".format(unit_price_fl,orange_wight_fl,sum_price))
#
#
# if __name__ == '__main__':
#     main()
# 5.编写如下程序
# 优化剪刀石头布优秀程序
# a.提示用户输入要出的拳――石头(1)/剪刀(2)/布(3)
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
# h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能(选做)


import random
import os


def menu_info():
	"""
	菜单显示信息
	:return:
	"""
	print()
	print("=" * 50)
	print("\t\t剪刀石头布终极对战")
	print()
	print("\t\t1.输入石头（1）/剪刀（2）/布（3）")
	print("\t\t2.输入（0）退出程序\n")
	print("=" * 50)


def check_input(num):
	"""
	判断用户输入的是否是0到3之间的正整数
	:param num:
	:return:True or False
	"""
	try:
		one_num = int(num)
		return True if one_num in range(4) else False
	except ValueError:
		return False


def user_vs_computer(user_player,computer_player):
	"""
	判断用户输赢
	:param user_player:用户猜拳数字
	:param computer_player:电脑猜拳数字
	:return:
	"""
	# 用户胜的情况：
	# 用户出石头（1），电脑出剪刀（2）
	# 用户出剪刀（2），电脑出布（3）
	# 用户出布（3），电脑出石头（1）
	user_win_tup = ((1,2),(2,3),(3,1))

	user = (user_player, computer_player)
	if user in user_win_tup:
		print("yeah,赢了")
		return "胜"
	elif user_player == computer_player:
		print("心有灵犀")
		return "和"
	else:
		print("很抱歉，再来一盘吧")
		return "败"


def user_input():
	"""
	校验用户输入
	:return:正整数
	"""
	while True:
		user_num = input("请输入0-3之间的数字：石头（1）/剪刀（2）/布（3）/退出（0）")
		if not check_input(user_num):
			print("您输入有误")
		else:
			break
	return int(user_num)


def file_handle(file_path,data=None,mode="a+",encoding="utf-8"):
	"""
	读写数据
	:param file_path:文件路径
	:param data:添加数据
	:param mode:文件打开模式
	:param encoding:文件编码
	:return:
	"""
	# 判断文件是否存在
	if not os.path.exists(file_path) or not os.path.isfile(file_path):
		print("文件路径有误")


	try:
		# 打开文件
		one_file = open(file_path,mode=mode,encoding=encoding)
		if data is not None:   # 如果内容不为空，则添加数据
			# 添加内容到文件
			datas_size = one_file.write(data)
			return datas_size
		else:
			# 读取内容
			one_file.seek(0)   # 将文件指针设置到起始位置
			datas_list = one_file.readlines()
			return datas_list
	except Exception as e:
		print("文件处理期间出现如下异常{}".format(e))
	finally:
		# 关闭文件
		one_file.close()


def main():
	result_file = "game_result.txt"
	win_count = 0   # 胜利次数
	fail_count = 0   # 失败次数
	peace_count = 0   # 平局次数
	game_count = 0   # 游戏总次数
	win_rate = 0   # 游戏胜算率

	# 1.显示游戏历史胜负情况
	print("游戏历史胜负情况如下：")
	handle_result = file_handle(result_file)
	if not handle_result:
		print("游戏记录为空")
	elif isinstance(handle_result,list):   # 如果返回的是读取的数据列表
		for key,value in enumerate(file_handle(result_file),start=1):
			print("第{}局:\t{}".format(key,value[:-1]))


	# 2.显示游戏界面
	menu_info()


	# 3.开始游戏
	while True:
		computer_num = random.randint(1,3)
		user_num = user_input()

		if user_num == 0:
			print("游戏退出，欢迎再来")
			break
		# 判断胜负
		result = user_vs_computer(user_num,computer_num)
		game_count += 1
		if result == "胜":
			win_count += 1
		elif result == "败":
			fail_count += 1
		else:
			peace_count += 1

	# 游戏结束，判断胜利情况
	try:
		win_rate = (win_count / game_count) * 100
	except ZeroDivisionError:
		print("除0异常")

	last_result = (win_count,fail_count,peace_count,game_count)
	print("用户胜负情况：\n{}胜{}负{}和，\n胜算率为{:.1f}%".format(*last_result))

	# 将用户胜负情况写入文件
	game_info = "{}胜、{}负、{}和，{:.1f}%胜算\n".format(*last_result)
	file_handle(result_file,game_info)


if __name__ == '__main__':
	main()