# 判断101-200之间有多少个素数，并输出所有素数。

# 想法一
count = 0
leap = 1
from math import sqrt

for m in range(101, 201):
    k = int(sqrt(m))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        count += 1
        print("%d" % m)
    leap = 1
print("There are %d numbers that meet the requirements."%count)
