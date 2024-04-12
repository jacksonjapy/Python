if __name__ == '__main__':
    # friends = ['张三', '李四', '王五', '赵六']
    # a = "上课了:" + "@".join(friends)  # 用@符号将列表中的元素连接起来
    # print(a)
    # username = ["MingRi", "mr", "mingrisoft", "wGH", "MRSoft"]
    # while True:
    #     new_username = input("请输入用户名:")
    #     registed = False
    #     for i in username:
    #         if new_username.lower() == i.lower():  # 判断用户名是否存在
    #             registed = True
    #             print("用户名已存在,请重新输入")
    #             break
    #     if not registed:
    #         username.append(new_username)  # 添加用户名
    #         print("用户名已添加")
    #         break
    student = list(map(str,input("请输入姓名:(用逗号分开)").replace(" ","").split(",")))
    print(student)
    # for i,k in enumerate(student):
    #     student[i] = k.strip()
    # print(student)
