#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: save_cookie.py
# author:liushen
# time:2020/12/28
import requests


# 通过登录接口，向服务器发起post请求
# 1.构造url
login_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/login"
recharge_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge"

# 2.创建请求参数
login_params = {"mobilephone":"13900001111",
				"pwd":"123456"}
recharge_params = {"mobilephone":"13900001111",
				   "amount":"500"}
headers = {'user_agent':'Mozilla/5.0 keyou/0.0.1'}

# 3.向服务器当中发起post请求，params为查询字符串参数
# # 登录
# res_login = requests.post(login_url,data=login_params,headers=headers)
# vip_cookies = res_login.cookies
# # 充值
# res_recharge = requests.post(recharge_url,data=recharge_params,cookies=vip_cookies)

# 创建会话对象
one_session = requests.Session()   # 返回一个Session对象，在整个会话过程中自动记录Cookie
# 登录
res_login = one_session.post(url=login_url,data=login_params)
# 充值
res_recharge = one_session.post(url=recharge_url,data=recharge_params)

# 4.关闭会话
one_session.close()