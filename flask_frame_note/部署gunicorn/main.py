import asyncio
import time
import concurrent.futures


def custom_sleep(n):
    time.sleep(n)
    return n


def how_start():
    """多线程计时"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    start_f0 = time.time()
    # ThreadPoolExecutor: python运行时创建的线程池,与gunicorn threads独立
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(custom_sleep, numbers)

    end_f0 = time.time()
    return '{:.4f} s'.format(end_f0 - start_f0)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def how_start1():
    """多进程计时"""
    numbers = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    start_f0 = time.time()
    # 如果gunicorn启动了2个(worker)进程(每个worker进程的线程数为3),每个worker进程运行时都创建了一个ProcessPoolExecutor(max_workers=5),那么总共会启动2*3*5=30个子进程并行该任务(计算斐波拉契数列),可能会导致并行效率下降(CPU超载)
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        f0_result = executor.map(fibonacci, numbers)
    end_f0 = time.time()
    return '{:.4f} s'.format(end_f0 - start_f0)


async def say_after(delay):
    await asyncio.sleep(delay)


async def how_start2():
    """异步计时"""
    start_f0 = time.time()
    # 通过asyncio.run()创建事件循环
    l = await asyncio.gather(say_after(1), say_after(2), say_after(3), say_after(4), say_after(5))
    end_f0 = time.time()
    return '{:.4f} s'.format(end_f0 - start_f0)


def how_start3():
    start_f0 = time.time()
    # HTTP请求数为2
    # 
    # 
    # # gunicorn设置1(threads = 2 workers = 1): 
    # # # 每个线程处理一个HTTP请求
    # # # IO密集型耗时5s + HTTP请求1CPU密集型10S + HTTP请求2CPU密集型10s 约等于 25s
    # 
    # # # gunicorn设置2(threads = 2 workers = 1): 
    # # # 每个进程处理一个HTTP请求
    # # # IO密集型耗时5s + CPU密集型10s 约等于 15s
    time.sleep(5)  # IO密集型任务(耗时5s)
    fibonacci(40)  # CPU密集型任务(假设耗时10s)
    end_f0 = time.time()
    return '{:.4f} s'.format(end_f0 - start_f0)


if __name__ == "__main__":
    # print(how_start())
    # print(how_start1())
    # print(asyncio.run(how_start2()))
    print(how_start3())
