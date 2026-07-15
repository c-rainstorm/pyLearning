import math


# 利用面向对象的思想写下面的程序：直接赋值

# 1.小明穿着白色的特步运动鞋在奥林匹克公园跑步
#   Person类
#      属性：name
#      方法：run(self, place, shoes)
class Person:
    name: str
    def __init__(self, name: str):
        self.name = name

    def run(self, place, shoes):
        print(f'{self.name}穿{shoes}在{place}运动')

person = Person("小明")
person.run("奥林匹克公园", "白色的特步运动鞋")

# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
#   Person2类
#      属性：name, pig
#      方法：find_pig(self)

class Person2(Person):
    pig:str
    def __init__(self, name: str, pig: str):
        super().__init__(name)
        self.pig = pig

    def find_pig(self):
        print(f'{self.name}家的宠物猪【{self.pig}】跑丢了，她哭着贴寻猪启示')

person = Person2("王梅", "笨笨")
person.find_pig()

# 3. 定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆类Circle:
#     属性: 半径r,圆心(Point对象)
#     方法: 周长,面积
#
# 点类Point:
#   属性: x,y
#   方法: 与圆的关系(在圆内/在圆外/在圆上)

class Point:
    x: float
    y: float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, point: "Point"):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

class Circle:
    heart:Point
    r: float
    def __init__(self, r: float, heart: Point):
        self.r = r
        self.heart = heart

    def relation(self, point: Point):
        distance = self.heart.distance(point)
        if distance < self.r:
            print("在圆内")
        elif distance > self.r:
            print("在圆外")
        else:
            print("在圆上")

circle = Circle(1, Point(0, 0))
circle.relation(Point(1, 1))
circle.relation(Point(1, 0))
circle.relation(Point(0.5, 0))

# 4. 使用面向对象的思想，创建下面的类，对象
#
#  有一个银行账户类 Account,
#     属性包括: 名字name , 余额balance属性
#    方法有：存钱 save_money(self,money)、
#           取钱 get_money(self,money)、
#           查询余额 show_balance(self)。
#    要求：取钱时，要判断余额是否充足，余额不够的时候要提示余额不足



class Account:
    name:str
    balance:int
    def __init__(self, name: str):
        self.name = name
        self.balance = 0

    def save_money(self, money):
        if money > 0:
            self.balance += money
    def get_money(self, money):
        if money > 0:
            if money > self.balance:
                print("余额不足")
            else:
                self.balance -= money
    def show_balance(self):
        print(f'{self.name}剩余金额{self.balance}')

account = Account("张三")
account.show_balance()
account.save_money(100)
account.get_money(1000)
account.get_money(10)
account.show_balance()