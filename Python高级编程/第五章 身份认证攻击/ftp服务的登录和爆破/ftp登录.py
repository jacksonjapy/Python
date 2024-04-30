import socket
import ftplib

if __name__ == '__main__':
    # 创建ftp对象
    ftp = ftplib.FTP()
    # 与服务器建立连接
    server = ["192.168.80.4", 21]
    reply = ftp.connect(server[0], server[1])
    try:
        if "220" in reply:
            print("Connected!")
        else:
            print("Connection failed!")
            exit()
    except (socket.timeout, ConnectionRefusedError):
        print("Connection failed, server not found or ftp server not running!")
        exit()
    # 登录
    while True:
        try:
            user = tuple(map(str, input("please input username and password:")))
            user_reply = ftp.login(user[0], user[1])
            if "230" in user_reply:
                print("Login success!")
                break
            else:
                print("Login failed!")
        except ftplib.error_perm:
            print("Login failed, username or password mistake!")

    # ftp操作
    try:
        while True:
            cmd = input(">>>")
            if cmd == "ls":
                ftp.retrlines("LIST")
            elif cmd == "pwd":
                ftp.pwd()
            elif cmd == "cd":
                ftp.cwd(input(">>>"))
            elif cmd == "get":
                ftp.retrbinary("RETR " + input(">>>"), open(input(">>>"), "wb").write)
            elif cmd == "put":
                ftp.storbinary("STOR " + input(">>>"), open(input(">>>"), "rb"))
            elif cmd == "quit":
                ftp.quit()
                break
    except ftplib.error_perm:
        print("Operation failed!")
    # 关闭连接
    ftp.close()
