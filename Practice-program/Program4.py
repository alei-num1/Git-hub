# 输入某年某月某日，判断这一天是这一年的第几天？

# 想法一
# year = int(input("请输入年份: "))
# month = int(input("请输入月份: "))
# days = int(input("请输入日期: "))
# month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# sum = days
# for num in range(0, month - 1):
#     sum += month_list[num]
# if month in range(1, 13) and days in range(1, 31) and year % 4 != 0:
#     print("这是今年的第%d天" % sum)
# elif month in range(1, 13) and days in range(1, 31) and (year % 4 == 0 and year % 100 != 0):
#     sum += 1
#     print("这是今年的第%d天" % sum)
# elif month in range(1, 13) and days in range(1, 31) and year % 400 == 0:
#     sum += 1
#     print("这是今年的第%d天" % sum)
# elif month in range(1, 13) and days in range(1, 31) and (year % 4 == 0 and year % 100 == 0):
#     print("这是今年的第%d天" % sum)
# else:
#     print("输入有误")

# 想法二
# year = int(input("请输入年份: "))
# month = int(input("请输入月份: "))
# day = int(input("请输入日期: "))
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 <= month <= 12:
#     sum = months[month - 1]
# else:
#     print('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print('it is the %dth day.' % sum)

# 方法三
# year = int(input("请输入年份: "))
# month = int(input("请输入月份: "))
# day = int(input("请输入日期: "))
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# now = sum(days[0:month-1]) + day
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     days[1] += 1
#     print("这是今年的第%d天" % now)
# elif year % 4 != 0:
#     days[1] += 0
#     print("这是今年的第%d天" % now)
# else:
#     print("输入有误")


# 想法四

# year = int(input("请输入年份: "))
# month = int(input("请输入月份: "))
# day = int(input("请输入日期: "))
# month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# d = 0
#
# if 0 < month <= 12:
#     if 0 < day <= 31:
#         d = d + day
#         if month > 2:
#             if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#                 d = d + 1
#         for i in range(12):
#             if (i + 1) < month:
#                 d = d + month_list[i]
#                 i = i + 1
#
#         print(d)
#     else:
#         print('输入的日期有错误')
# else:
#     print('输入的月份有错误')


# 想法五
import time
number = input("请输入时间格式为(1990-09-24): ")
print(time.strptime(number, '%Y-%m-%d')[7])




