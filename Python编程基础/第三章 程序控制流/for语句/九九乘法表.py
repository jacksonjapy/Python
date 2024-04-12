if __name__ == '__main__':
    for a in range(1,10): #控制行数
        for b in range(1, a + 1): #控制列数
            print(f"{b}×{a}={a * b:<2}", end="  ")
        print()