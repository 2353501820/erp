# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Class_9_class_object.py
# author : liushen
# time : 2020/9/14 0014 22:09
---------------------------------------------------
"""
# 类
# 类是对一惧有相同特征或者行为的事物的一个统称，是抽象的，不能直接使用
# 特征被称为属性
# 它是什么样的
# 行为被称为方法
# 它可以做什么
# 类就相当于建造房子时的施工图纸(blueprint) ，是一个模板，是负责创建房子(对象) 的


# 对象
# 对象是由类创建出来的一个具体存在，可以直接使用
# 由哪一个类创建出来的对象，就拥有在哪一个类中定义的：
# 属性
# 方法
# 对象就相当于用施工图纸建造的房子
# 在程序开发中应该先有类，再有对象


# 类和对象的关系
# 类是模板，对象是根据类这个模板创建出来的
# 先有类，再有对象
# 类只有一个，而对象可以有很多个
# 	不同的对象之间属性可能会各不相同
# 类中定义了什么属性和方法，对象中就有什么属性和方法，不可能多，也不可能少


# 类的设计要素
# 在程序开发中，要设计一个类，通常需要满足一下三个要素：
# 类名
# 满足大驼峰命名法
# 属性
# 这类事物具有什么样的特征
# 方法
# 这类事物具有什么样的行为


# 大驼峰命名法
# 每个单词的首字母大写
# 单词与单词之间没有下划线

# 确定类名
# 名词提炼法分析整个业务流程，出现的名词，通常就是找到的类


# 案例分析
# 1.在Python中要定义一个只包含方法的类，语法格式如下：
# c1ass 类名：
# 	def 方法1(se1f，参数列表):
# 		pass
# 	def 方法2(se1f，参数列表):
# 		pass

# 方法的定义格式和之前学习过的函数几乎一样
# 区别在于第一个参数必须是se1f


# 2.创建对象
# 当一个类定义完成之后，要使用这个类来创建对象，语法格式如下：
# 对象变量 = 类名()


# 3.self
# 使用self在方法内部输出每个人的名字
# 由哪一个对象调用的方法，方法内的se1f就是哪一个对象的便利贴
# 在类封装的方法内部，se1f就表示当前调用方法的对象自身
# 调用方法时程序员不需要传递se1f参数
# 在方法内部
#  可以通过se1f.访问对象的属性
#  也可以通过se1f.调用其他的对象方法


# 定义带有属性的类
# 1.案例
# 在类的外部，通过变量名，访问对象的属性和方法
# 在类封装的方法中，通过se1f.访问对象的属性和方法


# 2.初始化方法
# 当使用类名()创建对象时，会自动执行以下操作：
#  为对象在内存中分配空间――创建对象
#  为对象的属性设置初始值――初始化方法(init)
# 这个初始化方法就是__init__方法，__init__是对象的内置方法
# __init__方法是专门用来定义一个类具有哪些属性的方法


# 3.在初始化方法内部定义属性
# 在__init__方法内部使用se1f.属性名 = 属性的初始值就可以定义属性
# 定义属性之后， 再使用Person类创建的对象， 都会拥有该属性



class Person:
	"""
	define a person class
	"""
	head = 1   # 定义类属性
	def __init__(self,name,age,height):
		self.hair = '小绒毛'   # 类的里面创建属性：在使用构造器传参数的时候可以给对象设置属性
		self.name = name   # 相当于给实例创建name的内置属性，self.name相当于获取属性把属性拿过来用；self.name = 相当于创建（定义）属性
		self.age = age
		self.height = height
		# self.head = 2   # 会优先寻找构造器中设置的属性，若构造器中没有，才会去找类属性 类似于局部变量
		print('姓名：{}\n年龄：{}\n身高：{}\n头发{}'.format(self.name,self.age,self.height,self.hair))

	def run(self):   # 定义实例方法或者叫属性方法
		# print("人会跑")
		# return "人会跑"
		self.weather_forecast()   # 在类的内部，可以通过self.静态方法名来调用静态方法
		print("{}可以去跑步".format(self.name))


	def eat(self):
		print('人会吃早餐')
		print("在类的里面调用实例方法", self.run())

	def __str__(self):
		return '{}'.format(self.name)

	@classmethod
	def angry(cls):   # 类方法，他的目的就是修改类属性
		cls.head = 3   # 在类的内部修改类属性,使用cls而不使用Person（类名）的原因是因为可以更改类名，否则需要重复更改
		# cls.weather_forecast()   # 在类方法中，可以通过cls.静态方法名来调用静态方法
		pass

	@staticmethod   # 我们往往会把跟类相关的函数放在类中，作为静态方法，这样封装性比较好
	def weather_forecast():
		"""
		播报天气
		:return:
		"""
		print ("天气晴朗")
		print ("适合出游")
		# Person.weather_forecast()   # 在静态方法中，可以通过类名.静态方法名来调用其他静态方法


one_person = Person('静宝',2.5,90)   # 使用类名+()：就会调用_init_的构造器（方法），第一个参数就是它本身创建的实例
two_person = Person('千千',0,0)
# one_person.hair = '小绒毛'   # 这种方法不好，动态创建属性
one_person.hair = '娃娃头'   # 修改对象
print(one_person.hair)
# print(one_person.run())   # 在类的外面调用实例方法,如果用print 则会返回None，因为类名+实例方法本身就相当于print
print(one_person.run())   # 在实例方法中用return，在类的外面用print可以返回值
one_person.eat()
# one_person.weather_forecast()   #在类的外部 我们可以通过对象.静态方法名来调用静态方法
# Person.weather_forecast()   # 也可以通过类.静态方法名来调用静态方法
one_person.run()


# __str__方法
# 1.定义
# 在Python中， 使用print输出对象变量， 默认情况下， 会输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址(十六进制表示)
# 如果在开发中， 希望使用print输出对象变量时， 能够打印自定义的内容， 就可以利用__str__这个内置方法了
# 注意：_str_方法必须返回一个字符串
print(one_person)


# 身份运算符
# 1.定义
# 身份运算符用于比较两个对象的内存地址是否一致--是否是对同一个对象的引用
# 在Python中针对None比较时， 建议使用is判断
# 运算符					描述									实例
# is		is是判断两个标识符是不是引用同一个对象		x is y,类似id(x) == id(y)
# is not 	is not是判断两个标识符是不是引用不同对象	x is not y,类似id(a) != id(b)

# 2.is与==区别
# is用于判断两个变量引用对象是否为同一个
# ==用于判断引用变量的值是否相等


# 类属性和实例属性
# 1.概念
# 类属性就是给类定义的属性
# 通常用来记录与这个类相关的特征
# 类属性不会记录具体对象的特征


# 类方法和静态方法
# 1.类方法
#  类属性就是针对类定义的属性
#   使用赋值语句在c1ass关键字下方可以定义类属性
#   类属性用于记录与这个类相关的特征
print('{}有{}个头'.format(one_person.name,one_person.head))   # 使用对象来找类属性，不推荐
print('人有{}个头'.format(Person.head))    # 使用类来查找类属性，会就近找到类

# one_person.head = 2   # 变量名.对象名= 这种形式是创建了个实例属性类似于创建局部变量,即使有一样的变量名，不会修改类属性
# Person.head = 3   # 在类的外面修改类属性 只能通过 类名.对象名 = 这种形式修改类属性 但是这种方法不推荐！！！
print('{}有{}个头'.format(one_person.name,one_person.head))
print('{}有{}个头'.format(two_person.name,two_person.head))
print('人有{}个头'.format(Person.head))

Person.angry()
one_person.angry()   # 通过对象来调用类方法，它不是将对象本身传给cls，而是将对象所属的类传给cls

# 类方法和静态方法
# 1.类方法
#  类属性就是针对类定义的属性
#   使用赋值语句在c1ass关键字下方可以定义类属性
#   类属性用于记录与这个类相关的特征
#  类方法就是针对类定义的方法
#   在类方法内部可以直接访问类属性或者调用其他的类方法
# 语法如下
# @classmethod
# def 类方法名(cls):
# 	pass
# 类方法需要用修饰器@c1ass method来标识， 告诉解释器这是一个类方法
# 类方法的第一个参数应该是c1s
#  由哪一个类调用的方法，方法内的c1s就是哪一个类的引用
#  这个参数和实例方法的第一个参数是self类似
#  提示使用其他名称也可以，不过习惯使用c1s
#  通过类名.调用类方法，调用方法时，不需要传递c1s参数
#  在方法内部
#  可以通过c1s.访问类的属性
#  也可以通过c1s.调用其他的类方法
# 在类方法内部，可以直接使用cls访问类属性或者调用类方法



# 2.静态方法
# 在开发时，如果需要在类中封装一个方法，这个方法：
#  既不需要访问实例属性或者调用实例方法
#  也不需要访问类属性或者调用类方法
# 这个时候，可以把这个方法封装成一个静态方法
# 语法如下
# @staticmethod
# def 静态方法名():
# 	pass
# 静态方法需要用修饰器@staticmethod来标识， 告诉解释器这是一个静态方法
# 通过类名.调用静态方法



# 3.案例小结
# 实例方法--方法内部需要访问实例属性
# 实例方法内部可以使用类名.访问类属性
# 类方法--方法内部只需要访问类属性
# 静态方法--方法内部，不需要访问实例属性和类属性
# 提问
# 如果方法内部即需要访问实例属性，又需要访问类属性，应该定义成什么方法?
# 答案
# 应该定义实例方法因为，类只有一个，在实例方法内部可以使用类名.访问类属性



# 七、继承
# 1.概念
# 子类拥有父类的所有方法和属性


class Animal(object):   # 在python3当中，创建类会默认继承object类
	"""
	创建动物类
	"""
	def __init__(self,name,age,color):
		"""

		:param name:名字
		:param age:年龄
		:param color:毛色
		"""
		self.name,self.age,self.color = name,age,color

	def eat(self):
		print("{}需要吃东西".format(self.name))

	def drink(self):
		print("{}需要喝水".format(self.name))

	def run(self):
		print("{}可以跑".format(self.name))

	def sleep(self):
		print("{}需要睡觉".format(self.name))


class Dog(Animal):
	"""
	定义狗类
	Animal 父类，基类
	Dog 子类
	"""
	def bark(self):
		print("{}会汪汪叫".format(self.name))


class ChinaDog(Dog):
	"""
	定义中华田园犬
	"""
	def __init__(self,name,age,color,job):
	# 	"""
	#	这里是直接丢弃父类的__init__构造方法不用,相当于重写
	# 	:param name:名字
	# 	:param age:年龄
	# 	:param color:毛色
	# 	"""
	# 	self.name,self.age,self.color,self.job = name,age,color,job
	# 不丢弃父类的__init__构造方法，而是在父类的基础上修改，super()相当于是父类的一个对象
	# 先调用父类的构造方法设置name,age,color这三个属性再添加job属性，对父类的拓展，相当于Java中的派生
		super().__init__(name,age,color)
		self.job = job


	def define_family(self):
		print("{}会看家护院".format(self.name))

	def run(self):   # 当定义了一个跟父类一样的方法名时，会覆盖父类的方法，父类的方法将不会被执行，先检查自己，没有再查父类，这种方法叫方法的重写
		print("{}是家养的不会跑".format(self.name))

	def eat(self):
		super().eat()   # 	这里就是先调用父类的实例方法再出现我们的eat，这就是类的拓展
		print("{}可以吃剩菜剩饭".format(self.name))



