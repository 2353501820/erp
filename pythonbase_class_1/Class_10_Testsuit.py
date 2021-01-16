# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_10_Testsuit.py
# author : gaobo
# time : 2020/10/29 0029 17:30
---------------------------------------------------
"""
# def mul(a,b):   # 在函数下面三个双引号只能写备注和三个大于号加空格这样判断
# 	"""
# 	>>> mul(10,2)
# 	21
# 	>>> mul("y",2)
# 	'yy'
# 	"""
# 	return a * b

# 测试两个数相称
# doctest缺点：函数场景非常多的时候，1.不直观2.非常难以统计

# 导入系统模块
import unittest
import inspect

# 导入自定义模块
from pythonbase_class_1.Class_9_class_object import MathOperation


class TestMulti(unittest.TestCase):  # unittest规则：每一条用例，使用实例方法来测试，并且实例方法吗要以test_开头
	"""
	测试两数相乘
	"""

	def test_negative_multi(self):
		"""
		1.两个负数相乘
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		# 		获取两个负数相乘的结果
		real_result = MathOperation(-5, -9).multiply()  # 类+() 是对象 用对象调用类中的实例multiply()
		# 		验证实际结果与预期是否一致
		except_result = 4
		# 第一种方法使用条件判断不能实现功能
		# if real_result == except_result:
		# 	print("pass")
		# else:
		# 	print("fail")
		try:
			self.assertEqual(except_result, real_result, msg="测试两个负数相乘失败")
		except AssertionError as e:
			print("这里需要使用日志器来记录日志")
			print("具体异常为：{}".format(e))
			# raise关键字是将某个异常主动抛出
			raise e

	def test_two_zero_multi(self):
		"""
		2.两个零相乘
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(0, 0).multiply()
		except_result = 0
		try:
			self.assertEqual(except_result, real_result, msg="测试两个0相乘失败")
		except AssertionError as e:
			print("这里需要使用日志器来记录日志")
			print("具体异常为：{}".format(e))
			raise e

	def test_two_pos_multi(self):
		"""
		3.两个正数相乘
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(3, 4).multiply()
		except_result = 0
		try:
			self.assertEqual(except_result, real_result, msg="两个正数相乘失败")
		except AssertionError as e:
			print("这里需要使用日志器来记录日志")
			print("具体异常为：{}".format(e))
			raise e

	def test_neg_pos_multi(self):
		"""
		4.一个正数和一个负数相乘
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(-3, 4).multiply()
		except_result = 0
		try:
			self.assertEqual(except_result, real_result, msg="一个正数和一个负数相乘失败")
		except AssertionError as e:
			print("这里需要使用日志器来记录日志")
			print("具体异常为：{}".format(e))
			raise e


if __name__ == '__main__':
	unittest.main()


# 在一个测试类中，用例执行的顺序是实例方法名的ASCII码数值从小到大执行

# 处理测试不通过抛出的异常信息，将异常信息记录到日志中


# 作业
# 一、必做题
# 1.什么是自动化测试?
# 参考答案：写一段程序去测试另一段程序是否正常的过程
# 2.自动化测试的流程?
# 参考答案：需求分析编写测试用例执行测试用例总结报告
# 3.doctest如何使用?
# 参考答案：在注释中对函数、类进行测试，运行时需要加-m doctest参数来运行
# 4.单元测试的作用?
# 参考答案：
# 对代码中的函数、类模块进行测试
# 辅助进行接口测试，将预期结果与实际结果进行对比
# 5.unittest框架中，如何测试多条用例?用例执行顺序?
# 参考答案：
# 如何测试多条用例?
# 定义一个继承unittest的测试类， 为每个测试用例定义一个以test开头的实例方法
# 用例执行顺序?
# 以test开头的实例方法名称的ASCII码数值，从小到大的顺序来执行
# 6.编写如下单元测试使用unittest框架来测试两数相减功能，编写用例，执行用例。
# 参考答案：
# 参见相乘
# 二、选作题
# 7.编写如下单元测试
# a.使用unittest框架来测试两数相除功能，编写用例，执行用例。
# b.使用文件来记录执行用例的结果
# 参考答案：
# import unittest
# import inspect
# from pythonbase_class_1.Class_9_class_object import MathOperation
class TestDivide(unittest.TestCase):
	"""
	测试除法运算
	"""

	def test_two_pos_divide(self):
		# 定义一个文件路径
		file_name = "record_run_result.txt"
		print("打开【{}】文件".format(file_name))
		file = open(file_name, mode="a", encoding="utf-8")  # 以追加的模式打开一个文件
		file.write("{:=^40s}\n".format("开始执行用例"))  # 将"开始执行用例"写入到文件中

		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(10, 2).division()
		except_result = 5
		msg = "两个正数相除失败"
		try:
			self.assertEqual(except_result, real_result, msg=msg)
		except AssertionError as e:
			print("具体异常为：{}".format(e))
			file.write("{},执行结果为：{}\n具体异常为：{}".format(msg, "Fail", e))
			raise e
		else:
			file.write("{},执行结果为：{}".format(msg, "Pass"))
		finally:
			# 用例执行结束关闭文件
			print("关闭【{}】文件".format(file_name))
			file.write("{:=^40s}\n".format("用例执行结束"))
			file.close()

	def test_two_neg_divide(self):
		# 定义一个文件路径
		file_name = "record_run_result.txt"
		print("打开【{}】文件".format(file_name))
		file = open(file_name, mode="a", encoding="utf-8")  # 以追加的模式打开一个文件
		file.write("{:=^40s}\n".format("开始执行用例"))  # 将"开始执行用例"写入到文件中

		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(-10, -2).division()
		except_result = 5
		msg = "两个负数相除失败"
		try:
			self.assertEqual(except_result, real_result, msg=msg)
		except AssertionError as e:
			print("具体异常为：{}".format(e))
			file.write("{},执行结果为：{}\n具体异常为：{}".format(msg, "Fail", e))
			raise e
		else:
			file.write("{},执行结果为：{}".format(msg, "Pass"))
		finally:
			# 用例执行结束关闭文件
			print("关闭【{}】文件".format(file_name))
			file.write("{:=^40s}\n".format("用例执行结束"))
			file.close()


if __name__ == '__main__':
	unittest.main()
