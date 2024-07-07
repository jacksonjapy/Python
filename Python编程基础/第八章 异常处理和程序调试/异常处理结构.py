"""
Write By Jackson
"""


if __name__ == '__main__':
    try:
        nums = input("请输入两个数,计算其商：").split()
        if len(nums) == 2:
            a, b = map(float, nums)
        else:
            print("输入数据的个数有误，请重新输入：")
            exit()
    except ValueError:
        print("输入类型有误，请重新输入")
        exit()

    try:
        c = a / b
    except ZeroDivisionError:
        print("除数不能为0，请重新输入")
        exit()

    print(f"结果为：{c}")
