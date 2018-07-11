# 方法一
# file_path = 'C:\\Users\\guzhu\\PycharmProjects\\01.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)
# 方法二
# file_path = r'C:\Users\guzhu\PycharmProjects\01.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# 方法三
file_path = r'C:/Users/guzhu/PycharmProjects/01.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
    # contents = file_object.read()
    # print(contents)
for line in lines:
    print(line.rstrip())


