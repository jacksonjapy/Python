# 发送命令给客户端，接收客户端的执行结果
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址
    client_address = ('192.168.80.135', 9999)
    sock.bind(client_address)
    # 监听客户端请求
    sock.listen()
    # 接收客户端请求
    connect, client_address = sock.accept()
    # 发送命令，接收客户端执行的结果，显示结果
    while True:
        cmd_str = input('请输入命令：')
        connect.send(cmd_str.encode('gbk'))    # 将命令发送给客户端
        result = connect.recv(4096).decode('gbk')  # 接收客户端执行的结果
        print(result)   # 打印结果
        if cmd_str == 'exit':   # 如果输入exit，退出循环
            break
    # 关闭连接
    connect.close()
    # 如果不再运行，关闭socket
    sock.close()
