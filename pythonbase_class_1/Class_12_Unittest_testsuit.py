# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_12_Unittest_testsuit.py
# author : gaobo
# time : 2020/11/6 0006 18:02
---------------------------------------------------
"""
# 如果有多个模块，那么如何批量执行每一个模块中的用例？
# 测试套件

import unittest

# from pythonbase_class_1.Class_11_Unittest_start_end_handle import TestDivide,TestMulti


from HTMLTestRunner import HTMLTestRunner

# 1.创建一个测试套件
# one_suite = unittest.TestSuite()   # 实例化，创建一个测试套件对象

# 2.加载用例
# 方法一：通过测试对象来加载用例，将实例方法（一个用例）名作为测试类的参数，最麻烦的一种方式
# one_suite.addTest(TestMulti("test_two_pos_multi"))   # 测试单个用例 只能添加测试类的实例（对象）
# one_tuple = (TestMulti("test_two_pos_multi"),TestDivide("test_two_pos_divide"))
# one_suite.addTests(one_tuple)   # 将多个测试用例，同时加入到套件中

# 方法二：通过测试类来批量加载测试用例
# 创建一个加载器对象 实现跨模块来执行测试用例 当类特别多时，还是很麻烦
# one_loader = unittest.TestLoader()
# one_suite.addTest(one_loader.loadTestsFromTestCase(TestMulti))   # 通过加载器把乘法类加载在one_suit的套件中
# one_suite.addTest(one_loader.loadTestsFromTestCase(TestDivide))
# one_tuple = (one_loader.loadTestsFromTestCase(TestMulti),one_loader.loadTestsFromTestCase(TestDivide))
# one_suite.addTests(one_tuple)

# 方法三：通过模块来批量加载测试用例
# 创建一个加载器对象
# one_loader = unittest.TestLoader()
from pythonbase_class_1 import Class_11_Unittest_start_end_handle as module1
from pythonbase_class_1 import Class_10_Testsuit as module2
# one_suite.addTest(one_loader.loadTestsFromModule(module1))
# one_suite.addTest(one_loader.loadTestsFromModule(module2))

# 方法四：方法三的补充
# 1.创建测试加载器，加载所有的测试模块
one_loader = unittest.TestLoader()
test_moduel_tuple = (one_loader.loadTestsFromModule(module1),one_loader.loadTestsFromModule(module2))

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


# 进一步美化输出日志报告，安装第三方包，file -> settings -> project interpreter -> + -> html-testRunner -> install Package 或者用pip
# pip install html-testRunner

# output输出生成指定名称的文件夹，会针对单独的测试类来生成HTML的报表，打开要放在html文件上右击选择Open in Browser 选择浏览器
one_runner = HTMLTestRunner(output="reports",report_name='测试结果集',report_title="标题，html会乱码",combine_reports=True)
one_runner.run(one_suite)