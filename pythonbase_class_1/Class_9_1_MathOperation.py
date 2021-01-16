# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_9_1_MathOperation.py
# author : liushen
# time : 2020/11/23 0023 21:07
---------------------------------------------------
"""


class MathOperation:
	"""
	数学计算
	"""
	def __init__(self,no_one,no_two):
		self.no_one,self.no_two = no_one,no_two

	def add(self):
		return self.no_one + self.no_two

	def minus(self):
		return self.no_one - self.no_two

	def multiply(self):
		return self.no_one * self.no_two

	def division(self):
		try:
			return round(self.no_one / self.no_two,2)   # 相乘后四舍五入
		except ZeroDivisionError:
			# print("除0错误")
			return "∞"