"""
Write By Jackson
"""

import time


if __name__ == '__main__':
    # date = time.strftime('%Y-%m-%d %H:%M:%S')
    # learning = "文件读写！\n"
    # path = r"test.txt"
    # with open(path, "w", encoding="utf-8") as f:
    #     f.write(learning)
    #     f.write(date)
    # write_line方法
    path = r"test.txt"
    info = ["吴黑客", "喜欢", "Python", 100]
    info = list(map(lambda x: str(x) + "\n", info))

    with open(path, "a", encoding="utf-8") as f:
        f.writelines(info)
