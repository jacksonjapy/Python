import time

if __name__ == '__main__':
    data = time.strftime("%Y年%m月%d日 %H:%M:%S")
    t = str.maketrans('0123456789', '零一二三四五六七八九')
    print(t)
    data = data.translate(t)
    print(data)
