# -*- coding: utf-8 -*-
# -*- python3 -*-
# This program must be enabled on Python versions greater than or equal to 3.10

from socket import timeout
from ftplib import FTP, error_perm

if __name__ == '__main__':
    # 创建ftp对象
    ftp = FTP()
    # 与服务器建立连接
    server = ("192.168.80.4", 21)
    reply = ftp.connect(server[0], server[1])
    try:
        if "220" in reply:
            print("Connected!")
        else:
            print("Connection failed!")
            exit()
    except (timeout, ConnectionRefusedError):
        print("Connection failed, server not found or ftp server not running!")
        exit(0)
    # 登录
    while True:
        try:
            user = tuple(input("please input username and password:").split())
            user_reply = ftp.login(user[0], user[1])
            if "230" in user_reply:
                print("Login success!")
                break
            else:
                print("Login failed!")
        except error_perm:
            print("Login failed, username or password mistake!")

    # ftp操作
    print("Supported operations:[ls, pwd, cd, get, put, bye(exit the program)]")
    while True:
        cmd = input(">>>")
        match cmd:
            case "ls":
                ftp.retrlines("LIST")
            case "pwd":
                ftp.pwd()
            case "cd":
                path = cmd.split()
                if len(path) == 2:
                    ftp.cwd(path[1])
                else:
                    print("Please input a path or path mistake!")
            case "get":
                filename = input("Please input filename to get: ")
                ftp.retrbinary("RETR " + filename, open(filename, "wb").write)
            case "put":
                filename = input("Please input filename to put: ")
                ftp.storbinary("STOR " + filename, open(filename, "rb"))
            case "bye":
                ftp.quit()
                ftp.close()
                exit(0)
            case _:
                print("Operation failed!")
