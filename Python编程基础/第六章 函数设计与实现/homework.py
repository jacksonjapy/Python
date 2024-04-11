"""
Write By Jackson
"""

# 1.定义函数：is_num(s),判断输入的数据是否整数。
def is_num(s):
    if s.isdigit():
        return True
    else:
        return False

# 2.定义函数 count(s) ,统计字符串中小写字母、大写字母、数字的个数，并以字典为结果返回给调用函数。
def conut(s):
    count_dict = {'小写字母': 0, '大写字母': 0, '数字': 0, '其他字符': 0}
    for i in s:
        if i.islower():
            count_dict['小写字母'] = count_dict.get('小写字母', 0) + 1
        elif i.isupper():
            count_dict['大写字母'] = count_dict.get('大写字母', 0) + 1
        elif i.isdigit():
            count_dict['数字'] = count_dict.get('数字', 0) + 1
        else:
            count_dict['其他字符'] = count_dict.get('其他字符', 0) + 1
    return count_dict
# 3.定义一个递归函数求阶乘，传入一个参数n，返回n的阶乘。
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''4.定义函数:taxRate(income,deduction) ,根据月收入和扣除额的不同,输出税后月工资、税额和税率。
假如：应纳税所得额=月度收入-5000元（起征点）-所有其他扣除额;税额=应纳税所得额*个人所得税税率;税后工资=月度收入-税额
个人所得税税率标准：
全年应纳税所得额税率          （%）
不超过36000元的	            3
超过36000元至144000元的部分	10
超过144000元至300000元的部分	20
超过300000元至420000元的部分	25
超过420000元至660000元的部分	30
超过660000元至960000元的部分	35
超过960000元的部分	45
例如：月收入为10000元，所有其他扣除2000元，则：应纳税所得额=10000-5000-2000=3000;税率=3% （3000*12=36000,全年应纳税所得额为36000，因此税率为3%）;税额=3000*3%=90;税后工资=10000-90=9910
请从键盘输入月收入和所有其他扣除，调用taxRate(income)函数计算其税后工资、税额，最后输出对应的税后工资、税额和税率。'''
def taxRate(income, deduction):
    # 定义税率和应纳税所得额的阈值
    tax_brackets = [(36000, 0.03), (144000, 0.1), (300000, 0.2), (420000, 0.25), (660000, 0.3), (960000, 0.35),(float('inf'), 0.45)]
    # 计算应纳税所得额
    taxable_income = (income - 5000 - deduction) * 12
    # 计算税额和税率
    tax = 0
    for bracket in tax_brackets:
        if taxable_income <= bracket[0]:
            tax = taxable_income * bracket[1]
            tax_rate = bracket[1]
            break
        else:
            taxable_income -= bracket[0]
    # 计算税后工资
    after_tax_income = income - tax / 12
    return after_tax_income, tax / 12, tax_rate


if __name__ == '__main__':
    # 第一题
    # while is_num:
    #     one = input('请输入一个整数：')
    #     if is_num(one):
    #         print('输入的整数为：', one)
    #         break
    #     else:
    #         print('输入的不是一个整数，请重新输入')
    # 第二题
    # count_dict = conut(input("please input a string:"))
    # for key, value in count_dict.items():
    #     print(key, ':', value)
    # 第三题
    # print(factorial(int(input('请输入一个整数：'))))
    # 第四题
    income = float(input("请输入您的月收入："))
    deduction = float(input("请输入您的所有其他扣除："))
    after_tax_income, tax, tax_rate = taxRate(income, deduction)
    print("税后工资：", after_tax_income)
    print("税额：", tax)
    print("税率：", tax_rate)

