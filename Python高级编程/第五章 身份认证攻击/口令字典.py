from itertools import combinations
from string import ascii_lowercase, digits, punctuation
from random import shuffle


def generate_password():
    # 生成一个包含数字或英文小写字母且长度为6位的密码字典文件。
    # 先选一位数字
    # 再选一位英文小写字母
    # 再选一位特殊字符
    # 剩余位置随机
    while True:
        password_length = int(input("请输入密码长度（密码长度必须大于6）："))
        if password_length <= 6:
            print("密码长度必须大于6")
        else:
            digit_char = combinations(digits, 1)
            lower_char = combinations(ascii_lowercase, 1)
            special_characters = combinations(punctuation, 1)
            other_char = combinations(ascii_lowercase + digits + punctuation, password_length - 3)
            lines = 100

            with open("password.txt", "a+") as file:
                for digit in digit_char:    # 选取数字
                    for lower in lower_char:    # 选取英文小写字母
                        for special in special_characters:
                            for other in other_char:    # 选取其他字符
                                while lines != 0:
                                    password = list(digit + lower + special + other)
                                    # 打乱密码顺序
                                    shuffle(password)
                                    file.write("".join(password) + "\n")
                                    lines += 1
            print("字典生成成功")
            break


if __name__ == '__main__':
    generate_password()
