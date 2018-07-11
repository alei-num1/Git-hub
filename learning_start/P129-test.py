# # 8-9
# # 1 创建列表
# magicians = ['Mr.xue', 'Miss lei', 'baby1', 'baby2']
#
#
# # 2 定义函数
# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)
#
#
# # 3 调用函数,打印
# show_magicians(magicians)


# 8-10
magicians = ['Mr.xue', 'Miss lei', 'baby1', 'baby2']
great_magicians = []


def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magician = 'the great ' + magician
        great_magicians.append(great_magician)
#         # print(magician)


# def make_great(magicians, great_magicians):
#     for magician in magicians:
#         great_magician = 'the great ' + magician
#         great_magicians.append(great_magician)
#         # print(magician)


def show_magicians(great_magicians):
    for name in great_magicians:
        print(name)


make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)

# 8-10
# magicians = ['Mr.xue', 'Miss lei', 'baby1', 'baby2']
# great_magicians = []
#
#
# def make_great(magicians, great_magicians):
#     for magician in magicians:
#         great_magician = 'the great ' + magician
#         great_magicians.append(great_magician)
#
#
# def show_magicians(great_magicians):
#     for name in great_magicians:
#         print(name)
#
#
# make_great(magicians[:], great_magicians)
# show_magicians(great_magicians)
# show_magicians(magicians)

