if __name__ == '__main__':
    student = {20200008: ['张三', 13032435356, 21, '男'],
               20200010: ['王岚', 13038659870, 19, '女'],
               20200003: ['李四', 13032867908, 20, '男']}
    # 根据键对字典进行排序
    result = sorted(student.items())
    print("按学号排序：")
    print("-" * 50)
    print(f"{'学号':^8}{'姓名':^8}{'电话':^10}{'年龄':^9}{'性别':^9}")
    print("-" * 50)
    for info in result:
        print(f"{info[0]:^9}{info[1][0]:^9}{info[1][1]:^9}{info[1][2]:^9}{info[1][3]:^9}")
    print()
    # 按年龄对字典进行排序
    result = sorted(student.items(), key=lambda x: x[1][2])
    print("按年龄排序：")
    print("-" * 50)
    print(f"{'学号':^8}{'姓名':^8}{'电话':^10}{'年龄':^9}{'性别':^9}")
    print("-" * 50)
    for info in result:
        print(f"{info[0]:^9}{info[1][0]:^9}{info[1][1]:^9}{info[1][2]:^9}{info[1][3]:^9}")