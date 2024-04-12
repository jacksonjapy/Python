"""
Write By Jackson
"""


# 方法一
# message = "唯有在被追赶的时候，你才能真正地奔跑。"  # 函数体外定义全局变量
#
#
# def demo():
#     print(message)
#
#
# if __name__ == '__main__':
#     demo()
#     print(message)

# 方法二：在函数体内定义全局变量
# def demo():
#     global message  # 先声明全局变量
#     message = "唯有在被追赶的时候，你才能真正地奔跑。"  # 后定义
#     print(message)
#
#
# if __name__ == '__main__':
#     demo()


message = "我喜欢Python编程！"


def demo():
    global message  # 在函数体内改变同名全局变量的值
    message = "唯有在被追赶的时候，你才能真正地奔跑。"
    print(message)


if __name__ == '__main__':
    demo()
    print(message)  # 引用的全局变量
