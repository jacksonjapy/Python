from time import strftime, sleep
from multiprocessing import Process


class ShowSystemTime(Process):
    def run(self):
        while True:
            print(f"\r{strftime('%Y-%m-%d %H:%M:%S')}", end="")
            sleep(1)


if __name__ == '__main__':
    p = ShowSystemTime()
    p.start()
