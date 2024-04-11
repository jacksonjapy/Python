if __name__ == '__main__':
    price = [ 1200 , 5330 , 2988 , 6200 , 1998 , 8888 ]
    #原始方法
    # new_list = []
    # for i in price:
    #     if i > 5000:
    #         new_list.append(i)
    # print(new_list)
    #推导式
    new_list = [i for i in price if i > 5000]
    print(new_list)