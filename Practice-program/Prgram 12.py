# 打印出所有的"水仙花数"
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153= 1的三次方＋5的三次方＋3的三次方。
# 注意：兼容 Python2.x 与 Python3.x，Python3.x 取整为 //，而不是 /

# algorithm one
# count = 0
# for num in range(100, 1000):
#     i = num // 100
#     j = num // 10 % 10
#     k = num % 10
#     if num == i ** 3 + j ** 3 + k ** 3:
#         print(num)
#         count += 1
# print(count)

# algorithm two
# from math import pow


list = []
for num in range(100, 1000):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    a = pow(i, 3)
    b = pow(j, 3)
    c = pow(k, 3)
    if num == a + b + c:
        list.append(num)
print(list)

# L = []
# for n in range(100, 1000):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         if n == pow(i, 3) + pow(j, 3) + pow(k, 3):
#             L.append(n)
# print(L)
# print(len(L))
