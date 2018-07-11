# 斐波那契数列 (呜呜呜)
# F(0) = 0 (n = 0)
# F(1) = 1 (n = 1)
# F(n) = F[n-1] + F[n-2] (n >= 2)

# 想法一（参考）


# def fib(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     fibs = [1, 1]
#     for i in range(2, n):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs
#
#
# # 输出前 10 个斐波那契数列
# print(fib(10))


# 斐波那契数列 (呜呜呜)
# F(0) = 1 (n = 0)
# F(1) = 1 (n = 1 )
# F(n) = F[n-1] + F[n-2] (n >= 2)

# 想法二
def fib(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


print(fib(10))
