#if单体
if __name__ == '__main__':
    num = int(input("请输入一个整数："))
    if num % 3 == 2 and num % 5 == 3 and num % 7 ==2:
        print("恭喜你猜对了！")