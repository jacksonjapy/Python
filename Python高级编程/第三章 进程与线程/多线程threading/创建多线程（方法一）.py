import threading
import time
import sys


# 任务一：做饭
def cooking(total_time):
    remain_time = total_time
    while remain_time > 0:
        sys.stdout.write(f"正在做饭，剩余时间：{remain_time}\n")
        remain_time -= 1  # 每次执行消耗一秒
        time.sleep(1)


# 任务二：洗衣服
def washing(total_time):
    remain_time = total_time
    while remain_time > 0:
        sys.stdout.write(f"正在洗衣服，剩余时间：{remain_time}\n")
        remain_time -= 1
        time.sleep(1)


# 任务三：整理衣物
def tiding(total_time):
    remain_time = total_time
    while remain_time > 0:
        sys.stdout.write(f"正在整理衣物，剩余时间：{remain_time}\n")
        remain_time -= 1
        time.sleep(1)


# 任务四：拖地
def mopping(total_time):
    remain_time = total_time
    while remain_time > 0:
        sys.stdout.write(f"正在拖地，剩余时间：{remain_time}\n")
        remain_time -= 1
        time.sleep(1)


if __name__ == '__main__':
    # 串行执行
    # cooking(10)
    # washing(20)
    # tiding(15)
    # mopping(5)
    # 多线程并行或并发执行
    start_time = time.time()
    threads = []  # 创建一个列表存放所有线程对象
    t = threading.Thread(target=cooking, args=(10,))    # 通过threadings模块中的Thread类创建线程对象
    threads.append(t)
    t = threading.Thread(target=washing, args=(20,))
    threads.append(t)
    t = threading.Thread(target=tiding, args=(15,))
    threads.append(t)
    t = threading.Thread(target=mopping, args=(5,))
    threads.append(t)
    # 启动线程
    for i in threads:
        i.start()
    # 等待线程结束
    for t in threads:
        t.join()
    end_time = time.time()
    need_time = end_time - start_time

    sys.stdout.write(f"所有任务已执行完成，消耗时间{need_time}")
