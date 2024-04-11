from time import strftime, sleep
from multiprocessing import Process


def ShowSystemTime():
    while True:
        print(f"\r{strftime('%Y-%m-%d %H:%M:%S')}", end="")
        sleep(1)


if __name__ == '__main__':
    p = Process(target=ShowSystemTime)
    p.start()
