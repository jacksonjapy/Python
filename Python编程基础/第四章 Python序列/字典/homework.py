if __name__ == '__main__':
    # 创建一个名为course_score的字典用于存放课程名和对应的成绩，如下所示：
    course_score = {'Python': 96, 'Linux': 99, '计算机网络技术': 90}

    # 1）求字典的长度。
    print(len(course_score))
    # 2）请修改
    # '计算机网络技术'
    # 课程的成绩为98。
    course_score['计算机网络技术'] = 98
    print(course_score)
    # 3）删除
    # "Linux"
    # 课程。
    course_score.pop('Linux')
    print(course_score)
    # 4）增加一门课程，课程名为
    # "路由交换", 成绩为90。
    course_score['路由交换'] = 90
    print(course_score)
    # 5）获取该字典的所有key，存储在名为course_name列表中。
    course_name = course_score.keys()
    print(course_name)
    # 6）获取所有的value值，存储在名为score列表中。
    score = course_score.values()
    print(score)
    # 7）判断
    # "Linux网络管理" 课程是否在字典中。
    if 'Linux网络管理' in course_score:
        print('Yes')
    else:
        print('No')
    # 8）获取字典中最高的成绩。
    max_score = max(course_score.values())
    print(max_score)
    # 9）将字典dic1 = {'php': 97}，将dic1的数据更新到course_score字典中。
    dic1 = {'php': 97}
    course_score.update(dic1)
    print(course_score)
    # 10）使用匿名函数对字典按成绩从高到低排序。
    result = sorted(course_score.items(), key=lambda x: x[1])
    print(result)