if __name__ == '__main__':
    # outside_list = []
    # #原始方法
    # for i in range(4): #控制子列表的下标
    #     inside_list = []
    #     for j in range(5): #控制子列表元素的下标
    #         inside_list.append(i + j)
    #     outside_list.append(inside_list)
    # print(outside_list)
    #
    # #推导式
    # a = [[i + j for j in range(5)] for i in range(4)]
    # print(a)

    str1 = "千山鸟飞绝"
    str2 = "万径人踪灭"
    str3 = "孤舟蓑笠翁"
    str4 = "独钓寒江雪"
    new_list = [list(str1), list(str2), list(str3), list(str4)]
    # print(new_list)
    # 横向输出
    for i in range(4):
        for j in range(5):
            print(new_list[i][j],end="")
        print()
    print()
    # 纵向输出
    for j in range(5):
        for i in range(4):
            print(new_list[i][j],end="")
        print()
    print()
    #倒着输出
    for j in range(5):
        for i in range(3,-1,-1):
            print(new_list[i][j],end="")
        print()