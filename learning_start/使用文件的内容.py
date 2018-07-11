file_path = r'C:/Users/guzhu/PycharmProjects/01.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
