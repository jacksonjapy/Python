"""
Write By Jackson
"""


# 练习：编写一个递归函数fibonacci，输出前n项的斐波那契数列 。
def fibonacci(n):  # 求第n个斐波那契数
    """
    斐波那契数列
    :param n: 第n个
    :return:
    """
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(1, 11):
        fibonacci(i)
        print(fibonacci(i))
