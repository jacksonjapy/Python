"""
Write By Jackson
"""

import os

if __name__ == '__main__':
    # 手动定义path路径
    # path = r"../test9.txt"
    # # 判断path变量指向路径下的文件是否存在并且是否具有相应的权限
    # if not os.path.exists(path) or not os.access(path, os.R_OK):
    #     print("该文件不存在或没有相应的权限！@_@")
    # else:
    #     print("检测到该文件！@_@")
    #     with open(path, 'r') as f:
    #         for line in f:
    #             print(line, end='')
    # 判断目录是否存在，存在则打开该目录，不存在则创建，如果创建成功则显示其绝对路径并打开该目录
    path = r"../test"
    path = os.path.abspath(path)
    os.chdir(path)
    if not os.path.isdir(path):
        os.makedirs(path)
        print("创建成功！@_@")
        os.chdir(path)
        print(os.path.abspath(path))
    else:
        print("目录已存在！@_@")
        print(os.path.abspath(path))
        # 打开目录
        os.chdir(path)
