import string

if __name__ == '__main__':
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    while True:
        print("=" * 35)
        choose = input("请选择操作(1:加密；2:解密;0:退出程序):")
        if choose == '1':  # 加密
            text = input("请输入明文:")
            key = int(input("请输入密钥:(1~25)"))
            tab = str.maketrans(lower + upper, lower[key:] + lower[:key] + upper[key:] + upper[:key])
            crypt_text = text.translate(tab)
            print(f"密文为:", crypt_text)
        elif choose == '2':  # 解密
            crypt_text = input("请输入密文:")
            key = int(input("请输入密钥:"))
            tab = str.maketrans(lower[key:] + lower[:key] + upper[key:] + upper[:key], lower + upper)
            crypt_text = crypt_text.translate(tab)
            print("密文为:", format(crypt_text))
        elif choose == '0':
            break
        else:
            print("error,please retype!")
