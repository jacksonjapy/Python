import random as ra


if __name__ == '__main__':
    # 1）随机生成300个0~100的正整数, 并以列表的方式保存，列表名为自己的姓名拼音。
    jiangmeiheng = [ra.randint(0, 100) for i in range(300)]
    # 2）统计前面生成的列表中有多少数为30。
    print(jiangmeiheng.count(30))
    # 3）删除列表的最后一个元素。
    jiangmeiheng.pop() #pop()方法默认删除列表的最后一个元素，所以无需更改pop()内的参数。
    # 4）删除列表中元素为28的所有元素。
    if 28 in jiangmeiheng:
        jiangmeiheng.remove(28)
    # 5）求列表的长度。
    print(len(jiangmeiheng))
    # 6）在列表末尾添加一个数字，数字为学号的后2位。
    jiangmeiheng.append(90)
    # 7）在列表的第22位置添加一个数字，数字为学号的后4位。
    jiangmeiheng.insert(21, 5090)
    # 8）分别求列表的最大值和最小值。
    print(max(jiangmeiheng))
    print(min(jiangmeiheng))
    # 9）修改列表第50位置的元素为888。
    jiangmeiheng[49] = 888
    # 10）判断元素49是否在列表中。
    if 49 in jiangmeiheng:
        print('yes')
    else:
        print('no')
    # 11）将[22, 33, 44]合并（extend操作）到列表的最后。
    new_list = [22, 33, 44]
    jiangmeiheng.extend(new_list)
    # 12）颠倒列表中元素的顺序。
    jiangmeiheng.reverse()
    # 13）对颠倒后的列表元素按降序排列。
    jiangmeiheng.sort(reverse=True)
    # 14）求排序后列表的和。
    print(sum(jiangmeiheng))
