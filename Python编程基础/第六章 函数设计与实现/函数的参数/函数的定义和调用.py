# Write By Jackson Ja
# 方法一
# from test_package import info_precess
#
# if __name__ == '__main__':
#     s = "函数的设计与使用"
#     info_precess.print_precess(s)

# 方法二
# import test_package.info_precess
#
# if __name__ == '__main__':
#     s = "函数的设计与使用"
#     test_package.info_precess.print_precess(s)

# 方法三
# from test_package import *
#
# if __name__ == '__main__':
#     s = "函数的设计与使用"
#     info_precess.print_precess(s)
def print_info(student_dict, key):
    if key in student_dict:
        print(student_dict[key])
    else:
        print("error,please retry!")

def print_info1(info):
    print(f"{'姓名':^5}{'学号':^10}{'性别':^3}{'年龄':^5}")
    for key, value in info.items():
        print(f"{value[0]:^5}{key:^10}{value[1]:^3}{value[2]:^5}")

def function_bmi(weight, height, name): # def关键字定义函数，括号内为函数参数（形参），括号外为函数体
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("过轻", end="\t")
    elif bmi < 24:
        print("正常", end="\t")
    elif bmi < 28:
        print("超重", end="\t")
    else:
        print("肥胖", end="\t")
    print(f"{name}的BMI是{bmi:.2f}")


if __name__ == '__main__':
    # student_dict = {
    #     10001: ["张三"],
    #     10002: ["李四"],
    #     10003: ["王五"],
    #     10004: ["赵六"]
    # }
    # user_input = int(input("please input sid:"))
    # print_info1(student_dict, user_input)
    # input("please input your weight, height, name(split by ','):").split(",")
    # students = {20200001: ["张三", "男", 20],
    #             20200003: ["李四", "男", 19],
    #             20200007: ["王敏", "女", 19]}
    # print_info1(students)
    input_list = input("please input your weight(kg), height(m), name(split by ','):").split(",")
    function_bmi(float(input_list[0]), float(input_list[1]), input_list[2]) # 调用函数时实参的顺序要与函数定义时的顺序一致（按位置参数传值）
    function_bmi(weight=float(input_list[0]), height=float(input_list[1]), name=input_list[2]) # 调用函数时实参的顺序可以与函数定义时的顺序不一致（按关键字参数传值）