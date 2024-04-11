import socket
import threading


first_recv = True
def send_data(socket_object):
    """
    :param socket_object: 已经建立连接的套接字对象
    :return:
    """
    global first_recv
    while True:
        data = input("键入待发送的数据：")
        first_recv = False
        print("键入 exit 以退出程序")
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
        if first_recv:
            print(f"\r接收到数据：{data}\n键入 exit 以退出程序", end="")
        else:
            print(f"\n接收到的数据：{data}", end="")
        if data == "exit":
            break


if __name__ == '__main__':
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 与服务器建立连接
    server_address = ("127.0.0.1", 9999)
    sock.connect(server_address)
    # 分别创建发送和接收数据的线程
    threads = []
    send_thread = threading.Thread(target=send_data, args=(sock,))
    threads.append(send_thread)
    recv_thread = threading.Thread(target=recv_data, args=(sock,))
    threads.append(recv_thread)

    for th in threads:
        th.start()
    for jo in threads:
        jo.join()
    # 关闭套接字对象
    sock.close()
