if __name__ == '__main__':
    # 定义二维列表
    list_2d = [
        ['姓名', '年龄', '性别'],
        ['张三', 20, '男'],
        ['李四', 21, '女'],
        ['王五', 22, '男'],
        ['赵六', 23, '女'],
    ]
    # 格式化输出二维列表
    for item in list_2d:
        print("{0:<6} {1:<5} {2:<6}".format(*item))