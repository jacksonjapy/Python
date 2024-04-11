import random


if __name__ == '__main__':
    #原始方法
    # newlist = []
    # while True:
    #     for i in range(10):
    #         newlist.append(random.randint(10,100))
    #     print(newlist)
    #     break
    #推导式
    newlist = [random.randint(10,100) for i in range(10)]