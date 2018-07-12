# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


# 参考答案 能实现 但不完善
# 首先输入数字，用了一个while循环进入，里面通过嵌套一个while循环来进入分解因数，通过for循环
# 从2 遍历，if判断输出的内容
# x = int(input("是否进入循环？是：1， 否：0\n"))
# while x:
#     n = int(input("请输入一个正整数："))
#     print("%d = " % n, end='')
#
#     while n not in [1]:
#         for i in range(2, n + 1):
#
#             if n % i == 0:
#                 n = int(n / i)
#
#                 if n == 1:
#                     print("%d " % i, end='')
#                 else:
#                     print("%d * " % i, end='')
#                 break
#
#     print()
#     x = int(input("是否进入循环？是：1， 否：0\n"))


# 想法  目的：将一个正整数分解质因数  输入一个正整数进行判断，用.isdight 判断是不是字符串，再通过.join将先前方法的列表种质因数连接。
# 定义了一个方法，讲求得的每个质因数数存在列表里
def prime(n):
    list = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                list.append(i)
                break
    return list


s = input("输入一个正整数:")
# print(type(s))
if s.isdigit() and int(s) > 0:
    print(s, "=", "*".join([str(x) for x in prime(int(s))]))
else:
    print("请输入正确的正整数")


# plan 3
n = int(input("请输入要分解的正整数："))

temp = []
list = [j for j in range(2, n + 1)]
while n != 1:
    for i in list:
        if n % i == 0:
            temp.append(i)
            n = n / i
            break
print(temp)