xiaolang = Dog("小浪",1,"灰色")
xiaolang.eat()
xiaolang.sleep()
xiaolang.bark()
# 继承父类，会将父类的所有实例方法和类方法、类属性都继承（私有方法除外，测开涉及）
ahuang = ChinaDog("阿黄",2,"黄色","看家护院，陪伴家人")
# ahuang = ChinaDog("阿黄",2,"黄色")
ahuang.eat()
ahuang.bark()
ahuang.define_family()
ahuang.run()
# print(ahuang.job)
ahuang.eat()

# 作业
# 必做题
# 1.__str__的作用?
# 参考答案：
# 打印对象时会调用
# 必须return字符串
# 2.is与==的区别?
# 参考答案：
# is为身份运算符，是否是对同一个对象的引用，跟使用id查看内存地址，再判断地址是否一致类似
# ==为比较运算符，判断值是否相等
# 3.类属性是什么?如何定义?在类外和类里如何调用?
# 参考答案：
# 类属性是什么?
# 给类定义的属性
# 用来记录与这个类相关的特征
# 不会记录具体对象的特征

# 如何定义?
# 在类的定义下方，使用类属性名=类属性值，这种形式来定义

# 在类外和类里如何调用?
# 类外
#  对象.类属性名
#  类.类属性名
#  类.类方法(需要在类中定义)
# 类里
#  self.类属性名
#  类.类属性名
#  在类方法中,cls.类方法

