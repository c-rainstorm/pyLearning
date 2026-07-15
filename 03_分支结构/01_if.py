
age = int(input("请输入年龄："))
if age < 18:
    print("未成年人")
elif  age < 30:
    print("年轻人")
elif age < 60:
    print("中年人")
else:
    print("老年人")

print("end")


a = 60
b = 40

c = a if b > a else b
print("c:",c)