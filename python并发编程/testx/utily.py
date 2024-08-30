import concurrent.futures
import time
import asyncio

LST = [40000000] * 36
NUM = [1, 2, 3, 4, 5]


def func_cpu(x):
    """CPU密集型任务"""
    sums = 0
    for i in range(x):
        sums += i
    return sums


def pool_computer():
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(func_cpu, LST)
    return list(f0_result)


def func_io(n):
    """IO密集型任务"""
    time.sleep(n)
    return n


def process_computer():
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(func_cpu, LST)
    return list(f0_result)


def thread_computer():
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(func_io, NUM)
    return list(f0_result)


async def func_coro(delay, what):
    await asyncio.sleep(delay)
    return what


async def async_computer():
    t0 = time.time()
    _ = await asyncio.gather(func_coro(1, 'hello'),
                             func_coro(2, 'world'))
    return time.time() - t0
