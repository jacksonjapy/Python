from nmap import PortScanner


if __name__ == '__main__':
    target_host = "192.168.80.0/24"
    # 创建扫描对象
    scan_obj = PortScanner()
    # 调用scan进行扫描
    scan_result = scan_obj.scan(hosts=target_host, arguments='-sP')
    # print(scan_result)  # 整体输出
    # 输出在线主机的IP
    #   方法一：通过all_hosts()方法提取
    # up_host_ip = scan_obj.all_hosts()
    # print(up_host_ip)
    #   方法二：通过字典方式提取
    up_host_ip = list(scan_result['scan'].keys())
    for ip in up_host_ip:
        print(ip)
    # 输出在线主机的操作系统类型
    # 输出开放的端口

