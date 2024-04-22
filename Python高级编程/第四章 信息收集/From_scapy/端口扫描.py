from scapy.layers.inet import IP, TCP, ICMP, sr1
from threading import Thread

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
        print('host \033[32m %s is online\033[0m' % dst_ip)
    else:
        print('host \033[31m %s is offline\033[0m' % dst_ip)


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
        print(dst_port, end="\t")


if __name__ == '__main__':
    target_hosts = ('192.168.80.128', '192.168.80.139', '192.168.80.111')
    target_ports = (21, 22, 23, 80, 443, 3306, 3307)
    # 一、串行扫描方式
    # 1.扫描主机是否在线
    for ip in target_hosts:
        scapy_host(ip)

    # 2.对在线主机进行端口扫描
    for ip in up_hosts:  # 每循环一次，就扫描一个主机的端口
        print('Scanning %s hosts port, open ports have been found:' % ip)
        for port in target_ports:   # 每循环1次扫描1个端口
            scapy_port(ip, port)
