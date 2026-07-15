# 1.实现万年历效果图，使用函数封装:
#   A:先输出提示语句，并接受用户输入的年、月。
#   B:根据用户输入的年，先判断是否是闰年。
#   C:根据用户输入的月来判断月的天数。
#   D:用循环计算用户输入的年份距1900年1月1日的总天数。
#   E:用循环计算用户输入的月份距输入的年份的1月1日共有多少天,
#   F:相加D与E的天数，得到总天数。
#   G:用总天数来计算输入月的第一天的星期数
#   H:根据G的值，格式化输出这个月的日历!
from unittest import case

def is_leap_year(year: int) -> bool:
    return year % 4 == 0

def days_in_month(year: int, month: int) -> int:
    match month:
        case 1 | 3| 5|7|8|10|12 :
            return 31
        case 2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        case _:
            return 30

def total_days_after_epoch_day(year: int, month: int) -> int:
    total = 0
    for y in range(1900, year):
        if is_leap_year(y):
            total += 366
        else:
            total += 365
    for m in range(1, month):
        total += days_in_month(year, m)
    return total

def first_weekday(total: int) -> int:
    return total % 7

def print_calendar(year: int, month: int) -> None:
    total_days = total_days_after_epoch_day(year, month)
    weekday = first_weekday(total_days)
    days = days_in_month(year, month)
    print("一\t二\t三\t四\t五\t六\t日\t")
    calendar_total = weekday + days - 1
    line = ""
    for i in range(1, calendar_total+1) :
        if i < weekday:
            line += "\t"
        else:
            line += str(i - weekday + 1) + "\t"
        if i > 0 and i % 7 == 0:
            print(line)
            line = ""
    print(line)

print_calendar(2026, 7)

# 2.请写一个生成器函数,生成一个无限序列,从1开始可以不断往后取值,每次+1
#    提示:使用while True, 通过调用n次next来获取前n个数

def generator():
    i = 1
    while True:
        yield i
        i += 1

generator = generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))