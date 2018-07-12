# 1-1-3
# 1：a = 'pyer',b = 'apple'用字典和format方法实现：my name is pyer, i love apple.
# a = 'pyer'
# b = 'apple'
# print('My name is {}, I love {}.'.format(a, b))
#
# info = {}
# info['a'] = 'pyer'
# info['b'] = 'apple'
# print(info)


# 2:打开文件info.txt,并且写入500这个数字。
with open('info.txt', 'w') as file:
    file.write('500')
