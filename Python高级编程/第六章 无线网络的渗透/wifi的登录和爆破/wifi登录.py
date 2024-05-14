from pywifi import PyWiFi, const, Profile
from time import sleep

if __name__ == '__main__':
    # 创建一个wifi管理对象
    wifi = PyWiFi()
    # 获取本地无线网卡，判断无线网卡状态
    wireless_interface = wifi.interfaces()
    interface_count = len(wireless_interface)
    interface_status = {0: '断开连接', 1: "正在扫描", 2: "已启用", 3: '正在连接', 4: '已连接'}
    if interface_count == 0:
        print('没有找到无线网卡!')
        exit(0)
    else:
        print('已找到以下网卡:')
        for card_index, card in enumerate(wireless_interface):
            print(card_index + 1, card.name(), interface_status[card.status()])
    # 选择要操作的网卡
    while True:
        try:
            choose = int(input('请选择无线网卡的编号: '))
        except ValueError:
            print('输入错误，请重新输入!')
        else:
            if 1 <= choose <= interface_count:
                break
            else:
                print('选择错误，请重新输入!')
    # 判断网卡状态
    if wireless_interface[choose - 1].status() == const.IFACE_DISCONNECTED:
        # 如果不重新连接，则退出并断开连接
        while True:
            reconnect = input(f'网卡{wireless_interface[choose - 1].name}已连接，是否重新连接?(y/n): ')
            match reconnect:
                case "y":
                    break
                case "n":
                    print('已退出!')
                    exit(0)
                case _:
                    print('输入错误，请重新输入!')
    else:
        pass
    # 扫描AP，并获取扫描结果
    wireless_interface[choose - 1].scan()
    sleep(2)
    ap = wireless_interface[choose - 1].scan_results()
    # AP去重
    available = dict()
    for ap_index, ap in enumerate(ap):
        ap_info = {"akm": ap.akm, "ssid": ap.ssid, "bssid": ap.bssid, "cipher": ap.cipher, "auth": ap.auth}
        if ap_info not in available.values():
            available[ap_index + 1] = ap_info
    # 显示AP信息
    for index, info in available.items():
        print(f"网卡编号{index} 秘钥管理类型{info['akm']} 名称：{info['ssid']} MAC地址：{info['bssid']} 密码加密类型：{info['cipher']} 认证算法的类型：{info['auth']}")
    # 选择要连接的AP
    while True:
        try:
            ap_choose = int(input('请选择要连接的AP的编号: '))
        except ValueError:
            print('输入错误，请重新输入!')
        else:
            if 1 <= ap_choose <= len(available):    # 选择正确则退出循环
                break
            else:
                print('选择错误，请重新输入!')

    # 判断当前需要连接的AP是否需要密码
    match available[ap_choose]['akm']:
        case [4]:  # 需要密码
            # 删除AP配置文件
            wireless_interface[choose - 1].remove_all_network_profiles()
            # 添加AP配置文件
            new_profiles = Profile()  # 新建配置文件
            new_profiles.ssid = available[ap_choose]['ssid']  # 设置AP的名称
            new_profiles.bssid = available[ap_choose]['bssid']  # 设置AP的MAC地址
            new_profiles.auth = const.AUTH_ALG_OPEN  # 设置AP的认证算法
            new_profiles.cipher = const.CIPHER_TYPE_CCMP  # 设置AP的密码加密类型
            new_profiles.akm.append(const.AKM_TYPE_WPA2PSK)  # 设置WiFi的密码加密类型
            while True:
                try:
                    new_profiles.key = input('请输入WiFi的密码: ')
                    if len(new_profiles.key) < 8:
                        print("密码长度不足8位，请重新输入!")
                        continue
                    else:
                        wireless_interface[choose - 1].add_network_profile(new_profiles)  # 添加配置文件
                        wireless_interface[choose - 1].connect(new_profiles)
                        sleep(4)
                        if wireless_interface[choose - 1].status() == const.IFACE_CONNECTED:  # 判断是否连接成功
                            print(
                                f'\033[32m{wireless_interface[choose - 1].name()}网卡已连接到WiFi{available[ap_choose]["ssid"]}!\033[0m')
                            break
                        else:
                            print(
                                f'\033[31m{wireless_interface[choose - 1].name()}网卡连接WiFi{available[ap_choose]["ssid"]}失败!\033[0m')
                except ValueError:
                    print('输入错误，请重新输入!')
                else:
                    break
        case [0]:  # 无密码则直接连接AP
            # 删除AP配置文件
            wireless_interface[choose - 1].remove_all_network_profiles()
            # 添加AP配置文件
            new_profiles = Profile()  # 新建配置文件
            new_profiles.ssid = available[ap_choose]['ssid']  # 设置AP的名称
            new_profiles.bssid = available[ap_choose]['bssid']  # 设置AP的MAC地址
            wireless_interface[choose - 1].add_network_profile(new_profiles)  # 添加配置文件
            wireless_interface[choose - 1].connect(new_profiles)
            sleep(4)
            if wireless_interface[choose - 1].status() == const.IFACE_CONNECTED:  # 判断是否连接成功
                print(
                    f'\033[32m{wireless_interface[choose - 1].name()}网卡已连接到WiFi{available[ap_choose]["ssid"]}!\033[0m')
            else:
                print(
                    f'\033[31m{wireless_interface[choose - 1].name()}网卡连接WiFi{available[ap_choose]["ssid"]}失败!\033[0m')
        case _:
            pass

    # 断开AP连接
