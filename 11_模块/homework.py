import json
import os
from sys import stdout

from mytest import sort

l = [1,2,6,3,7,8,3]

after_sort1 = sort.sort1(l)
print(l)
print(after_sort1)

after_sort2 = sort.sort2(l)
print(after_sort2)

print(sort.find_index(l, 3))

class PersonInfo:
    name:str
    idCard: str
    sex: str
    birthday: str
    address:str
    postcode: str
    phone: str
    phone2: str
    phone3: str
    email: str
    any:str
    def __init__(self, info:str):
#        曹阳,32010619720506042x,F,19720506,-,210005,13770848687,025-842019149,-,cy_qing@163.com,0
        infos = info.split(',')
        self.name = infos[0]
        self.idCard = infos[1]
        self.sex = infos[2]
        self.birthday = infos[3]
        self.address = infos[4]
        self.postcode = infos[5]
        self.phone = infos[6]
        self.phone2 = infos[7]
        self.phone3 = infos[8]
        self.email = infos[9]
        self.any = infos[10]


    def to_dict(self):
        # 手动指定要导出的字段，过滤敏感内容
        return self.__dict__

def grep_info_by_name(name: str) -> PersonInfo|None :
    with open('kaifanglist.txt', 'r', encoding='utf-8') as __fp:
        while True:
            line = __fp.readline()
            if not line:
                break
            __person = PersonInfo(line)
            if __person.name == name:
                return __person
        return None

# 2. 开房查询
# 	创建函数，传入一个名字，查找到这哥们的开房记录，
#       然后把身份证号码和地址取出来，写入到以这哥们名字为名的txt文件中 如：张三.txt


person = grep_info_by_name("徐争鸣")
if person:
    json.dump(person.__dict__, stdout, ensure_ascii=False)
    os.makedirs("output", exist_ok=True)
    with open("output/" + person.name + '.txt', 'w', encoding='utf-8') as fp:
        fp.write(person.idCard)
        fp.write(',')
        fp.write(person.address)

