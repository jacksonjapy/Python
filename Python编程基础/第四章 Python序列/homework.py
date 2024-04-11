if __name__ == '__main__':
    # 1.定制手机套餐：假设我们可以根据需求定制自己的手机套餐，可选项为话费、流量和短信。假设有如下设置:
    # 话费:0分钟、50分钟、100分钟、300分钟、不限量
    # 流量: 0M、500M、1G、5G、不限量
    # 短信: 0条、50条、100条
    phone_bill = ('0分钟', '50分钟', '100分钟', '300分钟', '不限量')
    phone_traffic = ('0M', '500M', '1G', '5G', '不限量')
    phone_sms = ('0条', '50条', '100条')

    print("定制自己的手机套餐：")
    print("A.请选择你的通话时长：")
    j = 1
    for i in phone_bill:
        print(f"{j}.{i}")
        j += 1
    bill_choose = input("输入编号进行选择：")

    print("B.请选择你的流量包：")
    j = 1
    for i in phone_traffic:
        print(f"{j}.{i}")
        j += 1
    traffic_choose = input("输入编号进行选择：")

    print("C.请选择你的短信包：")
    j = 1
    for i in phone_sms:
        print(f"{j}.{i}")
        j += 1
    sms_choose = input("输入编号进行选择：")
    print(f"您的手机套餐定制成功：通话时长为{phone_bill[int(bill_choose) - 1]}/月，"
          f"流量包为{phone_traffic[int(traffic_choose) - 1]}/月，短信包为{phone_sms[int(sms_choose) - 1]}/月")

    # 2.模拟火车订票系统
    train = [["T1949", "西藏-北京", "07：04", "17：04", "10:08", 999],["Z1997", "成都-香港", "10:30", "次日10:30", "24:00", 999],
              ["Z158", "长春-北京", "12:48", "21:06", "08:18", 112],["T298", "成都-广元", "00:06", "10:50", "10:44", 70]]
    #使用for循环依次打印出火车车次、始发/终到站、出发时间、到达时间、历时、票数并打印
    print(f"{'车次':^8}{'始发/终到站':^8}{'出发时间':^10}{'到达时间':^9}{'历时':^9}{'票数':^9}")
    for i in train:
        print(f"{i[0]:^8}，{i[1]:^8},{i[2]:^10}，{i[3]:^9}，{i[4]:^9}，{i[5]:^9}")

    train_num = []
    j = 0
    for i in train:
        train_num.append(i[0])
    #判断输入的车次是否在列表中
    train_choose = input("请输入要购买的车次：")
    if train_choose not in train_num:
        print("没有该车次，请重新输入")
    people = list(map(str, (input("请输入乘车人：（用逗号隔开）").split(","))))
    print(f"您已购买{train_choose}车票，乘车人为{'、'.join(people)}，如需换取纸质车票，请联系客服。[中国铁路12306订票系统]")
    #使用for循环遍历车次列表，对已经购买的车票数进行修改
    for i in train:
        if i[0] == train_choose:
            i[5] -= len(people)
    print(f"{'车次':^8}{'始发/终到站':^8}{'出发时间':^10}{'到达时间':^9}{'历时':^9}{'票数':^9}")
    for i in train:
        print(f"{i[0]:^8}，{i[1]:^8},{i[2]:^10}，{i[3]:^9}，{i[4]:^9}，{i[5]:^9}")
    # 3. 应用列表、元组或字典将以下电视剧按收视率由高到低进行排序:
    '''电视剧名：《甄嬛传》、《延禧攻略》、《喜羊羊与灰太狼》、《破冰行动》、《铠甲勇士》、《铠甲勇士刑天》，《铠甲勇士拿瓦》、《雷欧奥特曼》
       收视率分别为：30.22%、50.10%，10.10%、8.62%、55.3%、80.12%、43.123%、66.66%'''
    #使用列表存储电视剧信息，并按照收视率进行降序排列
    tv_list = [('甄嬛传', 30.22), ('延禧攻略', 50.10), ('喜羊羊与灰太狼', 10.10), ('破冰行动', 8.62),
               ('铠甲勇士', 55.3),('铠甲勇士刑天', 80.12)]
    list_result = sorted(tv_list, key=lambda x: x[1], reverse=True)
    print(list_result)
    #使用元组存储电视剧信息，并按照收视率进行降序排列
    tv_tuple = (('甄嬛传', 30.22), ('延禧攻略', 50.10), ('喜羊羊与灰太狼', 10.10), ('破冰行动', 8.62),
                ('铠甲勇士', 55.3),('铠甲勇士刑天', 80.12))
    tuple_result = sorted(tv_tuple, key=lambda x: x[1], reverse=True)
    print(tuple_result)
    #使用字典存储电视剧信息，并按照收视率进行降序排列
    tv_dict = {'甄嬛传': 30.22, '延禧攻略': 50.10, '喜羊羊与灰太狼': 10.10, '破冰行动': 8.62,
               '铠甲勇士': 55.3, '铠甲勇士刑天': 80.12}
    dict_result = sorted(tv_dict.items(), key=lambda x: x[1], reverse=True)
    print(dict_result)