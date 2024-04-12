"""
By Jackson Ja
"""
from multiprocessing import Pool
from time import sleep


def p_hello(num):
    print(f"{num} Start!")
    sleep(2)
    print(f"{num} End!")


def main():
    # 创建进程池
    pool = Pool(processes=3)
    # 添加进程
    pool.map(pool, range(1, 5))
    pool.close()


if __name__ == '__main__':
    main()
