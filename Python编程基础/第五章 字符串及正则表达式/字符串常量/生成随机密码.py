import string
import random

if __name__ == '__main__':
    password_length = int(input("请输入密码长度："))
    password_number = int(input("请输入密码的个数："))
    digits = string.digits
    char = string.ascii_letters
    punctuation = string.punctuation

    for i in range(password_number):  # 没循环一次就生成一个新的密码
        password = []
        # 密码必须包含字母、数字和特特殊符号
        password.append(random.choice(digits)) # 随机生成一个数字
        password.append(random.choice(char)) # 随机生成一个字母
        password.append(random.choice(punctuation)) # 随机生成一个特殊符号

        for j in range(password_length - 3): # 生成剩余的字符个数
            password.append(random.choice(char + digits + punctuation))
            password.append(random.choice(char + digits + punctuation))

        # 打乱顺序
        random.shuffle(password)
        print("".join(password))
