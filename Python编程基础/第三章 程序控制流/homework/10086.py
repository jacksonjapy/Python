import random as ra


if __name__ == '__main__':
    cash = ra.uniform(0,100)
    mobile_data = ra.uniform(0,100)
    call = ra.randint(0,100)
    ver_list = [1, 2, 3, 0]
    quit_sys = False
    print("1:查询当前余额\n2:查询当前剩余流量\n3:查询当前剩余通话\n0:退出自助查询系统！")
    #s = int(input("input the number:"))

    while not quit_sys:
        input_sys = int(input())
        if input_sys not in ver_list:
            print("没有此编号，请重新输入:")
        if input_sys == ver_list[3]:
            print("退出自助查询系统！")
            quit_sys = True
        elif input_sys == ver_list[0]:
            print("当前余额{:.2f}元".format(cash))
        elif input_sys == ver_list[1]:
            print("当前剩余流量{:.2f}G".format(mobile_data))
        elif input_sys == ver_list[2]:
            print(f"当前剩余通话{call}分钟")