# 4.类方法是什么?作用?如何定义?
# 参考答案：
# 类方法是什么?
# 针对类定义的方法

# 作用?
# 修改、获取类属性

# 如何定义?
# @c1assmethod
# def 类方法名(c1s):
# 	pass
# 需要修饰器@c1assmethod来标识
# 第一个参数应该是c1s
# 在类方法内部，可以直接使用c1s访问类属性或者调用类方法

# 5.编写如下程序
# 创建一个名为Restaurant的类， 要求拥有饭店名(restaurant_name)和美食种类(cooking_type) 两个属性。
# a.需要创建一个名为describe_restaurant()的方法(描述饭店名和美食种类相关信息) 和一个名为open_restaurant()的方法(显示饭店正在营业)
# b.根据这个类创建一个名为restaurant的实例,分别打印其两个属性， 再调用前述两个方法。
# 参考答案：
class Restaurant:
	"""
	创建一个餐馆类
	"""
	def __init__(self, restaurant_name, cooking_type):
		self.restaurant_name,self.cooking_type = restaurant_name,cooking_type

	def describe_restaurant(self):
		print("*" * 50)
		print("{:^40s}\n".format(self.restaurant_name))   # ^代表居中对齐40s代表占据40个字符
		for key, item in enumerate(self.cooking_type,start=1):
			print("\t{}.{}".format(key,item))
		print("\t请点餐，祝您用餐愉快!")
		print("*" * 50)

	def open_restaurant(self):
		print("{},正在营业...".format(self.restaurant_name))

