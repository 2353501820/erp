# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_7_python_file.py
# author : liushen
# time : 2020/8/20 0020 22:08
---------------------------------------------------
"""
# 概念：1.计算机中的文件就是存储在某种长期储存设备上的一段数据2.长期存储设备包括：硬盘、U盘、移动硬盘光盘..
# 作用：作用将数据长期保存下来，在需要的时候使用
# 存储方式：在计算机中，文件是以二进制的方式保存在磁盘上的
# 分类：1.文本文件：可以使用文本编辑软件查看本质上还是二进制文件例如：python的源程序
# 2.二进制文件：保存的内容不是给人直接阅读的，而是提供给其他软件使用的例如：图片文件、音频文件、视频文件等等不能使用文本编辑软件查看
# 文件中的基本操作：
# 1.打开文件
# one_file = open('Class_7_sanguo.txt',encoding='utf-8')   # 不同的系统，若没有写encoding='utf-8'可能会报错，'utf-8'='utf8'
# # 2.读，将文件内容读入内存；写，将内存内容写入文件
# # print(one_file.read())   # 一次性读取文件中所有内容，以字符串方式展现，缺点是若文件内存过大，会占用大量内存
# # print(one_file.readline())   # 每调用一次读取一行
# print(one_file.readlines())   # 相当于把每一行都读取当做列表中的元素，返回一个列表
# # 3.关闭文件
# one_file.close()
# open函数负责打开文件，并且返回文件对象，read/white/close三个方法都需要通过文件对象来调用
# read：
# 1.open函数的第一个参数是要打开的文件名(文件名区分大小写)如果文件存在，返回文件操作对象，如果文件不存在，会抛出异常
# 2.read方法可以一次性读入并返回文件的所有内容
# 3.close方法负责关闭文件，如果忘记关闭文件，会造成系统资源消耗，而且会影响到后续对文件的访问
# 注意：read方法执行后， 会把文件指针移动到文件的末尾
# 在开发中，通常会先编写打开和关闭的代码，再编写中间针对文件的读/写操作

# 文件指针(了解)
# 1.文件指针标记从哪个位置开始读取数据第一次打开文件时，通常文件指针会指向文件的开始位置
# 2.当执行了read方法后， 文件指针会移动到读取内容的末尾默认情况下会移动到文件末尾

# 打开文件的方式
# 默认以只读方式打开文件，并且返回文件对象。语法：f = open('文件名','访问方式')
# r:以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。如果文件不存在就报错，存在就正常读取
# w:以只写方式打开文件。若文件不存在，新建文件然后写入；如果存在，先清空(覆盖)文件内容，再写入

# one_file = open("sanguo.txt",mode="w",encoding="utf-8")
# one_file.write("月色真美")   # 写入只能写入字符串，可以调用函数结果为字符串
# one_file.close()

# a:以追加方式打开文件。如果文件不存在，新建文件，然后写入；如果存在，在文件尾部追加写入(文件指针将会放在文件的结尾)

# one_file = open("sanguo.txt",mode="a+",encoding="utf-8")
# one_file.write("月色真美")
# one_file.close()

# r+:以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常
# w+:以读写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件
# a+:以读写方式打开文件，如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
# b:二进制模式比如rb、wb、ab， 以bytes类型操作数据
# one_image = open("yzm.jpg","rb")
# another_image = open("yzm1.jpg","wb")
#
# image_content = one_image.read()
# another_image.write(image_content)
#
# one_image.close()
# another_image.close()

# 频繁的移动文件指针，会影响文件的读写效率，开发中更多的时候会以只读、只写的方式来操作文件

# 大文件复制（文件内容过大）
# rec_file = open("sanguo.txt","r+",encoding="utf-8")   # 源文件
# dec_file = open("sanguo_1.txt","w+",encoding="utf-8")   # 目标文件
#
# while True:
# 	rec_content = rec_file.readline()
# 	if not rec_content:
# 		break
# 	dec_file.write(rec_content)
#
# rec_file.close()
# dec_file.close()



# 作业
# 1.什么是文件？有哪些种类？
# 文件是计算机需要长期储备的一段数据，分为文本文件和二进制文件
# 2.文件的操作步骤
# 打开、读取、写入、关闭
# 3.操作文件的常用函数/方法有哪些？
# open read write close
# 4.read、readline、readlines有什么区别？（返回的对象类型、文件指针位置、应用场景）
# read，readline、readlines返回对象类型分别是字符串、字符串、列表，文件指针位置分别是文件末尾，下一行文件的开头，文件的末尾,应用场景分别是小文件、大文件、对每行数据进行处理
# 5.打开文件的方式有哪些？
# r w a r+ w+ a+ b
# 6.编写如下程序
# 将你喜欢的一首歌，拓展名为.mp3，通过文件读写的方式将其复制，并修改文件名
# one_song = open("夏天的风.mp3","rb")
# another_song = open("夏天的风1.mp3","wb")
# content_song = one_song.read()
# another_song = write(content_song)
# one_song.close()
# another_song.close()

# 如果mp3比较大
# one_song = open("夏天的风.mp3","rb")
# another_song = open("夏天的风1.mp3","wb")
#
# while True:
# 	part_content = one_song.read(1024)
# 	if not part_content:
# 		break
# 	another_song = write(part_content)
# one_song.close()
# another_song.close()

# 7.编写如下程序有两行数据，存放在txt文件里面：
# url：http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url：http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：(可定义函数)
# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register', 'mobile':'18866668888','pwd':'123456'} ，
# {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'} ]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写
# file_test = open("test_1","w+",encoding="utf-8")
# file_test.write("url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\n"
# 				"url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000")
# file_test.close()
#
# f = open("./test_1")
# txt=f.read()
# # print(txt)
# txt_list = []
# # a =[]
# txt = txt.split("\n")
# for i in txt:
# 	s_i = i.split('@')
# 	txt_dict = {}
# 	for keys in s_i:
# 		key=keys.split(":",1)
# 		txt_dict[key[0]]=key[1]
# 		# a.append(key)
#
# 	# a = dict(a)
# 	txt_list.append(txt_dict)
#
# print(txt_list)

# 8.编写如下程序
# 创建一个txt文本文件,以csv格式(数据之间以英文逗号分隔) 来添加数据
# a.第一行添加如下内容：name,age,gender,hobby,motto
# b.从第二行开始，每行添加具体信息，例如:
# 可忧,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!
# c.具体用户信息要求来自于一个嵌套字典的列表(可自定义这个列表)，例如：
# person_info=[{"name":"可优","age":17,"gender":"男","hobby":"臭美","motto": "Always Be Coding!"} ,
# {"name":"柠檬小姐姐","age":16,"gender":"女","hobby":"可优","motto":"Lemon is best!"},]
# d.将所有用户信息写入到txt文件中之后，再读出
# 注意：csv格式的数据，是以英文逗号分隔的

# person_info=[{"name":"可优",
# 			  "age":17,
# 			  "gender":"男",
# 			  "hobby":"臭美",
# 			  "motto": "Always Be Coding!"} ,
# 			 {"name":"柠檬小姐姐",
# 			  "age":16,
# 			  "gender":"女",
# 			  "hobby":"可优",
# 			  "motto":"Lemon is best!"},
# 			 ]


# def handle_data(one_list):
# 	"""
# 	处理数据
# 	:param one_list:嵌套字典的列表
# 	:return:列表
# 	"""
# 	datas_str = ""
# 	for item in one_list:
# 		# 将所有值转化为列表后用逗号拼接
# 		tmp_list = []
# 		for i in item.values():
# 			tmp_list.append(str(i))
# 		datas_str = datas_str + ",".join(tmp_list) + "\n"
# 	return datas_str
#
#
# def file_handle(file_path,data=None,mode="a+",encoding="utf-8"):
# 	"""
# 	读写数据
# 	:param file_path:文件路径
# 	:param data:添加的数据
# 	:param mode:文件打开模式
# 	:param encoding:文件编码
# 	:return:
# 	"""
# 	# 打开文件
# 	one_file = open(file_path,mode=mode,encoding=encoding)
# 	if data is not None:   # data如果不为None,则添加内容
# 		# 添加内容到文件
# 		datas_size = one_file.write(data)
# 		# 关闭文件
# 		one_file.close()
# 		return datas_size
# 	else:   # 如果data为None,则读取内容，并返回
# 		# 读取内容
# 		one_file.seek(0)   # 将文件指针设置到起始行
# 		datas_str = one_file.read()
# 		one_file.close()
# 		return datas_str
#
#
#
# def main():
# 	"""
# 	主要函数
# 	:return:
# 	"""
# 	file_path = "result_datas.txt"
# 	first_line = "name,age,gender,hobby,motto\n"
#
# 	# 写入第一行内容
# 	file_handle(file_path,first_line)
# 	# 写入其他数据
# 	write_datas = handle_data(person_info)
# 	file_handle(file_path,write_datas)
# 	# 读取数据
# 	print("最终文件内容为：\n{}".format(file_handle(file_path)))
#
#
# if __name__ == '__main__':
# 	main()


