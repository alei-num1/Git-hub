# 打印乘法表
# 方法一
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = j * i
#         if i >= j:
#             print('%s * %s = %s\t ' % (j, i, result), end='')
#     print()

#  方法二
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print('%s * %s = %s  ' % (j, i, result), end='')
#         if j >= i:
#             break
#     print()

# 方法三
for i in range(1, 10):
    for j in range(1, i + 1):
        result = j * i
        print("%s * %s = %s\t" % (j, i, result), end="")
    print()
