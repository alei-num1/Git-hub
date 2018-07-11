# file_path = r'C:/Users/guzhu/PycharmProjects/guest.txt'
# with open(file_path, 'w') as file_object:
#     while True:
#         str1 = input("Please give a name: ")
#         if str1 == 'q':
#             break
#         file_object.write(str1 + "\n")
#         print("Hello, " + str1)

file_path = r'C:/Users/guzhu/PycharmProjects/guest.txt'
with open(file_path, 'a') as file_object:
    input("Why do you like python?()")
    while True:
        str2 = input("Reason: ")
        if str2 == 'q':
            break
        file_object.write(str2 + "\n")

