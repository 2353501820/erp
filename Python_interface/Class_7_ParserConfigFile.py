# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_7_ParserConfigFile.py
# author : liushen
# time : 2020/11/27 0027 21:20
---------------------------------------------------
"""
# 有很多变量写死了，如果Excel的文件名，记录日志的文件名
# 可以将这些变量写到一个配置文件中，如果项目需求改变，只需修改配置文件即可

# 一般配置文件的拓展名为：.ini .conf等
# 配置文件一般是
# section 片段/区域[区域名]
# 区域名区分大小写，不必遵守python中的标识符命名规则

# option 相当于字典中的key
# 选项名时不区分大小写，默认小写存储，不必遵守python中的标识符命名规则
# =号右边value相当于字典中的value

# 给选项赋值默认使用等号"="当然也可以使用英文中的冒号":"等号或者冒号两侧的空格可有可无
# 给文件注释可以使用井号或分号"#"";"
from configparser import ConfigParser

# 1.创建配置解析器对象
config = ConfigParser()

# 2.执行读取的配置文件名
read_file = config.read("testcase.conf",encoding="utf-8")

# 3.读取数据
# config 相当于嵌套字典的字典
# config.sections()   # 返回区域名（字符串）组成的一个列表

# 方法一：获取某个值
# config["file path"]["test_path"]
# 方法二：通过get获取
# config.get("file path","test_path")   # 跟字典中的get有区别，字典中的get直接给一个key就能获取值
# 方法三：
file_path = config["file path"]
for key,value in file_path.items():
	print(key,value)
# 从配置文件中获取的所有值都是字符串类型
# 可以使用int来转换，也可以使用eval函数
# 配置文件中，提供了一个getint()
print(config.getint("excel","actual_col"))
# getboolean()
# config.getboolean("excel","actual_col")
# 1、yes、on、true getboolean都会识别为True
# 0、no、off、false getboolean都会识别为False

# getfloat() 将数字类型的字符串转换为float类型
# 如果是其他类型，比如列表、元组、字典，只能够使用eval函数
print(eval(config.get("excel","three_res")))

# 配置文件中有一个默认的区域(DEFAULT)，这个区域中保存的是所有区域中公共的数据
# 如果不显示定义DEFAULT，那么就是一个空字典

# config类似这种结构
# config = {
# 	"file path":{"test_path":"test.xlsx","log_path":"record_run_results.txt"}
# 	"msg":{"success_result":"Pass","Fail_result":"Fail"},
# 	"excel":{"actual_col":"6","result_col":"7"}
# }


# 写配置文件
# 1.创建配置解析器对象
config = ConfigParser()   # 没有赋值的时候相当于一个空字典

# 2.将需要写入配置文件中的数据组合成嵌套字典的字典
datas = {
	"file path":{
		"test_path":"test.xlsx",
		"log_path":"record_run_results.txt"
	},
	"msg":{
		"success_result":"Pass",
		"fail_result":"Fail"
	},
	"excel":{
		"actual_col":"6",
		"result_col":"7"}
}
for key in datas:
	config[key] = datas[key]

# 3.保存到文件
with open("write_config.ini","w") as file:
	config.write(file)



pass