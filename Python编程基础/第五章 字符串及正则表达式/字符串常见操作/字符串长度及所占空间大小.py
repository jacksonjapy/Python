if __name__ == '__main__':
    ikun = "人生苦短，我用python!"
    print(len(ikun.encode())) #默认使用utf-8编码
    print(len(ikun.encode('gbk'))) #使用gbk编码
    print(len(ikun.encode('gb2312'))) #使用gb2312编码