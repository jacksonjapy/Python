"""
Write By Jackson
"""


def f(n):
    if n == 1:  # 退出条件
        return 1
    else:
        return n + f(n - 1)


if __name__ == '__main__':
    n = int(input('请输入一个整数：'))
    result = f(n)
    print(f"和为{result}")
