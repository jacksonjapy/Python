if __name__ == '__main__':
    # 1）创建一个集合，其元素值分别为"张三"、"李四"、"王五"、"赵六"。
    newset = {"张三", "李四", "王五", "赵六"}
    # 2）将自己的真实姓名作为元素添加到创建的集合中。
    newname = "姜美恒"
    newset.add(newname)
    print(newset)
    # 3）删除集合中的元素"赵四"。
    rmname = "赵四"
    if rmname in newset:
        newset.remove(rmname)
    print(newset)

    '''IEEE榜排名前五的语言是：Python，Java，C，C++，JavaScript。
    TIOBE榜排名前五的语言分别是：Python、C、Java、C++、C。
    分别用集合的方式保存排序，且请用集合编程的方式解决如下问题：'''

    # 1）列出上榜的所有语言。
    IEEEset = {"Python", "Java", "C", "C++", "JavaScript"}
    TIOBEset = {"Python", "C", "Java", "C++", "C"}
    print(IEEEset | TIOBEset)
    print(IEEEset.intersection(TIOBEset))
    # 2）列出两个榜单中同时出现的语言。
    print(IEEEset & TIOBEset)
    # 3）列出只在IEEE榜中出现的语言。
    print(IEEEset - TIOBEset)
    # 4）列出只在一个榜中出现的语言。
    print(TIOBEset ^ IEEEset)