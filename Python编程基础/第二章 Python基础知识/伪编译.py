import py_compile


if __name__ == '__main__':
    path = r"test.py"  #指定被编译的文件
    path2 = py_compile.compile(path)
    print(path2)