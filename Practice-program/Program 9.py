# 暂停一秒输出
import time

list_a = {1: 'a', 2: 'b'}
for key, value in dict.items(list_a):
    print(key, value)
    time.sleep(1)
