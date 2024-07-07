import socket  # 导入模块

if __name__ == '__main__':
    # 创建套接字
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 指明连接方式
    sock = socket.socket()  # 默认使用IPv4+TCP
    # 连接服务器
    server_address = ('127.0.0.1', 8888)
    sock.connect(server_address)
    # 接受数据
    while True:
        data = sock.recv(1024)
        if data == "quit":
            break
        print("接收到客户端数据：", data.decode())
    # 发送数据
    while True:
        send_data = input("请输入要发送的数据:")
        sock.sendall(send_data.encode())
        if send_data == "quit":
            print("接收到到的客户端请求，服务器退出")
            break
    # 关闭套接字
    sock.close()
