def test():
    print(f"__name__的值为{__name__}")


if __name__ == '__main__':
    print("在if语句中调用test")
    test()


# print("直接调用test")
# test()
