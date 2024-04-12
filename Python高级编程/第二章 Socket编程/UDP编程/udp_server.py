import socket

if __name__ == '__main__':
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 默认使用IPv4和TCP协议进行通信，此处指定使用IPv4和UDP协议进行通信。
    # 绑定地址
    server_address = ("127.0.0.1", 9999)
    sock.bind(server_address)  # 绑定地址，指定本机的IP地址和端口号。
    # 收发数据
    while True:
        receive_data, client_address = sock.recvfrom(1024)  # 接收数据时，既接收了数据（数据类型：字节串），也接收了客户端的地址
        # 把字节串转换（还原）为字符串
        print("客户端发送的数据：", receive_data.decode())
        print("客户端的地址：", client_address)
        if receive_data == b"exit":  # 如果客户端发送的命令为exit，则关闭套接字
            break
        send_data = input("请输入要发送的数据：")
        sock.sendto(send_data.encode(), client_address)
        if send_data == "exit":  # 如果发送的命令为exit，则关闭套接字
            break
    # 关闭套接字
    sock.close()