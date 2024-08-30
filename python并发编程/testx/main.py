import time

from utily import process_computer, thread_computer


def get_time_cpu():
    t0 = time.time()
    _ = process_computer()
    return time.time() - t0


def get_time_io():
    t0 = time.time()
    _ = thread_computer()
    return time.time() - t0


if __name__ == '__main__':
    print(get_time_io())
    print(get_time_cpu())
