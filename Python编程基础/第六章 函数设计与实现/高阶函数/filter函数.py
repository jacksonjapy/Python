"""
Write By Jackson
"""


if __name__ == '__main__':
    a = range(1, 101)
    # 找出1-100中平方根为整数的数
    b = filter(lambda x: x ** 0.5 == int(x ** 0.5), a)
    print(list(b))
