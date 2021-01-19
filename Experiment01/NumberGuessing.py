# Using the random module the computer “thinks” about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer tells
# if this was bigger or smaller than the number it generated, or if was the same.
# The game ends after just one guess.
# 使用随机模块，计算机可以“思考”一个介于1到20之间的整数。用户必须猜测这个数字。
# 在用户输入猜测后，计算机会告诉它是大于还是小于它生成的数字，或者是否相同。猜一猜，游戏就结束了。
import random

def guessNumber(x):
    random_x = random.randint(1,20)  # 生成的随机数n: 1 <= n <= 20
    if x == random_x:
        print("猜对了！")
    elif x > random_x:
        print("猜的过大！")
    elif x < random_x:
        print("猜的过小！")

print("猜测一个[1, 20]的整数")
x = int(input("输入猜测:"))
guessNumber(x)
