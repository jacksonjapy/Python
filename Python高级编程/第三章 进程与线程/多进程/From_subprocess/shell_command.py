from subprocess import Popen, PIPE


def shell_command():
    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        process = Popen(args=command, shell=True, stdout=PIPE)  # 创建进程对象执行命令
        result = process.stdout.read().decode()
        print(result)


if __name__ == '__main__':
    shell_command()
