if __name__ == '__main__':
    for i in range(1,201):
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
            print(i)
            break #找到一个就跳出循环
