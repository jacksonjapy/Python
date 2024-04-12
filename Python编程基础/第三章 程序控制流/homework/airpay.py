import random as ra

# if __name__ == '__main__':
#     sum_num = 0
#     work = 2
#     Living_expenses = 10
#     offline_payment = 5
#     online_ticketing = 5
#     shared_bike = 10
#     quit_fun = True
#
#     while quit_fun:
#         if input("行为:") == "步行":
#             sum_num = work + sum_num
#             print(f"本次积分{work}")
#         elif input("行为：") == "生活缴费":
#             sum_num = Living_expenses + sum_num
#             print(f"本次积分{Living_expenses}")
#         elif input("行为：") == "线下支付":
#             sum_num = offline_payment + sum_num
#             print(f"本次积分{offline_payment}")
#         elif input("行为：") == "网络购票":
#             sum_num = online_ticketing + sum_num
#             print(f"本次积分{online_ticketing}")
#         elif input("行为：") == "共享单车":
#             sum_num = shared_bike + sum_num
#             print(f"本次积分{shared_bike}")
#         elif input("行为:") == "退出":
#             print()
#             break
#         else:
#             quit_fun
if __name__ == '__main__':
    sum_dict = {"步行": 2, "生活缴费": 10, "线下支付": 5, "网络购票": 5, "共享单车": 10}
    sum_num = ra.randint(0, 100)
    quit_fun = False

    print(f"初始积分为{sum_num}")
    while True:
        input_str = input("行为:")
        if input_str in sum_dict:
            print(f"本次积分{sum_dict[input_str]}")
            sum_num = sum_dict[input_str] + sum_num
        elif input_str == "退出":
            print(f"总积分是{sum_num}")
            break
        elif input_str not in sum_dict:
            print("输入错误，请重新输入:")
