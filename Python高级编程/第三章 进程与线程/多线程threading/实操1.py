import threading
import time
import sys


def GetSystemTime():
    while True:
        # 获取当前时间并格式化
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 使用sys.stdout.write覆盖上一次的输出
        sys.stdout.write("\r当前系统时间: " + current_time)
        # 阻止自动换行并移动光标到行首
        sys.stdout.flush()
        # 每隔1秒刷新一次时间
        time.sleep(1)


if __name__ == '__main__':
    system_time = threading.Thread(target=GetSystemTime)
    system_time.start()
