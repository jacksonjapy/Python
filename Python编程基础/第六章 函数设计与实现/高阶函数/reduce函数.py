"""
Write By Jackson
"""
from functools import reduce

def add(x, y):
    return x + y


if __name__ == '__main__':
    number = range(1, 6)
    result = reduce(add, number)
    print(result)
