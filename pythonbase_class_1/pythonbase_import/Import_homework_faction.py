# -*-coding: utf-8 -*-
# @time     :2020-7-29 16:39
# @author   :liushen
# @email    :lsliushen@126.com
# @file     :Import_homework_faction.py
# @software :PyCharm
# 9.编写如下程序
# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# b.在每个模块中需要添加测试代码
import math


def area_circle(r):
    """
    the area of a circle
    :param r: 半径
    :return: 面积
    """
    area_yuan = math.pi * (r ** 2)
    area_yuan = round(area_yuan,3)
    return area_yuan


def circumference_circle(r):
    """
    circumference of a circle
    :param r: 半径
    :return: 周长
    """
    circumference_yuan = 2 * math.pi * r
    circumference_yuan = round(circumference_yuan, 3)   # 四舍五入，保留三位小数
    return circumference_yuan


def area_rectangle(long_side,short_side):
    """
    the area of a rectangle
    :param long_side: 长
    :param short_side: 宽
    :return: 长方形的面积
    """
    area_fang = long_side * short_side
    area_fang = round(area_fang,2)
    return area_fang


def circumference_rectangle(long_side,short_side):
    """
    circumference of a rectangle
    :param long_side: 长
    :param short_side: 宽
    :return: 周长
    """
    circumference_fang = (long_side + short_side) * 2
    circumference_fang = round(circumference_fang,2)
    return circumference_fang


if __name__ == '__main__':
    # print(area_circle(3))
    # print(area_rectangle(3.5,5))
    radius = float(input("请输入圆的半径："))
    print("半径为{:.2f}的圆，面积为{}，周长为{}".format(radius,area_circle(radius),circumference_circle(radius)))
    rectangle_long = float(input("请输入长方形的长："))
    rectangle_short = float(input("请输入长方形的宽："))
    # print("长为{},宽为{},的长方形，面积为{},周长为{}".
    # format(rectangle_long,rectangle_short,area_rectangle(rectangle_long,rectangle_short),circumference_rectangle(rectangle_long,rectangle_short)))
    param = (rectangle_long,rectangle_short,area_rectangle(rectangle_long,rectangle_short),circumference_rectangle(rectangle_long,rectangle_short))
    print("长为{},宽为{},的长方形，面积为{},周长为{}".format(*param))
