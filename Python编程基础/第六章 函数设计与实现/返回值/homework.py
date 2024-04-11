"""
Write By Jackson
"""


# 练习： 定义一个名称为fun_checkout的函数。参数：一个列表，用于保存输入的商品金额。 功能：计算应付金额和实付金额。
# 满500可享受9折优惠、满1000可享受8折优惠、满2000可享受7折优惠、满3000可享受6折优惠。
# 返回值：应付金额和实付金额。 在主程序中通过循环输入多个金额保存到列表中，并调用fun_checkout函数。
def fun_checkout(*price_list):
    sum_payable = 0  # 应付金额
    sum_paid = 0  # 实付金额
    for i in price_list:
        i = float(i)
        sum_payable += i
        if 1000 > i:
            sum_paid += i * 0.9  # 满500，9折优惠
        elif 2000 > i:
            sum_paid += i * 0.8  # 满1000，8折优惠
        elif 3000 > i:
            sum_paid += i * 0.7  # 满2000，7折优惠
        elif i >= 3000:
            sum_paid += i * 0.6  # 满3000，0.6惠
        else:
            sum_paid += i  # 其他情况，直接加上原价
    return float(f"{sum_payable:.2f}"), float(f"{sum_paid:.2f}")


# test_data: 3000;2000;1000;500;100.35


if __name__ == '__main__':
    while True:
        # 输入商品金额
        price_list = input("Please enter the price of each item, separated by a semicolon:").split(";")
        # 计算应付金额和实付金额
        sum_payable, sum_paid = fun_checkout(*price_list)
        # 打印应付金额和实付金额
        print(f"AmountDue：{sum_payable}CNY，OutOfPocketAmount：{sum_paid}CNY")
        # 退出程序
        break
