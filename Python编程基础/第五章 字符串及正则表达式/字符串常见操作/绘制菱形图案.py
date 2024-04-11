if __name__ == '__main__':

    #方法一
    # rows = int(input("请输入菱形的大小:"))
    # for i in range(1, rows + 1):
    #     star = i * 2 - 1
    #     result = (rows - i) * " "
    #     print(result + "*" * star)
    #
    # for i in range(rows - 1, 0, -1):
    #     star = i * 2 - 1
    #     result = (rows - i) * " "
    #     print(result + "*" * star)
    n = int(input("请输入菱形的大小:"))

    #方法二
    # for i in range(1, n + 1):
    #     result = "*" * (i * 2 - 1)
    #     print(result.center(n * 2 - 1))
    #
    # for i in range(n - 1, 0, -1):
    #     result = "*" * (i * 2 - 1)
    #     print(result.center(n * 2 - 1))

    #方法三
    for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
        result = "*" * (i * 2 - 1)
        print(result.center(n * 2 - 1))