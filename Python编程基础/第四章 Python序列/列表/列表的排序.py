if __name__ == '__main__':
    grade = [98,99,97,100,100,96,94,89,95,100]
    #数字升序
    # grade.sort() #括号内两个参数默认为按数字排序和升序
    # print(grade)
    #数字降序
    # grade.sort(reverse=True)  # 括号内两个参数默认为按数字排序和升序
    # print(grade)
    #字典升序
    grade.sort(key=lambda x:str(x))
    print(grade)