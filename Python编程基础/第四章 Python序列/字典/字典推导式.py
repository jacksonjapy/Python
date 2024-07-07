if __name__ == '__main__':
    #使用字典推导式生成值为None,键为学号的字典
    student_information = {k:None for k in range(20220001,20220056)}
    print(student_information)