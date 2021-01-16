#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_RE_match.py
# author:liushen
# time:2021/01/02
# 正则表达式
import re


target_str = '{"mobilephone":"${not_exited_tel}","pwd":"123456","regname":"静宝"}'

# 1.将正则字符串编译成Pattern对象
# pattern = re.compile(r".*\$\{not_exited_tel\}")   # 知识拓展.*相当于匹配所有{} 0次或无限次
pattern = re.compile(r"\$\{not_exited_tel\}")

# 2.使用pattern对象去匹配文本
# 如果未匹配上，则返回None,如果能匹配则返回match对象
# match_obj = re.match(pattern,target_str)   # match偏难,做了解
# 查找
match_obj = re.search(pattern,target_str)

# sub中第一个参数为模式对象，第二个参数为需要替换的值，第三个参数为原始字符串
new_str = re.sub(pattern,"19811112222",target_str)
pass