cooking_types = ["北京烤鸭","扬州炒饭","蒸羊羔","东坡肉"]
famous_restaurant = Restaurant("静宝的小厨房",cooking_types)
famous_restaurant.describe_restaurant()
famous_restaurant.open_restaurant()


# 6.编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）
class MathOperation:
	"""
	数学计算
	"""
	def __init__(self,no_one,no_two):
		self.no_one,self.no_two = no_one,no_two

	def add(self):
		return self.no_one + self.no_two

	def minus(self):
		return self.no_one - self.no_two

	def multiply(self):
		return self.no_one * self.no_two

	def division(self):
		try:
			return round(self.no_one / self.no_two,2)   # 相乘后四舍五入
		except ZeroDivisionError:
			# print("除0错误")
			return "∞"

nums = (25,0)
math_operation = MathOperation(*nums)
print("{} + {} = {}".format(*nums,math_operation.add()))
print("{} - {} = {}".format(*nums,math_operation.minus()))
print("{} * {} = {}".format(*nums,math_operation.multiply()))
print("{} / {} = {}".format(*nums,math_operation.division()))

# 7.编写一个工具箱类，需要有工具名称，功能描述，价格
# 能够添加工具，删除工具，查看工具，并且能获取工具箱中工具的总数


class Tool:
	"""
	工具
	"""
	def __init__(self,name,desc,price):
		"""
		构造方法
		:param name:工具名称
		:param desc:工具描述
		:param price:价格
		"""
		self.name,self.desc,self.price = name,desc,price

	def describe_tool(self):
		"""
		获取工具信息
		:return:
		"""
		print("{:*^100}".format("开始描述"))
		print("名称:{0.name}\n功能:{0.desc}\n价格:{0.price}".format(self))
		# print("描述工具\n名称:{}\n功能:{}\n价格:{}".format(self.name,self.desc,self.price))
		print("{:*^100}".format("描述介绍"))

	def __str__(self):
		return "<{}>".format(self.name)


