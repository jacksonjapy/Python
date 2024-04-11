import random as ra

if __name__ == '__main__':
    # 用open()函数自动创建文件，并写入10个1~100的随机整数
    with open('22705090姜美恒.txt', 'w') as f:
        for i in range(10):
            f.write(str(ra.randint(1, 100)) + '\t')
        f.write("\n" + "22705090 信安22-1 姜美恒")
