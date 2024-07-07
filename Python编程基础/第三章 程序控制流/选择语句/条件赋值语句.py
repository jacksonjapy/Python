import random


if __name__ == '__main__':
    a = random.randint(1,100)
    b = random.randint(1,100)
    # if a > b:
    #     max_num = a
    # else:
    #     max_num = b
    max_num = a if a>b else b
    print(f"{a}、{b}中的最大数是{max_num}")
