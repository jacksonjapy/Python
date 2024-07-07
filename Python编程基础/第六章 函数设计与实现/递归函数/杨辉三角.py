"""
Write By Jackson
"""


def f(m, n):  # m为行数，n为列数
    if m == n or n == 0:
        return 1
    else:
        return f(m - 1, n) + f(m - 1, n - 1)


if __name__ == '__main__':
    line = int(input("请输入杨辉三角的行数："))
    t = []  # 保存杨辉三角的列表
    for i in range(line):
        p_line = []
        for j in range(i + 1):
            p_line.append(f(i, j))
        t.append(p_line)
    # 格式化输出杨辉三角，打印成三角形图案(每个数字和每一行所占宽度)
    word_width = len(str(t[line - 1][line // 2])) + 2
    line_width = word_width * line
    for i in t:  # 每循环一次取出一个一维列表
        s = ""  # 一维列表中的所有数字全部保存到s字符串
        for j in i:  # 依次将一维列表中的所有数字取出，居中显示放大s字符串
            s += str(j).center(word_width)
        print(s.center(line_width))
