import threading
import time
import sys


# 先创建线程子类，再通过线程子类创建线程对象

# 创建做饭线程子类
class Cooking(threading.Thread):
    def __init__(self, total_time):
        threading.Thread.__init__(self)
        self.total_time = total_time

    def run(self):  # 必须重写run method，线程运行时自动调用该方法。
        while self.total_time > 0:
            sys.stdout.write(f"正在做饭……\n")
            self.total_time -= 1
            time.sleep(1)


class Washing(threading.Thread):
    def __init__(self, total_time):
        threading.Thread.__init__(self)
        self.total_time = total_time
        self.cookie = Cooking(total_time)

    def run(self):
        while self.total_time > 0:
            sys.stdout.write(f"正在洗衣服……\n")
            self.total_time -= 1
            time.sleep(1)


if __name__ == '__main__':
    # 通过子类创建线程对象
    start = time.time()
    thread = []
    t = Cooking(10)
    thread.append(t)
    t = Washing(10)
    thread.append(t)

    for i in thread:    # 启动线程
        i.start()

    for t in thread:    # 等待线程结束再继续下面的代码
        t.join()
    end = time.time()
    need = end - start
    print(f"所有任务已完成，共计使用时间：{need:.4f}")
