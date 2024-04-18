from nmap import PortScannerAsync as pa


def print_result(host, result):
    """
    Host在线：
    端口号 端口状态 服务名 版本
    """
    print(host, "在线")
    # 提取扫描结果
    if "tcp" in result["scan"][host]:
        print("结果：")
        for port, port_info in result['scan'][host]['tcp'].items():
            print(port,
                  port_info["state"],
                  port_info["product"],
                  port_info["version"])
        print("-"*20)
    else:
        print(host, "主机不在线")


if __name__ == '__main__':
    # 创建扫描对象
    nm_obj = pa()
    target_host = "192.168.80.4"
    target_port = "1-500"
    # 调用ScannerAsync的scan方法进行扫描
    print("Scanning......")
    nm_obj.scan(target_host, target_port, arguments="-sV", callback=print_result)
    nm_obj.wait()   # 必须加上wait方法，否则主线程会退出，扫描结果无法输出
