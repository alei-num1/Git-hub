# 基本数据类型
# 1-1-1
info = 'abc'
info[2] = 'd'
# 结果是什么，为什么会报错呢?
# 答：字符串属于不可变类型，想通过下标修改所以会报错

# 1-1-2
# 如果要把上面的字符串info里面的c替换成d，要怎么操作呢？
info = 'abc'
tem = list(info)
# print(type(info))
# print(type(tem))
tem[2] = 'd'
print(tem)

# 1-1-3
# 下面2个变量
# a = '1'
# b = 2
# print (a + b) 的结果是什么?
# 为什么会出现这个结果，如果希望结果是3，要怎么操作？

# 答：报错。
a = '1'
b = 2
print(int(a) + b)
