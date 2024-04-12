"""
Write By Jackson
"""


# def printcoffee(*coffee_name):
#     print("本店现有的咖啡有：")
#     for i in coffee_name:
#         print(i,end="\t")
#     print()
#
# if __name__ == '__main__':
#     printcoffee('蓝山')
#     printcoffee('蓝山', '卡布奇诺')
#     printcoffee('蓝山', '卡布奇诺', '曼特宁', '摩卡')
def printsign(**name_sign): # name_sign前加上**表示以字典的形式传入任意个参数
    print(name_sign)

if __name__ == '__main__':
    printsign(张三='双鱼座', 李四='双子座', 王五='射手座')