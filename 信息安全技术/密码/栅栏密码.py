# import
# import


if __name__ == '__main__':
    c = ""
    with open("/home/jackson/Downloads/BUUCTF/篱笆墙的影子.txt", "r", encoding="utf-8") as f:
        for line in f:
            c += line
    # 解密栅栏密码
    for i in range(1, len(c) + 1):
        if len(c) % i == 0:
            if len(set(c[i::i])) == 1:
                print(i)
                break
