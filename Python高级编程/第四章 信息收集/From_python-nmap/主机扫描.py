from nmap import PortScanner


if __name__ == '__main__':
    target_host = "127.0.0.1"
    target_port = "1-9999"
    # 创建扫描对象
    scan_obj = PortScanner()
    # 调用scan进行扫描
    scan_result = scan_obj.scan(hosts=target_host, ports=target_port, arguments='-sV -O')
    print(scan_result)
    # 输出在线主机的IP
    # 输出在线主机的操作系统类型
    # 输出开放的端口

