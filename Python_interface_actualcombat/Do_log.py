# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Do_log.py.py
# author : gaobo
# time : 2020/12/11 0011 18:50
---------------------------------------------------
"""
import logging
from logging.handlers import RotatingFileHandler

from Python_interface_actualcombat.Do_config import do_config


class HandleLog:
	"""
	封装处理日志的类
	"""
	def __init__(self):
		self.case_logger = logging.getLogger(do_config("log","logger_name"))
		self.case_logger.setLevel(do_config("log","logger_level"))
		console_handle = logging.StreamHandler()
		file_handle = RotatingFileHandler(filename=do_config("log","log_filename"),maxBytes=do_config("log","max_byte"),backupCount=do_config("log","backcount"),
											   encoding="utf-8")
		console_handle.setLevel(do_config("log","console_level"))
		file_handle.setLevel(do_config("log","file_level"))
		simple_log = logging.Formatter(do_config("log","simple_log"))
		verbose_log = logging.Formatter(do_config("log","verbose_log"))
		console_handle.setFormatter(simple_log)
		file_handle.setFormatter(verbose_log)
		self.case_logger.addHandler(console_handle)
		self.case_logger.addHandler(file_handle)
		# 这里需要返回一个实例属性，但是构造方法是不能够使用return 所有不能用return self.case_logger，所以我们需要再创建一个实例对象


	def get_logger(self):
		"""
		获取Logger日志器对象
		:return:
		"""
		return self.case_logger
do_log = HandleLog().get_logger()


if __name__ == '__main__':
	case_logger = HandleLog().get_logger()
	case_logger.debug("这是debug收集器")
	case_logger.info("这是info收集器")
	case_logger.warning("这是warning收集器")
	case_logger.error("这是error收集器")
	case_logger.critical("这是critical收集器")


