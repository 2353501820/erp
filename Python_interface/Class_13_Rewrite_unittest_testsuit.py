# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_13_Rewrite_unittest_testsuit.py.py
# author : liushen
# time : 2020/12/15 0015 19:56
---------------------------------------------------
"""
# 方法三：通过模块来批量加载测试用例
# 创建一个加载器对象
from datetime import datetime
import unittest
# one_loader = unittest.TestLoader()

from Python_interface import HTMLTestRunnerNew
# from pythonbase_class_1 import Class_11_Unittest_start_end_handle as module1
from Python_interface import Class_12_Rewrite_excel_unittest_encapsulation as module1
# from pythonbase_class_1 import Class_10_Testsuit as module2
from Python_interface import Class_14_excel_add_unittest_Html as module2   # 用测试套件执行Excel中sheet名为add的加法sheet
# one_suite.addTest(one_loader.loadTestsFromModule(module1))
# one_suite.addTest(one_loader.loadTestsFromModule(module2))

from Python_interface.Class_8_ParserConfigFile__call__ import do_config

# 方法四：方法三的补充
# 1.创建测试加载器，加载所有的测试模块
one_loader = unittest.TestLoader()
test_moduel_tuple = (one_loader.loadTestsFromModule(module1),one_loader.loadTestsFromModule(module2))   # ,one_loader.loadTestsFromModule(module2)  模块2暂时不加

# 2.创建测试套件
# 创建测试套件时，将所有的测试模块所构成的元组传给TestSuite类
one_suite = unittest.TestSuite(tests=test_moduel_tuple)   # 这里通过类名+（）来创建对象会调用__init__.py方法，所以这里就不需要addTest

# 3.执行用例
# 创建一个运行器对象
# one_runner = unittest.TextTestRunner()   # 因为是对象，所以一定要加(),类+() = 对象，用对象调用
# one_runner.run(one_suite)

# 执行的结果中，一个"点"代表成功执行一条用例，一个"F"代表执行一条用例失败

# 利用unittest框架提供的输出报告方式，将批量执行的测试用例结果信息存放到文件中
# 打开文件
# save_to_file = open("test_results.txt",mode="w",encoding="utf-8")
# # 将测试结果存放到文件中
# one_runner = unittest.TextTestRunner(stream=save_to_file,descriptions="测试结果集",verbosity=1)   # verbosity对应输出日志报告详细程度2最详细，0普通
# one_runner.run(one_suite)
# # 关闭文件
# save_to_file.close()

# # 打开关闭文件太麻烦的话可以用with as 上下文管理器，这样就不用担心文件是否关闭
# with open("test_results.txt",mode="w",encoding="utf-8") as save_to_file:
# 	one_runner = unittest.TextTestRunner(stream=save_to_file, descriptions="测试结果集", verbosity=1)
# 	one_runner.run(one_suite)


# 进一步美化输出日志报告，安装第三方包，file - settings - project interpreter - + - html-testRunner - install Package 或者用pip
# pip install html-testRunner

# # output输出生成指定名称的文件夹，会针对单独的测试类来生成HTML的报表，打开要放在html文件上右击选择Open in Browser 选择浏览器
# one_runner = HTMLTestRunner(output="reports",report_name='测试结果集',report_title="标题，html会乱码",combine_reports=True)
# one_runner.run(one_suite)

# 执行用例 test_results_202012151043.html 需要这种格式
report_html_name = do_config("file path","report_html_name")
report_html_name_full = report_html_name + "_" + datetime.strftime(datetime.now(),"%Y%m%d%H%M%S") + ".html"

with open(report_html_name_full,mode="wb") as save_to_file:
	one_runner = HTMLTestRunnerNew.HTMLTestRunner(stream=save_to_file, title="测试结果集", verbosity=1,description="测试两数相乘用例",tester="静宝")
	one_runner.run(one_suite)
