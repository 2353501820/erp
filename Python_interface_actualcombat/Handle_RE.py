#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_RE.py
# author:liushen
# time:2021/01/02
import re


# 定义两个匹配模式
not_exited_tel_pattern = re.compile(r"\$\{not_exited_tel\}")
regname_pattern = re.compile(r"\$\{regname\}")


def not_exited_tel_replace(data):
	# 如果未匹配上，则返回None,如果能匹配到${not_exited_tel}这样的字符串则返回match对象
	if re.search(not_exited_tel_pattern,data):
		# sub中第一个参数为模式对象，第二个参数为需要替换的值，第三个参数为原始字符串
		# sub返回的是修改之后的字符串
		data = re.sub(not_exited_tel_pattern,"18911112222",data)

	if re.search(regname_pattern,data):
		data = re.sub(regname_pattern,"静宝",data)

	return data

if __name__ == '__main__':
	target_str1 = '{"mobilephone":"${not_exited_tel}","pwd":"123456","regname":"静宝"}'
	target_str2 = '{"mobilephone":"${not_exited_tel}","pwd":"123456"，"regname":"${regname}"}'
	target_str3 = '{"mobilephone":"","pwd":"123456",}'
	target_str4 = '{"mobilephone":"18000001212","pwd":""}'
	print(not_exited_tel_replace(target_str1))
	print(not_exited_tel_replace(target_str2))
	print(not_exited_tel_replace(target_str3))
	print(not_exited_tel_replace(target_str4))
