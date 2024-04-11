import random as ra


if __name__ == '__main__':

# 1）创建一个元组，共10个元素，分别1,2,3,...,10，并将其保存到tup1变量，然后输出tup1的值。
    tup1 = tuple(range(1, 11))
# 2）创建一个元组，共2个元素，分别自己的姓和名的拼音，如（"zhang"，"san"）,并将其保存到变量tup2，然后输出tup2的值。
    tup2 = ("jiang","meiheng")
# 3）创建一个元组，里面包含1到50之间的所有奇数，并将其保存到变量tup3。
    tup3 = tuple(i for i in range(1, 51) if i % 2!= 0)
# 4）输出tup3元组的中的第10个元素。
    print(tup3[10])
# 5）输出tup3元组的中的第11到15位的元素。
    print(tup3[11:15])
# 6）输出tup3元组的中的后8位元素。
    print(tup3[-1:-8:-1])
# 7）将tup3元组的中的后10位保存到tup4变量。
    tup4 = tup3[-10:]
    print(tup4)