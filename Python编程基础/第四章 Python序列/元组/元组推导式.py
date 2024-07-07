import random as ra


if __name__ == '__main__':
    a = tuple(ra.randint(1, 10) for i in range(10))
    print(a)
