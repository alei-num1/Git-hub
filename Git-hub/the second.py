# 1-2-1 字符串:a = 'abcd' 用2个方法取出字母d
# plan 1 准变成列表类型
a = 'abcd'
b = list(a)
print(b[-1])

# plan 2 字符串切片
a = 'abcd'
print(a[-1])

# 1-2-2：a = 'jay',b = 'python'用字符串拼接的方法输出：my name is jay,i love python.
a = 'jay'
b = 'python'
print('My name is %s,I love %s.' % (a, b))
