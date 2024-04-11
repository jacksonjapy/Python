if __name__ == '__main__':
    s = "Hello World!"
    print("|" + s.center(20, ) + "|")
    print("|" + s.ljust(20, ) + "|")
    print("|" + s.rjust(20, ) + "|")
    print("|" + s.zfill(20, ) + "|")
    print("|" + s.center(20, "*") + "|")