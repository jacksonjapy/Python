'''
Write By Jackson
'''
def function_bmi(weight, height, name="路人甲"): # def关键字定义函数，括号内为函数参数（形参），括号外为函数体。 带有默认值的参数只能放在参数列表的最后。
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
    function_bmi(76, 1.85) # 调用函数,不指定形参，默认使用默认值。
    function_bmi(77,1.76, "ikun") # 调用函数，指定形参。