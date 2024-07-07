import random

random_number = random.randint(10, 100)  # 生产1~100之间任意一个的整数
guess = False  # 定义一个while语句中用来跳出循环的布尔变量
print("-"*20+"开始游戏"+"-"*20)
print("请输入一个1~100之间的任意一个整数：", end="")

while not guess:
    # 使用try...except语句来处理用户输入的非整数数据
    try:
        user_number = int(input())
    except ValueError:
        print("请输入的数据类型有误，请重新输入:", end="")
        continue
    if user_number < 1 or user_number > 100:
        print("超出范围，请重新输入:", end="")
        continue
    if user_number < random_number:
        print("你猜的数字小了！\n请继续:", end="")
    elif user_number > random_number:
        print("你猜的数字大了！\n请继续:", end="")
    else:
        print("恭喜你，猜对了！")
        print("----------------------游戏结束----------------------")
        guess = True  # 更新跳出循环的变量，防止死循环
