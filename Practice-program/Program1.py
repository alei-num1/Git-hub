# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？共有多少个？
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)
                count += 1
print("符合要求的数共有:" + str(count) + "个。")
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
#           组成所有的排列后再去掉不满足条件的排列。
#           定义一个数 用来计算一共输出多少个
