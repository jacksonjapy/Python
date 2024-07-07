# if __name__ == '__main__':
    # phones = ["小米", "华为", "魅族", "中兴"]
    # phones.append("Apple")
    # print(phones)
    # phones = ["小米", "华为", "魅族", "中兴"]
    # phones.insert(0,"Apple")
    # print(phones)


# if __name__ == '__main__':
#     current_list = ["迈克尔·乔丹", "卡里姆·阿布杜尔·贾巴尔"
#         , "哈基姆·奥拉朱旺", "查尔斯·巴克利", "姚明"]
#
#     new_stars = ["贾森·基德", "史蒂夫·纳什", "格兰特·希尔"]
#     current_list.extend(new_stars)
#     print(current_list)


# if __name__ == '__main__':
#     verse = ["长亭外", "古道边", "芳草碧连天"]
#     #将最后一个元素修改为"一行白鹭上青天"
#     verse[2]="一行白鹭上青天" #等价于  verse[-1]="一行白鹭上青天"
#     del(verse[-1]) #等价于 verse.pop() 括号内参数默认为-1
#
#     print(verse)


# if __name__ == '__main__':
#     verse = ["长亭外", "古道边", "芳草碧连天"]
#     if "1" in verse:
#         verse.remove("1")
#     print(verse)


if __name__ == '__main__':
    verse = ["长亭外", "古道边", "芳草碧连天"]
    verse.clear() #del verse会直接删除这个对象,而clear只会清空该对象
    print(verse)