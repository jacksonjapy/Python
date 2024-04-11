import time

if __name__ == '__main__':
    #获取当前系统时间
    present_time = time.strftime("%Y-%m-%d %H:%M:%S %A")
    print(present_time)
    """hour = int(present_time.split(" ")[1].split(":")[0])
    weekday = present_time.split(" ")[2]"""
    hour = int(time.strftime("%H"))
    weekday = time.strftime("%A")
    # 判断是否满足条件
    if (weekday == "Monday" or weekday == "Friday") and hour == 16:
        print("尊敬的用户你好，我店的华为Mate 10系列手机进行折扣让利活动，欢迎火速选购！")