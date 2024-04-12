from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import path
from json import loads
from time import sleep

save_path, filesize, savesize = ["", 0, 0]
# 接收文件
def server_recv(ConnectionObject):
    '''
    :param ConnectionObject: 已经建立连接的套接字对象
    :return:
    '''
    global savesize
    global filesize
    global save_path

    file_information = ConnectionObject.recv(1024).decode()  # 接收文件信息，格式为json格式
    file_information = loads(file_information)
    filename = file_information['filename']
    filesize = file_information['filesize']
    print(f"filename:{filename}, filesize:{filesize}")

    while True:
        save_path = rf"{input('Please input sava path:')}"
        if path.isdir(save_path):
            break
        else:
            print("save path not exists!")

    ConnectionObject.send("OK".encode())
    savesize = 0
    with open(path.join(save_path, filename), 'wb') as f:
        while savesize < filesize:
            data = ConnectionObject.recv(1024)
            savesize += len(data)
            f.write(data)


def show_process_bar():
    # 需要知道文件总大小和已发送文件大小
    global filesize
    global savesize
    while savesize > 0:
        print(
            f"\r{'▊' * int(savesize / filesize * 10)} {savesize / filesize * 100:.2f}% 已接收{savesize}字节/共{filesize}字节",
            end="")
        if savesize == filesize:
            break
        sleep(1)


if __name__ == '__main__':
    # 创建套接字对象
    sock = socket(AF_INET, SOCK_STREAM)
    # 绑定地址
    server_address = ('127.0.0.1', 9999)
    sock.bind(server_address)
    # 监听客户端请求
    sock.listen()
    # 接收请求
    connection, client_address = sock.accept()
    # 创建两个线程分别执行接收文件和显示进度条任务
    thread1 = Thread(target=server_recv, args=(connection,))
    thread2 = Thread(target=show_process_bar)
    threads = (thread1, thread2)
    thread1.start()

    while save_path == "":
        pass

    thread2.start()

    for th in threads:
        th.join()
    # 关闭连接和套接字对象
    connection.close()
    sock.close()
