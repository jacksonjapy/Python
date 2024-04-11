if __name__ == '__main__':
    dic = {"张三": "天蝎座", "李四": "射手座", "王五": "天秤座"}
    # name = "张三"
    # if name in dic:
    #     print(f"{name}的星座为:{dic[name]}")
    # else:
    #     print("查无此人！")
    #get()方法
    name = "张四"
    print(f"{name}的星座为:{dic.get(name,'查无此人！')}")