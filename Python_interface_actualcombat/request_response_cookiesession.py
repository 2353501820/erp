# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : request_response_cookiesession.py
# author : liushen
# time : 2020/12/16 0016 19:13
---------------------------------------------------
"""
# 接口的分类
# 外部内部广泛的分类
# 按照不同的请求协议http webservice dubbo socket
# 学习的思路--方法很重要。

# 接口的本质：登录接口注册的接口 例如：获取某个省份天气预报的接口
# 类：函数/方法--->就是测试类里面的方法
# Apache tomcat中间件容器服务--->URL地址

# 参数(数据)逻辑
# http协议的接口：
# http请求分为哪几种：get post delete head option

# webservice协议的接口经过封装的http post请求

# 一、请求
# 1.URL
# http：//域名/请求路径
# https：//域名/请求路径
# 域名会被DNS服务器解析为ip地址
# 2.结构
# 请求首行(请求行)
# 请求头(消息报头)
# 请求体(请求正文)
# 3.请求首行(请求行)
# 请求方法

# get
# 获取服务器资源(取回数据)
# 对应sql语句中的select
# 没有请求体(json格式的数据必须放在请求体当中，而get请求方式没有请求体，所以get请求方式不能传json格式数据)
# 请求参数(query string查询字符串) 放在url中以?key1=value&key2=value2的形式
# 不要在处理敏感数据时使用(数据放在url上)

# post
# 往往创建(新增)资源
# 对应sql语句中的insert into
# 有请求体
# 请求参数
# url上的查询字符串参数(请求头中)
# 请求体中的参数(请求体中)
# Body参数方式					Content-type
# Text							text/plain
# Form							application/x-www-form-urlencoded
# JSON							application/json
# File							不确定
# text/plain文本传输为HTTP的报文体中是纯文本，没有任何格式和修饰，服务端就会拿走文本自己处理
# Form这个是最常用的传递参数方式， HTML中都有form标签与其对应其本身采用KeyValue的方式传递参数
# Json格式比Form更加有效的地方是可以传送Object；
# File传输单个文件
# 根据Content-type不同， 服务器去读取HTTP Body中参数的方式也不一样

# put
# 修改服务器的资源
# 对应sql通包中的update
# 有请求体、有参数

# delete
# 删除服务器的资源
# 对应sql语句中的delete from
# 有请求体、有参数


# 请求地址

# 协议版本号
# HTTP/1.1

# 4.请求头(消息报头)
# User-Agent(客户端类型)
# 浏览器
# 手机
# Cookie
# 用户的非敏感信息

# 5.请求体(请求正文)
# get请求没有请求体
# 携带请求参数


# 二、响应
# 1.结构
# 响应首行(状态行)
# 响应头(消息报头)
# 响应体(响应实体)
# 2.响应首行(状态行)
# 状态码大类	表示的含义					客户端client要做的事							服务器端server要做的事
# 1XX			Informational信息			啥都不用做，知道就好							告诉client，信息收到了， 我后续会处理
# 2XX			Successful成功				啥都不用做，知道就好							告诉client，请求已正确处理
# 3XX			Redirection重定向			重新请求返回的新地址->才能获取真正需要的数据	告诉client，你需要的内容由于一些原因，比如地址已发生变化了，然后返回该内容的新地址
# 4XX			Client Error客户端的错误	确保用正确的参数和信息正确，重新请求			告诉client， 请求已正确处理
# 5XX			Server Error服务器端的错	(一般来说)都无需啥操作->往往需要服务器端改了	需要服务器Server端自己找到具体出了啥错->往往是服务器端的代码的bug导致了出错
# 											bug后，重新发送请求

# 最常用的状态码及含义
#  Successful-2xx：成功类， 行为被成功地接受、理解和采纳
#  200 OK
#  服务器成功返回用户请求的数据
#  往往为了简化处理
#  POST创建成功后应该返回201的
#  404 NOTFOUND
# 找不到资源
# 500 INTERNAL SERVER ERROR
# 服务器内部错误
# 最常见的原因是：服务器内部挂了
# 比如你传递参数中有些参数是空，而导致后台代码无法解析，出现异常而崩溃

# 次常用的响应码及含义
# Successful-2xx：成功类，行为被成功地接受、理解和采纳
# 201 CREATED
# 通过POST或PUT创建资源成功
# 204 NO CONTENT
# 资源修改成功但具没有返回内容
# 常用于DELETE操作的返回
# Redirection-3xx：重定向类，为了完成请求，必须进一步执行的动作
# 301永久重定向
# 302临时重定向
# Client Error-4xx：客户端错误类，请求包含语法错误或者请求无法实现
# 401 UNAUTHORIZED
# 没有权限访问该资源
# 典型情况：用户没有登录，没有获得对应的access token而直接访问某资源
# 403 FORBIDDEN
# 禁止访问
# 典型情况：虽然用户已登录，但是去更新/删除需要更高权限才能操作的资源
# 405 METHOD NOT ALLOWED
# 方法不允许
# 举例：比如某个资源不允许POST请求， 但是你确发起了POST请求


# 3.响应头(消息报头)
# Content-Type
# Set-Cookie
# 口服务器将用户信息(session-id) 放到Set-Cookie， 然后将其放到Cookie中保存至浏览器
# 剖析cookie session
# cookie：在客户端存储用户的一些数据比如说用户名啥的浏览记录啥的
# session：在服务器端，记录用户的请求状态，一般默认时间是30min。
# 会员卡机制。
# session_id会存在cookie中， 每次请求cookie中的所有信息都会传送给服务器， 服务器通过session_id来识别是否是同一个用户的请求。不是同一个用户的话，就会要求用户重新登录。
# 为什么会有这种机制?因为http请求是无状态的。
# 很多网站登录后会有csrf-token 或者jwt-token 有了token之后才能访问 不是获取了cookie就可以登录

# 4.响应体(响应实体)
# 响应数据
# html页面或者json格式数据

# 剖析访问授权
# 鉴权：访问的接口是否正常，是否是非法访问，绕过前端访问。token
# 授权：是否具有访问接口的权限。key
# 一般来说：是唯一的，全局的，动态的，具备一定特征
# 具体可以参考这个：
# https：//blog.csdn.net/sjy8207380/article/details/79232644
# 如果遇到接口不会处理怎么办?
#


