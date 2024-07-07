"""
Write By Jackson
"""

import os

if __name__ == '__main__':
    '''1.data.txt文件中保存的是学生的基本信息，其内容如下所示。
            学号,姓名,电话号码,年龄,性别
            20200008,张三,13032435356,21,男
            20200010,王岚,13038659870,19,女
            20200003,李四,13032867908,20,男
    读取下列字典中的信息，按data.txt文件中的格式以追加写的方式写入data.txt文件。    
            students = {20200201:["赵六",18290456608,20,"男"],
            20200102:["孙七",15212093406,21,"男"]}
            说明：students字典中加一个元素，用于保存自己的真实信息。'''
    # students = {20200201: ["赵六", 18290456608, 20, "男"], # 定义需要追加信息的字典。
    #             20200102: ["孙七", 15212093406, 21, "男"],
    #             22705090: ["姜美恒", 17780412653, 20, "男"]}
    # for key, value in students.items(): # 遍历字典中的每一个元素。
    #     with open("data.txt", "a") as f:
    #         f.write(str(key) + "," + value[0] + "," + str(value[1]) + "," + str(value[2]) + "," + value[3] + "\n")
    '''读取data.txt文件中的内容，将读取出来的数据转换为如上述格式的字典进行保存。
    然后对字典按学号升序排序后再写入当前目录下的new目录下的sort.txt文件中，注意要判断目录是否存在，不存在则先创建。'''
    path = r"new/sort.txt"
    students = {}
    if not os.path.exists("new"):
        os.mkdir("new")
    if os.path.exists("data.txt"):
        with open("data.txt", "r") as f:
            for line in f.readlines():
                line = line.strip().split(",")
                students[str(line[0])] = [line[1], str(line[2]), str(line[3]), line[4]]
    else:
        print("该文件不存在")
    del(students["学号"])
    with open(path, "w") as g:
        for key, value in sorted(students.items()):
            g.write(str(key) + "," + value[0] + "," + str(value[1]) + "," + str(value[2]) + "," + value[3] + "\n")
