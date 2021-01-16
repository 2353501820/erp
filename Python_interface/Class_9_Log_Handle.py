# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_9_Log_Handle.py
# author : liushen
# time : 2020/12/3 0003 18:37
---------------------------------------------------
"""
# 1.记录的信息不全面，比如没有时间信息、执行人的信息、日志等级、日志详细信息
# 2.文件记录的信息混乱，不方便使用脚本统计
# 3.当日志文件大的时候没有自动进行日志轮转功能

# 使用日志器
# 日志 --> 菜
# 日志收集器（logger）用来装日志信息 --> 装菜的容器
# 日志收集器的日志等级（NOTSET(0)、DEBUG(10)、INFO(20)、WARNING(30)、ERROR(40)、CRITICAL(50)）等级从左至右越来越高（日志等级>=当前设置的都能收集，反之不能）
# 日志输出渠道（console终端、文件、smtp、http）(Handlers) --> 装好的菜放置的地方
# 日志输出渠道的日志等级  --> 放置菜的地方对菜种类的限制
# 日志的显示格式(Formatter)  --> 菜的摆盘方式


# 1.定义日志收集器（装日志信息的容器）
import logging   # 是python系统自带的模块 不需要安装
# 默认有一个root根收集器，根收集器使用的日志等级为warning
# logging.debug("这是debug收集器")
# logging.info("这是info收集器")
# logging.warning("这是warning收集器")
# logging.error("这是error收集器")
# logging.critical("这是critical收集器")

# 1.因不满足需求，所以要自定义收集器，返回Logger对象
case_logger = logging.getLogger("case")   #如果不传name参数，那么默认使用root根收集器

# 2.指定日志收集器的日志等级
case_logger.setLevel(logging.DEBUG)   # 能收集除NOTSET以外所有等级的日志信息，这边等级往往会比较低

# 3.定义日志输出渠道（可以指定多个渠道）
# Handler对象
# 输出到console控制台
console_handle = logging.StreamHandler()
# 输出到文件
file_handle = logging.FileHandler("cases.log",encoding="utf-8")

# 4.指定日志输出渠道的日志等级
# console_handle.setLevel(logging.ERROR)
console_handle.setLevel("ERROR")   # 如果不能被收集器收集的日志，一定没办法输出到渠道中
file_handle.setLevel(logging.INFO)

# 5.定义日志的显示格式
simple_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s")   # "%()s"是默认格式，asctime日志开始时间，levelname等级名称，简单的日志格式
verbose_formatter = logging.Formatter("%(asctime)s - [%(levelname)s]- [%(module)s]- [%(name)s] - [%(lineno)d] [日志信息]:%(message)s")   # 比较复杂一些的日志格式

console_handle.setFormatter(simple_formatter)   # 控制台为简单的日志格式
file_handle.setFormatter(verbose_formatter)   # 文件为复杂一些的日志格式

# 6.对接，将日志收集器与输出渠道进行对接
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)

if __name__ == '__main__':
	case_logger.debug("这是debug收集器")
	case_logger.info("这是info收集器")
	case_logger.warning("这是warning收集器")
	case_logger.error("这是error收集器")
	case_logger.critical("这是critical收集器")




