import json
import socket
import os

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.80.128', 9999)
    sock.bind(server_address)
    sock.listen()
    connect, client_address = sock.accept()
    print("conn suu!")
    while True:
        save_path = rf"{input('Please input sava path:')}"
        if os.path.isdir(save_path):
            break
        else:
            print("save path not exists")
    # repr(save_path)
    file_information = connect.recv(1024).decode()  # 接收文件信息，格式为json格式
    file_information = json.loads(file_information)
    filename = file_information['filename']
    filesize = file_information['filesize']
    print(f"filename:{filename}, filesize:{filesize}")
    save_size = 0
    connect.send("OK".encode())
    with open(os.path.join(save_path, filename), 'wb') as f:
        while save_size < filesize:
            data = connect.recv(1024)
            save_size += len(data)
            f.write(data)
    print("send over")
    connect.close()
    sock.close()
