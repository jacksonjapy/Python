if __name__ == '__main__':
    price = [1200, 5330, 2988, 6200, 1998, 8888]
    #原始方法
    # discount_price = []
    # for i in price:
    #     discount_price.append(i * 0.5)
    # print(discount_price)
    #推导式
    discount_price = [i * 0.5 for i in price]
    print(discount_price)