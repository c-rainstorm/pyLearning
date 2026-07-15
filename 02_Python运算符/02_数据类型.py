# 数据类型：
#   int, float【数字类型：整型int，浮点型[小数]float，复数类型complex 】， 如： 100,  3.14
# 	str【字符串】， 如："hello",  '张三'
# 	bool【布尔类型】：  True真（1）， Flase假（0）
# 	NoneType【空值】 : None
#
# 	list【列表】 类似c语言的数组array， 如： [1, 2, 3]
# 	tuple【元组】 不可改变的列表,  如： (1, 2, 3)
# 	dict【字典】由键值对组成的，如： {"name": "张三",  "age": 30}
# 	set【集合】(了解) ，如： {1, 2, 3}
# 	bytes【字节】二进制， 如：b'hello'


a = 100
print(a, type(a))

a = 3.14
print(a, type(a))

a = "张三"
print(a, type(a))

a = True
print(a, type(a), int(a))

a = False
print(a, type(a), int(a))

a = None
print(a, type(a))

a = [1,1,2,2,3,3]
print(a, type(a))

a.append(4)
print(a, type(a))

a = (1,1,2,2,3,3)
print(a, type(a))

a = {"name": 'ikun', "like": '篮球', "age": 22}
print(a, type(a))

a = b'hello'
print(a, type(a))  # b'hello' <class 'bytes'>