person_info=[{"name":"可优",
			  "age":17,
			  "gender":"男",
			  "hobby":"臭美",
			  "motto": "Always Be Coding!"} ,
			 {"name":"柠檬小姐姐",
			  "age":16,
			  "gender":"女",
			  "hobby":"可优",
			  "motto":"Lemon is best!"},
			 ]


def handle_data (one_list):
	"""
	处理数据，把嵌套字典的列表转化为字符串型的列表
	:param one_list:
	:return:
	"""

	datas_str = ""
	for item in one_list:
		tmp_list = []  # 先定义一个空列表
		for i in item.values():
			tmp_list.append(str(i))
		datas_str = datas_str + ",".join(tmp_list) + "\n"
	return datas_str


def handle_file(file_path,data=None,mode="a+",encoding="utf-8"):
	"""
	处理文件
	:param file_path:
	:param data:
	:param mode:
	:param encoding:
	:return:
	"""
	one_file = open(file_path,mode=mode,encoding=encoding)
	if data is not None:
		data_size = one_file.write(data)
		one_file.close()
		return data_size
	else:
		one_file.seek(0)
		data_file = one_file.read()
		one_file.close()
		return data_file


def main():
	"""
	定义主函数
	:return:
	"""
	file_path = "result_datas.txt"
	first_line = "name,age,gender,hobby,motto\n"
	handle_file(file_path,first_line)
	write_data = handle_data(person_info)
	handle_file(file_path,write_data)



if __name__ == '__main__':
	main()