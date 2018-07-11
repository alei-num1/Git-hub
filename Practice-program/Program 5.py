# 输入三个整数x,y,z，请把这三个数由小到大输出 (以后遇见排序的列表最好用了)

# 想法一
# tmp_list = []
# for i in range(3):
#     num = int(input("请输入数字:"))
#     tmp_list.append(num)
# tmp_list.sort()
# print(tmp_list)


# 想法二
while True:
    try:
        a = int(input("请输入第一个整数: "))
        b = int(input("请输入第二个整数: "))
        c = int(input("请输入第三个整数: "))
        tmp_list = [a, b, c]
        print(sorted(tmp_list))
        break
    except TypeError:
        print("请输入整数")
