import time

from utily import pool_computer


def get_time():
    t0 = time.time()
    _ = pool_computer()
    return time.time() - t0


if __name__ == '__main__':
    print(get_time())
