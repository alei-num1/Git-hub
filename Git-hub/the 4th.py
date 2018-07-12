# 一.已经字符串 s = "i,am,li_lei",请用两种办法取出之间的“am”字符。

# plan 1
# s = "i,am,li_lei"
# print(s[2:4])
# tem = list(s)
# print(tem)

# plan 2
s = "i,am,li_lei"
list1 = s.split(',')
# print(type(list1))
print(list1[1])

# 二.在python中，如何修改字符串？




