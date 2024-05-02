from ftp_brute_force import FtpBruteForce, MultiThreadedLogin

if __name__ == '__main__':
    server_address = input("请输入服务器地址：")
    user_dict = r"user.dic"
    password_dict = r"password.dic"
    fbf = FtpBruteForce(server_address, user_dict, password_dict)
    user_tuple, password_tuple = fbf.load_dict()
    fbf.connection()
    fbf.login(user_tuple, password_tuple)
