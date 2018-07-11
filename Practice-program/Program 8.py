# 将一个列表的数据复制到另一个列表中

# 想法一
# list_a = [i for i in range(10)]
# # print(list_a)
# list_b = list_a[:]
# print(list_b)

# 想法二
# list_a = [i for i in range(10)]
# b = list_a.copy()
# print(b)

# 想法三
# list_a = [i for i in range(10)]
# print(len(list_a))
# list_b = []
# for i in range(len(list_a)):  # 使用for循环出列表元素
#     list_b.append(list_a[i])  # 逐以放到新的列表
# print(list_b)

# 想法四
# list_a = [i for i in range(10)]
# list_b = [j for j in list_a]
# print(list_b)

# 想法五
import copy

a = [1, 2, 3, 4, 5]
b = ["A", "B", a]  # 浅拷贝

c = b[:]
print(c)  # ['A', 'B', [1, 2, 3, 4, 5]]

a[0] = 11
print(c)  # ['A', 'B', [11, 2, 3, 4, 5]] # 此时a变化c跟着变化

# 深拷贝
c = copy.deepcopy(b)
print(c)  # ['A', 'B', [11, 2, 3, 4, 5]]

a[0] = 111
print(a)  # [111, 2, 3, 4, 5]

print(c)  # ['A', 'B', [11, 2, 3, 4, 5]] 此时c中数据不受a影响
