"""
Write By Jackson
"""

import time
import os


if __name__ == '__main__':
    path = r"test.txt"
    with open(path, "r", encoding="utf-8") as f:
        # 方法一：read()
        # s = f.read()
        # print(s)
        # 方法二：readline()
        # while True: # 第一种
        #     line = f.readline()
        #     if not line:  # 判断是否到达文件末尾
        #         break
        #     # if line == "":
        #     #     break
        #     print(line, end="")
        # for line in f: # 第二种
        #     print(line, end="")  # 每次读取一行
        #     time.sleep(0.5)
        # 方法三：readlines()
        lines = f.readlines()
        print(lines)

