if __name__ == '__main__':
    postal_code = dict(成都=610000, 自贡=643000, 绵阳=621000, 广元=628000)
    print(postal_code)
    # d = dict(1="first") # 错误的写法，赋值运算符前的变量名不能用数字开头
    postal_code = dict([('成都', 610000), ('自贡', 643000)])
    print(postal_code)
    # 使用dict()函数和zip()函数创建字典
    city = ["成都", "自贡", "绵阳", "广元"]
    code = [610000, 643000, 621000, 628000]
    k = dict(zip(city, code))
    print(k)
    student_informations = dict.fromkeys(range(20220001, 20220056))
    print(student_informations)