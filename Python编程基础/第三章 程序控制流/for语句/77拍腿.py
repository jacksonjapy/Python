if __name__ == '__main__':
    for a in range(1,51):
        if a / 7 == 0 or a % 10 == 7:
            print("拍腿",end=" ")
            continue
        print(a,end=" ")