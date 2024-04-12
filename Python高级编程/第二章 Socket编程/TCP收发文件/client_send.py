import json
import os
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 9999)
    sock.connect(server_address)
    if sock:
        print("连接成功")
    else:
        print("连接失败")

    while True:
        file_path = rf'{input("Please input file path:")}'
        if os.path.exists(file_path):
            break
        else:
            print(f"{file_path}不存在！")
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)

    file_information = {'filename': f"{filename}", 'filesize': f"{filesize}"}
    file_information = json.dumps(file_information)

    sock.sendall(file_information.encode())
    wait = sock.recv(1024)
    # remain_size = filesize
    send_size = 0
    with open(file_path, "rb") as f:
        while filesize > 0:
            data = f.read(1024)
            filesize -= len(data)
            send_size += len(data)
            sock.sendall(data)
            print(f"已发送{send_size}字节/{filesize}")

    sock.close()
