from multiprocessing import Pool, cpu_count
from time import time


def is_prime(num):
    '''
    :param num:待判断的素数
    :return:
    '''
    if num == 1:
        return 0
    elif num == 2:
        # print(f"{num}是素数", end="")
        return 1
    elif num & 1 == 0:
        return 0
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # 因为被整除，不是素数
                return 0
    # print(f"{num}", end=" ")
    return 1


if __name__ == '__main__':
    start_time = time()
    cpu_num = cpu_count()  # 逻辑核心数
    pool = Pool(cpu_num - 1)
    pool_num = 100000
    total_prime = sum(pool.map(is_prime, range(1, pool_num)))
    end_time = time()
    need_time = end_time-start_time
    print(f"\n1~{total_prime}总共有：{total_prime}个素数，总耗时：{need_time:.2f}")
