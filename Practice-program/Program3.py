# 这是一个猜字游戏
import random

guess_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

# 向游戏者询问数字4次
for guess_counts in range(1, 5):
    print("Please take a guess.\n")

    try:
        number = int(input("Please tell me a number: "))
        if number < guess_number:
            print("Your number is lower than guess_number.")
        elif number > guess_number:
            print("Your number is higher than guess_number.")
        else:
            break  # 正确数字
    except ValueError:
        print("The number is error.Please tell me a number again.")
if number == guess_number:
    print("You are right! And you guessed my number in "
          + str(guess_counts) + " guesses!")
else:
    print("Sorry,game over.")

# 这是一个猜字游戏
# import random
#
# guess_number = random.randint(1, 20)
# print("I'm thinking of a number between 1 and 20.")

# # 向游戏者询问数字 直到猜对为止
# # for guess_counts in range(1, 5):
# guess_counts = 0
# while True:
#     print("Please take a guess.\n")
#     guess_counts += 1
#     number = int(input("Please tell me a number: "))
#     if number < guess_number:
#         print("Your number is lower than guess_number.")
#     elif number > guess_number:
#         print("Your number is higher than guess_number.")
#     elif number == guess_number:
#         print("You are right! And you guessed my number in "
#               + str(guess_counts) + " guesses!")
#         break
#     else:
#         print("Sorry,game over.")
