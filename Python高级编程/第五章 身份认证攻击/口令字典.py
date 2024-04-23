from itertools import combinations
from string import ascii_lowercase, digits
from random import shuffle


def generate_password():
    # 生成一个包含数字或英文小写字母且长度为6位的密码字典文件。
    # 先选一位数字
    # 再选一位英文小写字母
    # 剩余位置随机
    password_length = int(input("请输入密码长度："))
    digit_char = combinations(digits, 1)
    lower_char = combinations(ascii_lowercase, 1)
    other_char = combinations(ascii_lowercase + digits, password_length - 2)
    for digit in digit_char:    # 选取数字
        for lower in lower_char:    # 选取英文小写字母
            for other in other_char:    # 选取其他字符
                password = list(digit + lower + other)
                # 打乱密码顺序
                shuffle(password)
                print("".join(password))


if __name__ == '__main__':
    generate_password()
