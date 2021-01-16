# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_11_Unittest_start_end_handle.py
# author : gaobo
# time : 2020/11/3 0003 22:14
---------------------------------------------------
"""
# 1、只要单元测试， 实例方法中有抛出异常， unittest框架都会识别为执行异常
# 2、self.assert Equal(期望值， 实际值， msg="执行失败之后的自定义提示信息)
# 3、如果频繁的打开、关闭一个文件， 将会有很大的资源消耗(cpu、内存) ， 是非常差的一种处理方式
# 4、

# 在每一条用例执行之前打开文件
# 在每一条用例执行之后关闭文件
# 解决多个测试类，记录执行日志的问题，会使用 def setUpModel 和 def tearDownModel
import unittest
import inspect

# 导入自定义模块
from pythonbase_class_1.Class_9_class_object import MathOperation


def setUpModule():
	"""
	所有测试类在调用之前，会执行一次
	函数名setUpModule是固定写法，会被我们的unittest框架自动识别
	:return:
	"""
	global file_name   # 这是个函数，不能用类(cls)，所以需要定义一个全局变量
	global file
	print("\n{:=^40s}\n".format("用例开始执行"))
	file_name = "record_run_result.txt"
	print("打开【{}】文件".format(file_name))
	file = open(file_name, mode="a", encoding="utf-8")
	file.write("{:=^40s}\n".format("用例开始执行"))


def tearDownModule():
	"""
	所有测试类被调用结束后，会执行一次
	函数名tearDownModule是固定写法，会被我们的unittest框架自动识别
	:return:
	"""
	print("{:=^40s}\n".format("用例执行结束"))
	file.write("{:=^40s}".format("用例执行结束"))
	print("关闭【{}】文件".format(file_name))
	file.close()


class TestDivide(unittest.TestCase):
	"""
	测试两数相乘
	"""
	# @classmethod
	# def setUpClass(cls):
	# 	"""
	# 	重写父类的类方法，在实例方法被执行之前会被调用一次
	# 	在所有用例执行之前会被执行
	# 	:return:
	# 	"""
	# 	print("\n{:=^40s}".format("用例开始执行"))
	# 	cls.file_name = "record_run_result.txt"
	# 	print("打开【{}】文件".format(cls.file_name))
	# 	cls.file = open(self.file_name, mode="a", encoding="utf-8")
	# 	cls.file.write("\n{:=^40s}\n".format("用例开始执行"))

	# def setUp(self):
	# 	"""
	# 	重写父类的方法，setUp是unittest.TestCase中的方法
	# 	在每一个用例执行之前，会被调用
	# 	:return:
	# 	"""
	# 	print("\n{:=^40s}".format("用例开始执行"))
	# 	self.file_name = "record_run_result.txt"
	# 	print("打开【{}】文件".format(self.file_name))
	# 	self.file = open(self.file_name,mode="a",encoding="utf-8")
	# 	self.file.write("\n{:=^40s}\n".format("用例开始执行"))

	def test_two_pos_divide(self):
		"""
		1.两个正数相除
		:return:
		"""
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
			file.write("{},执行结果为：{}\n".format(msg, "Pass"))

	@unittest.skip("test_two_neg_divide")   # 当有的用例不需要执行的时候用unittest.skip，这条用例默认跳过不执行
	def test_two_neg_divide(self):
		"""
		2.两个负数相除
		:return:
		"""
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
			file.write("{},执行结果为：{}\n".format(msg, "Pass"))


	# def tearDown(self):
	# 	"""
	# 	重写父类的方法，setUp是unittest.TestCase中的方法
	# 	在每一个用例执行之后，会被调用
	# 	:return:
	# 	"""
	# 	print("{:=^40s}".format("用例执行结束"))
	# 	self.file.write("{:=^40s}".format("用例执行结束"))
	# 	print("关闭【{}】文件".format(self.file_name))
	# 	self.file.close()

	# @classmethod
	# def tearDownClass(cls):
	# 	"""
	# 	重写父类的类方法
	# 	所有用例执行之后，会被调用一次
	# 	:return:
	# 	"""
	# 	print("{:=^40s}".format("用例执行结束"))
	# 	cls.file.write("{:=^40s}".format("用例执行结束"))
	# 	print("关闭【{}】文件".format(cls.file_name))
	# 	cls.file.close()


class TestMulti(unittest.TestCase):
	"""
	测试两数相乘
	"""
	# @classmethod
	# def setUpClass(cls):
	# 	"""
	# 	重写父类的类方法，在实例方法被执行之前会被调用一次
	# 	在所有用例执行之前会被执行
	# 	:return:
	# 	"""
	# 	print("\n{:=^40s}".format("用例开始执行"))
	# 	cls.file_name = "record_run_result.txt"
	# 	print("打开【{}】文件".format(cls.file_name))
	# 	cls.file = open(self.file_name, mode="a", encoding="utf-8")
	# 	cls.file.write("\n{:=^40s}\n".format("用例开始执行"))

	# def setUp(self):
	# 	"""
	# 	重写父类的方法，setUp是unittest.TestCase中的方法
	# 	在每一个用例执行之前，会被调用
	# 	:return:
	# 	"""
	# 	print("\n{:=^40s}".format("用例开始执行"))
	# 	self.file_name = "record_run_result.txt"
	# 	print("打开【{}】文件".format(self.file_name))
	# 	self.file = open(self.file_name,mode="a",encoding="utf-8")
	# 	self.file.write("\n{:=^40s}\n".format("用例开始执行"))

	def test_two_pos_multi(self):
		"""
		1.两个正数相除
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(10, 2).multiply()
		except_result = 20
		msg = "两个正数相乘失败"
		try:
			self.assertEqual(except_result, real_result, msg=msg)
		except AssertionError as e:
			print("具体异常为：{}".format(e))
			file.write("{},执行结果为：{}\n具体异常为：{}".format(msg, "Fail", e))
			raise e
		else:
			file.write("{},执行结果为：{}\n".format(msg, "Pass"))

	def test_two_neg_multi(self):
		"""
		2.两个负数相除
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		real_result = MathOperation(-10, -2).multiply()
		except_result = 20
		msg = "两个负数相乘失败"
		try:
			self.assertEqual(except_result, real_result, msg=msg)
		except AssertionError as e:
			print("具体异常为：{}".format(e))
			file.write("{},执行结果为：{}\n具体异常为：{}".format(msg, "Fail", e))
			raise e
		else:
			file.write("{},执行结果为：{}\n".format(msg, "Pass"))


	# def tearDown(self):
	# 	"""
	# 	重写父类的方法，setUp是unittest.TestCase中的方法
	# 	在每一个用例执行之后，会被调用
	# 	:return:
	# 	"""
	# 	print("{:=^40s}".format("用例执行结束"))
	# 	self.file.write("{:=^40s}".format("用例执行结束"))
	# 	print("关闭【{}】文件".format(self.file_name))
	# 	self.file.close()

	# @classmethod
	# def tearDownClass(cls):
	# 	"""
	# 	重写父类的类方法
	# 	所有用例执行之后，会被调用一次
	# 	:return:
	# 	"""
	# 	print("{:=^40s}".format("用例执行结束"))
	# 	cls.file.write("{:=^40s}".format("用例执行结束"))
	# 	print("关闭【{}】文件".format(cls.file_name))
	# 	cls.file.close()


if __name__ == '__main__':
	unittest.main()
