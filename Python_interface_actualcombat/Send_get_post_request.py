#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Send_get_post_request.py
# author:gaobo
# time:2020/12/28
import requests


# 通过注册接口，向服务器发起get请求
# 1.构造url
url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/register"

# 2.创建请求参数
params = {
	"mobilephone":"13900001111",
	"pwd":"123456",
	"regname":"静宝"
}

json_params = '{"mobilephone":"13900001111","pwd":"123456","regname":"静宝"}'

headers = {'user_agent':'Mozilla/5.0 keyou/0.0.1'}

# 向服务器当中发起get请求，params为查询字符串参数
# res = requests.get(url,params=params)   # 返回一个Response对象，相当于一个响应报文
# print(res.status_code)   # 返回状态码
# print(res.text)   #获取响应体中的内容，转化的是json格式数据的字符串
# print(res.json())   # 转化为json格式字典
# print(res.cookies)   # 获取cookie信息，类似于Python中的字典类型，支持字典的所有操作


# 向服务器当中发起post请求，get,post 都支持params为查询字符串参数
# res_p = requests.post(url,params=params)

# 讲参数放在请求体中,向data传参，将会使用x-www-from-urlencoded 形式来传参，且会放在请求体中
# res_p = requests.post(url,data=params)   # data也可以传json，data=json_params，会自动转化为字典之后再来传

# json,以json形式传参
res_p = requests.post(url,json=json_params,headers=headers)   # headers=可以修改请求头
print(res_p.headers)   # 可以获取响应报文的头部信息