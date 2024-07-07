import socket

if __name__ == '__main__':
    # 创建套接字对象，指明使用IPv4+TCP协议
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址
    server_address = ("127.0.0.1", 8888)
    sock.bind(server_address)
    # 监听请求
    sock.listen(5)
    # 接受请求
    connect = sock.accept()  # 返回一个元组，第一个元素是客户端的套接字对象，第二个元素是客户端地址
    # 发送数据
    while True:
        send_data = input("请输入要发送的数据:")
        connect[0].sendall(send_data.encode())
        if send_data == "quit":
            print("接收到到的客户端请求，服务器退出")
            break
    # 接收数据
    while True:
        data = connect[0].recv(1024)
        if data == "quit":
            break
        print("接收到客户端数据：", data.decode())
    # 关闭连接
    connect[0].close()
    # 关闭套接字
    sock.close()
