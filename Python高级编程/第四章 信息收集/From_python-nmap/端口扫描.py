from nmap import PortScanner

if __name__ == '__main__':
    target_hosts = "192.168.80.0/24"
    target_port = "1-500"
    # 创建扫描对象
    nm = PortScanner()
    # 调用scan方法进行扫描
    nm.scan(hosts=target_hosts, ports=target_port, arguments="-sS")
    # 提取在线主机的IP地址以及开放的端口
    for ip in nm.all_hosts():
        # 判断主机是否有开放的端口
        if len(nm[ip].all_tcp()):
            print("主机IP地址：", ip)
            for port in nm[ip].all_tcp():
                print(port, end=" ")
            print()
        else:
            print(f"{ip}在线，但没有开放端口！")
