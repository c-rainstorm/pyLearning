
# Python算术运算符：
#    +  -  *  /  %  //（整除:向下取整）   **
print("1+2=",1+2)
print("1-2=",1-2)
print("1*2=",1*2)
print("1/2=",1/2)

print("3%2=",3%2)
print("3//2=",3//2)
print("3**2=",3**2)

print("4+5*3**2=",4+5*3**2)

n = 4 + 5 > 3 + 4
print(n)  # True

# 科学计数法

print(3.14e5)
print(3.14e-5)


# 常见内存单位：
# 1b = 0 或 1
# 1B = 8bit
# 1KB = 1024Byte
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB
# ...

num = 123

a = num // 100
b = num // 10 % 10
c = num % 10
print(a,b,c, sep=",")


n = 10
print(5 < n < 20)