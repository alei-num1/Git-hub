# 利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# plan 1
# score = int(input("请输入成绩(0-100之间): "))
# if score >= 90:
#     print("%d A" % score)
# # elif score >= 60 and score <= 89:
# elif 60 <= score <= 89:
#     print("%d B" % score)
# elif score < 60:
#     print("%d C" % score)


# plan 2
def get_score(score):
    if score in range(0, 60):
        return 'C'
    if score in range(60, 90):
        return 'B'
    if score in range(90, 100):
        return 'A'


score = int(input("请输入成绩(0-100之间): "))
print(get_score(score))
