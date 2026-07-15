import math
from itertools import count


# 1.封装一个函数 验证一个数是否是回文：str(n)[::-1] == str(n)
#   回文： 颠倒过来 与 自身数据一样的称为回文  例如 111  121  1221 12321
def fn1(n) -> bool:
    return str(n)[::-1] == str(n)

print(fn1("123"))
print(fn1("121"))

# 2.封装一个函数，获取多个数中的最小值，最大值，和，以及平均值
def fn2(*args) -> tuple:
    minValue = math.inf
    maxValue = -math.inf
    sumValue = 0

    for n in args[0]:
        if n > maxValue:
            maxValue = n
        if n < minValue:
            minValue = n
        sumValue += n

    avgValue = sumValue / len(args[0])
    return minValue, maxValue, sumValue, avgValue

print(fn2([1,2,3,4,5]))

# 3.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数
def fn3(*args) -> tuple:
    sumValue = sum(args[0])
    avgValue = sumValue / len(args[0])
    countAboveAvg = 0
    for n in args[0]:
        if n > avgValue:
            countAboveAvg += 1
    return avgValue, countAboveAvg

print(fn3([1,2,3,4,5]))

# 4.封装一个函数，获取所有的水仙花数
#   水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
#   （例如：1^3 + 5^3+ 3^3 = 153）
def isFlourDigit(num: int) -> bool:
    a = num // 100
    b = num % 100 // 10
    c = num % 10
    return num == a**3 + b**3 + c**3

def fn4() -> list:
    result = []
    for num in range(100, 1000):
        if isFlourDigit(num):
            result.append(num)

    return result


print(fn4())