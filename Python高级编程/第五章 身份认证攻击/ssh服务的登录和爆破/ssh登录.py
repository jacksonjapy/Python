from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError, SSHException

if __name__ == '__main__':
    server_address: str = "192.168.80.4"
    server_port: int = 22
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy)  # 允许连接不在know_hosts文件中的主机
    while True:
        username, password = input("请输入用户名和密码，用空格分隔：").split()
        try:
            ssh_client.connect(username=username, password=password, hostname=server_address, port=server_port,
                               banner_timeout=1)
        except TimeoutError:
            print("连接超时或服务器不在线")
        except NoValidConnectionsError:
            print("服务器在线，但服务未运行")
        except AuthenticationException:
            print("用户名或密码错误")
        except SSHException:
            pass
        else:
            print("登录成功")
            # 其他操作
            stdin, stdout, stderr = ssh_client.exec_command("ls")
            print(stdout.read().decode())
            break
    ssh_client.close()  # 关闭连接
