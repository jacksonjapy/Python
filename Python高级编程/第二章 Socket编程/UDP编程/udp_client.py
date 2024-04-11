import socket

if __name__ == '__main__':
    # 创建套接字对象
    sock: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 9999)
    # 收发数据
    while True:
        send_data = input("请输入要发送的数据：")
        sock.sendto(send_data.encode(), server_address)
        if send_data == "exit":  # 如果发送的命令为exit，则关闭套接字
            print("收到退出指令，正在退出……")
            break
        receive_data, server_address = sock.recvfrom(1024)  # 接收数据时，既接收了数据（数据类型：字节串），也接收了服务器的地址
        print("服务器的地址：", server_address)
        print("服务器发送的数据：", receive_data.decode())
        if receive_data == b"exit":  # 如果服务器发送的命令为exit，则关闭套接字
            print("收到退出指令，正在退出……")
            break
    # 关闭套接字
    sock.close()
