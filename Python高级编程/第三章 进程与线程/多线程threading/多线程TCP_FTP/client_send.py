from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import path
from json import dumps
from time import sleep

filesize, sendsize, wait = [0, 0, ""]


# 发送文件任务
def send_file(socketobject, filepath):
    '''
    :param socketobject: 已经建立连接的套接字对象
    :param filepath: 待发送文件的路径
    :return:
    '''
    global filesize, sendsize, wait

    filename = path.basename(filepath)
    filesize = path.getsize(filepath)
    file_information = {'filename': filename, 'filesize': filesize}
    file_information = dumps(file_information)
    sock.sendall(file_information.encode())
    wait = socketobject.recv(1024)
    sendsize = 0
    with open(filepath, "rb") as f:
        while filesize > sendsize:
            data = f.read(1024)
            sendsize += len(data)
            sock.sendall(data)


# 显示进度条任务
def show_process_bar():
    # 需要知道文件总大小和已发送文件大小
    global filesize, sendsize

    while True:
        if sendsize != 0:
            print(
                f"\r{'▊' * int(sendsize / filesize * 10)} {sendsize / filesize * 100:.2f}% 已发送{sendsize}字节/共{filesize}字节",
                end="")
        if sendsize == filesize:
            break
        sleep(1)


def get_valid_file_path():
    while True:
        file_path = rf'{input("Please enter the valid file path: ")}'

        try:
            if path.isfile(file_path):
                return file_path
            else:
                print("The provided path does not exist or is not a file. Please try again.")
        except FileNotFoundError:
            print("The provided file or directory could not be found. Please check the path and try again.")


if __name__ == '__main__':
    # 创建套接字对象
    sock = socket(AF_INET, SOCK_STREAM)
    # 与服务器建立连接
    address = input("请输入服务器IPv4地址:")
    try:
        port = int(input("请输入端口："))
        server_address = (address, port)
        sock.connect(server_address)
        # 创建两个线程，分别执行发送文件和显示进度条任务
        file_path = get_valid_file_path()
        thread1 = Thread(target=send_file, args=(sock, file_path))
        thread2 = Thread(target=show_process_bar)
        thread1.start()
        threads = (thread1, thread2)

        while wait == "":
            pass

        thread2.start()

        for i in threads:
            i.join()
        # 关闭套接字
        sock.close()
    except ValueError:
        print("端口号必须为整数")
