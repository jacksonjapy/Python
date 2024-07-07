from scapy.layers.inet import IP, TCP, ICMP, sr1
from threading import Thread
from time import time

up_hosts = []


def scapy_host(dst_ip):
    """
    扫描主机是否在线
    :param dst_ip:目的IP地址
    :return:
    """
    global up_hosts
    # 1.构造包
    packet = IP(dst=dst_ip) / ICMP()  # ICMP默认发送的类型是echo_request，type为8, code为0
    # 2.发送并接收包
    answer = sr1(packet, timeout=4, verbose=0)
    # 3.分析结果，判断主机是否在线
    if answer and answer[ICMP].type == 0 and answer[ICMP].code == 0:
        up_hosts.append(dst_ip)
        print('host \033[32m %s \033[0m is online' % dst_ip)
    else:
        print('host \033[31m %s \033[0m is offline' % dst_ip)


def scapy_port(dst_ip, dst_port):
    """
    扫描端口是否开放
    :return:
    """
    # 1.构造包
    packet = IP(dst=dst_ip) / TCP(dport=dst_port, flags="S")
    # 2.发送并接收包
    answer = sr1(packet, timeout=4, verbose=0)
    # 3.分析结果，判断端口是否开放
    if answer and "TCP" in answer and answer[TCP].flags == "SA":
        print(dst_port, end=" ")


if __name__ == '__main__':
    start_time = time()
    target_hosts = ('192.168.80.128', '192.168.80.139', '192.168.80.4')
    target_ports = (21, 22, 23, 80, 443, 3306, 3307)
    # 二、并行扫描方式（多进程）
    threads_list = []
    for hosts in target_hosts:
        host_thread = Thread(target=scapy_host, args=(hosts,))
        host_thread.start()
        threads_list.append(host_thread)

    for thread in threads_list:
        thread.join()

    if len(up_hosts) == 0:  # 判断是否存在在线主机，如果没有主机在线，则不扫描端口。
        pass
    else:
        for up_host in up_hosts:
            print(f"host {up_host} open port:", end="")
            for port in target_ports:
                port_thread = Thread(target=scapy_port, args=(up_host, port))
                port_thread.start()
                threads_list.append(port_thread)
        for th in threads_list:
            th.join()
    end_time = time()
    need_time = (end_time - start_time)
    print(f"总耗时{need_time:.2f}秒")
