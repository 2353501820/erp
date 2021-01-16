# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_9_Log_Handle_poll.py
# author : liushen
# time : 2020/12/9 0009 19:00
---------------------------------------------------
"""
# 轮询日志、限制单个文件的大小 需要使用RotatingFileHandle来代替FileHandle日志渠道
from logging.handlers import RotatingFileHandler
import logging
# 1.自定义收集器
case_logger = logging.getLogger("case")
# 2.指定日志收集器的日志等级
case_logger.setLevel(logging.DEBUG)
# 3.输出到文件
file_handle = RotatingFileHandler("cases.log",maxBytes=1024,backupCount=3,encoding="utf-8")
# backupCount是日志文件的数量，maxBytes是一个日志文件的最大字节数 如果要写100M 就是maxBytes=1024 * 1024 * 100
# 4.指定日志输出渠道的日志等级
file_handle.setLevel(logging.DEBUG)
# 5.定义日志显示的格式
simple_handle = logging.Formatter("%(asctime)s - [%(levelname)s] - [日志信息]:[%(message)s]")
file_handle.setFormatter(simple_handle)
# 6.对接，将日志收集器与输出渠道进行对接
case_logger.addHandler(file_handle)

if __name__ == '__main__':
	case_logger.debug("这是DEBUG收集器")

