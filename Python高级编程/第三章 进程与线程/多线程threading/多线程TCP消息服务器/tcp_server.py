import socket
import os
import threading

first_recv = True   # 标志是否为第一次发送数据

def send_data(socket_object):
    """
    :param socket_object: 已经建立连接的套接字对象
    :return:
    """
    global first_recv
    while True:
        data = input("键入待发送的数据：")
        first_recv = True   # 只要发送了数据，后面第一次收到的数据则为第一次接收数据
        print("键入 exit 以退出程序")
        if recv_data:
            print()
        socket_object.send(data.encode())
        if data == "exit":
            break


def recv_data(socket_object):
    """
    :param socket_object: 已经建立连接的套接字对象
    :return:
    """
    global first_recv
    while True:
        data = socket_object.recv(1024).decode()
        if first_recv:  # 判断是否为第一次接收数据，是则退格显示
            print(f"\r接收到数据：{data}\n键入 exit 以退出程序", end="")  # 第一次接收时，覆盖之前的内容再显示新消息
        else:
            print(f"\n接收到的数据：{data}", end="")  # 后面发送的数据先换行再显示
        if data == "exit":
            break


if __name__ == '__main__':
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址
    server_address = ("127.0.0.1", 9999)
    sock.bind(server_address)
    # 监听客户端请求
    sock.listen()
    # 接收请求
    connect, client_address = sock.accept()
    # 创建两个线程，分别执行发送数据和接收数据的任务
    threads = []
    send_thread = threading.Thread(target=send_data, args=(connect,))
    threads.append(send_thread)
    recv_thread = threading.Thread(target=recv_data, args=(connect,))
    threads.append(recv_thread)

    for th in threads:
        th.start()
    while send_thread.is_alive() and recv_thread.is_alive():
        pass
    os.kill(os.getpid(), 9)
    # 关闭连接和套接字
    connect.close()
    sock.close()
