if __name__ == '__main__':
    dic = {"张三": "天蝎座", "李四": "射手座", "王五": "天秤座"}
    #遍历字典的键和值
    for name, xz in dic.items():
        print(f"姓名：{name}，星座：{xz}")
#只遍历字典的值
if __name__ == '__main__':
    dic = {"张三": "天蝎座", "李四": "射手座", "王五": "天秤座"}
    for xz in dic.values():
        print(f"星座：{xz}")
#只遍历字典的键
if __name__ == '__main__':
    dic = {"张三": "天蝎座", "李四": "射手座", "王五": "天秤座"}
    for name in dic.keys():
        print(f"姓名：{name}")