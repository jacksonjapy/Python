if __name__ == '__main__':

    s = "我喜欢编程"
    # b1 = s.encode('utf-8')  # 使用默认utf-8编码
    # b2 = s.encode('gbk')  # 指定编码为gbk
    # print(b1, len(b1))
    # print(b2, len(b2))

    # 解码
    b1 = b'\xe6\x88\x91\xe5\x96\x9c\xe6\xac\xa2\xe7\xbc\x96\xe7\xa8\x8b'
    b2 = b'\xce\xd2\xcf\xb2\xbb\xb6\xb1\xe0\xb3\xcc'
    s1 = b1.decode()
    s2 = b2.decode('gbk')
    print(s1)
    print(s2)
