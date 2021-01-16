# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Json_Datahandle.py
# author : liushen
# time : 2020/12/23 0023 18:26
---------------------------------------------------
"""
# 一、定义
# 是一种数据格式
# 使用JavaScript对象表示法

# 二、特点
# 1.与XML格式数据的区别
# 两种格式的数据，都是跨语言、跨平台的
# c、c++、java、php、Python、go等等都能处理
# Windows、Linux、Unix
# json更为清晰且冗余更少，更轻量级，传输效率更高
# xml常常导致复杂的代码，极低的开发效率
# 对于大多数web应用来说根本不需要复杂的XML来传输数据
# 2.结构
# 对象结构
# {
# "key1":"value1",
# "key2":"value2",
# ...
# }
# 数组结构
# [
# 	{
# 	"key1":"value1",
# 	"key2":"value2"
# 	},
# 	{
# 	"key3":"value3",
# 	"key4":"value4"
# 	},
# 	...
# ]
# 3.注意事项
# json格式的数据， 在python中以字符串形式呈现频
# json中的空值为null
# json中除数字外，所以的key和value都是字符串，且一定要以双引号括起来

import json


# 1.对象结构
# json格式数据以字符串的形式呈现
# data_json =' {"status":1,"code":10001,"data":null,"msg":"注册成功"}'   # null会转化为python中的None
# # 将json格式转化为Python中的字典类型
# json_dict = json.loads(data_json)
# print(json_dict)
# 2.数组结构
# some_data_json = '[{"status":1,"code":10001,"data":null,"msg":"注册成功"},' \
# 				 '{"status":2,"code":10001,"data":null,"msg":"注册成功"},' \
# 				 '{"status":3,"code":10001,"data":null,"msg":"注册成功"}]'
# nested_dict_list = json.loads(some_data_json)
# print(nested_dict_list)
# print(nested_dict_list[1]["code"])   # 获取第二个字典中的code

#将python中的字典类型转换了json
# one_dict = {"name":"静宝","age":3,"hobby":None}
# # 宕机（D开头的取巧记忆法，python转换为json）
# one_json = json.dumps(one_dict)
# print(one_json)
# print(type(one_json))
#将嵌套字典的列表转化为json
# one_list = [{"name":"静宝","age":3,"hobby":None},{"name":"静宝的二姨","age":26,"hobby":""}]
# nested_dict_onelist = json.dumps(one_list)
# print(nested_dict_onelist)


# 处理含有json的文本文件
# 1.从文件中读取json格式的数据
with open("one_json_file.txt",encoding="utf-8") as f:
	one_dict = json.load(f)
print(one_dict)
# 2.将json格式的数据写入到文件中
with open("one_json_file.txt",mode="w",encoding="utf-8") as file:
	json.dump(one_dict,file)