class ToolPackage:
	"""
	定义工具箱类
	"""
	tools_count = 0

	def __init__(self,name):
		self.name = name
		self.all_tools = []   # 存放工具的列表

	def add(self,one_tool):
		"""
		添加工具到工具箱中
		:param one_tool:工具对象
		:return:
		"""
		if isinstance(one_tool,Tool):
			self.all_tools.append(one_tool)
			self.modify_tool_count()
			print("成功添加【{}】到【{}】中！".format(one_tool.name,self.name))
		else:
			print("{}不是工具对象，无法添加！".format(one_tool))

	def has_tool(self,one_tool):
		"""
		判断工具是否在工具箱中
		:param one_tool:Tool工具对象或者工具名
		:return:True or False
		"""
		if isinstance(one_tool,Tool):   # 如果one_tool是工具对象
			return one_tool in self.all_tools   # 判断是否在工具箱中
		elif isinstance(one_tool,str):   # 如果是工具名，字符串
			for tool_obj in self.all_tools:
				if one_tool == tool_obj.name:
					return True
		return False

	def remove(self,one_tool):
		"""
		删除工具
		:param one_tool:Tool工具对象或者工具名
		:return:
		"""
		if self.has_tool(one_tool):   # 如果要删除的工具存在
			if isinstance(one_tool,Tool):   # 如果one_tool为Tool的工具对象
				self.all_tools.remove(one_tool)
			else:   # 为工具名称字符串
				for index,item in enumerate(self.all_tools):
					if one_tool == item.name:   # 当前遍历的工具名称为one_tool
						self.all_tools.pop(index)
						break   # 删除之后，退出循环
		else:
			print("工具不存在，无法删除！")

	def search(self,one_tool):
		"""
		根据工具对象或者工具名称查找工具
		:param one_tool:Tool工具对象或者工具名
		:return:
		"""
		if self.has_tool(one_tool):
			if isinstance(one_tool,Tool):   # 如果one_tool为Tool的工具对象
				one_tool.describe_tool()
			else:   # 为工具名称字符串
				for index,item in enumerate(self.all_tools):
					if one_tool == item.name:   # 当前遍历的工具名称为one_tool
						self.all_tools[index].describe_tool()
						break  # 找到工具之后，退出循环
		else:
			print("工具不存在！")

	@classmethod
	def modify_tool_count(cls):
		"""
		类方法，每调一次工具总数加一
		:return:
		"""
		cls.tools_count += 1

	@classmethod
	def get_tool_count(cls):
		"""
		类方法，获取工具箱中，工具总数
		:return:
		"""
		return cls.tools_count

hammer = Tool("锤子","由金属或木头等材料做成的头和与之垂直的柄构成的敲击工具",25.2)
screwdriver = Tool("螺丝刀","是一种用来拧螺丝以使其就位的工具",35)
saw = Tool("锯子","用来把木料或者其他材料割开的工具",12)
electric_drill = Tool("电钻","利用电做动力的钻孔工具",278)

family_tool_package = ToolPackage("家用工具箱")
# 将工具添加到工具箱中
family_tool_package.add(hammer)
family_tool_package.add(screwdriver)

# 删除一个不存在的工具
family_tool_package.remove(saw)
# 按照工具名称来删除一个工具
family_tool_package.remove("锤子")

# 再次添加工具
family_tool_package.add(electric_drill)

# 查询工具
family_tool_package.search(saw)   # 查询不存在的工具
family_tool_package.search(screwdriver)   # 查询已存在的工具
family_tool_package.search("电钻")   # 通过工具名称来查询工具

# 获取工具总数
print("{}中现在有【{}】件工具".format(family_tool_package.name,family_tool_package.get_tool_count()))