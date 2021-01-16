# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_6_excel_encapsulation_unittest_rewrite.py
# author : liushen
# time : 2020/11/27 0027 19:21
---------------------------------------------------
"""
# 将Excel封装之后再次重构单元测试
import unittest
from ddt import ddt,data
import inspect
from pythonbase_class_1.Class_9_1_MathOperation import MathOperation
from Python_interface.Class_5_excel_encapsulation import HandleExcel
from Python_interface.Class_8_ParserConfigFile__call__ import Handleconfig

@ddt
class TestMulti(unittest.TestCase):  # unittest规则：每一条用例，使用实例方法来测试，并且实例方法吗要以test_开头
	"""
	测试两数相乘
	"""
	config = Handleconfig()
	# test_obj = HandleExcel("test.xlsx")
	test_obj = HandleExcel(config("file path","test_path"))
	tests = test_obj.get_tests()

	@data(*tests)
	def test_negative_multi(self,data_namedtuple):
		"""
		1.两个负数相乘
		:return:
		"""
		print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		# 		获取两个负数相乘的结果
		case_id = data_namedtuple.case_id
		msg = data_namedtuple.title
		l_data = data_namedtuple.l_data
		r_data = data_namedtuple.r_data
		except_result = data_namedtuple.expected
		real_result = MathOperation(l_data, r_data).multiply()  # 类+() 是对象 用对象调用类中的实例multiply()
		# except_result = 4   # 不需要手动添加期待值
		# 第一种方法使用条件判断不能实现功能
		# if real_result == except_result:
		# 	print("pass")
		# else:
		# 	print("fail")
		try:
			self.assertEqual(except_result, real_result, msg="测试{}失败".format(msg))
		except AssertionError as e:
			print("这里需要使用日志器来记录日志")
			print("具体异常为：{}".format(e))
			# ws.cell(row=case_id+1,column=7,value="Fail")
			# self.test_obj.write_result(row=case_id+1,actual=real_result,result="Fail")
			self.test_obj.write_result(row=case_id+1,actual=real_result,result=self.config("msg","fail_result"))
			self.assertRaises(TypeError)   # assertRaises可以直接断言异常
			# raise关键字是将某个异常主动抛出
			raise e
		else:
			# ws.cell(row=case_id+1,column=7,value="Pass")
			# self.test_obj.write_result(row=case_id+1,actual=real_result,result="Pass")
			self.test_obj.write_result(row=case_id+1,actual=real_result,result=TestMulti.config("msg","success_result"))

if __name__ == '__main__':
	unittest.main()

