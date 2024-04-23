from nmap import PortScannerAsync as pa


def error_display(message, over=False):
    if not over:
        print(f"\033[1;31m{message}\033[0m", end="")
    else:
        print(f"\033[1;31m{message}\033[0m")


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
            state = port_info["state"]
            product = port_info["product"]
            version = port_info["version"]
            print(f"端口：\033[33m{port}\033[0m", end="")
            if state == "open":
                print(f"状态：\033[1;32m{port}\033[0m", end="")
            elif state == "closed":
                print(f"状态：", end="")
                error_display(state, over=True)
            else:
                print(f"{state}")

            print(f"服务名：{product} 版本：{version}")
        print("-"*20)
    else:
        print(host, "主机不在线")


def check_ip(ip):
    """
    检查IP地址是否合法
    """
    check_list = []
    for i in ip.split("."):
        if i.isdigit():
            check_list.append(i)
        else:
            print("请输入正确的IPv4地址")

    if len(check_list) == 4:
        pass
    elif int(check_list[3]) < 1 or int(check_list[3]) > 255:
        print("请输入正确的IPv4地址")


def check_port(port):
    check_list = []
    for i in port.split("-"):
        if i.isdigit():
            check_list.append(i)
        else:
            pass
    if len(check_list) == 2:
        pass
    elif int(check_list[0]) == 0:
        print("起始端口号范围过小，不支持扫描0号端口", end="")
        error_display(check_list[0], over=True)
    elif int(check_list[1]) > 15000:
        print("结束端口号过大", end="")
        error_display(check_list[1], over=True)
    else:
        print("\033[1;31m请输入正确的端口范围\033[0m")


if __name__ == '__main__':
    # 创建扫描对象
    nm_obj = pa()
    target_host = input("请输入目标主机（IPv4地址）：")
    target_port = input("请输入目标端口（范围实例:1-100，建议最大端口号为15000）：")
    # 调用ScannerAsync的scan方法进行扫描
    print("Scanning......")
    nm_obj.scan(target_host, target_port, arguments="-sV", callback=print_result)
    nm_obj.wait()   # 必须加上wait方法，否则主线程会退出，扫描结果无法输出
