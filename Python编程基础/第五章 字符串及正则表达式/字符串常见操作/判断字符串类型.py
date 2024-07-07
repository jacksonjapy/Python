if __name__ == '__main__':

    while True:
        n = input("input the number:")
        if n.isdecimal():
            n = int(n)
            break
        else:
            print("error,please retype!")