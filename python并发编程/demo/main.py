import time
import asyncio

from utily import process_computer, thread_computer, async_computer


def get_time_cpu():
    t0 = time.time()
    _ = process_computer()
    return time.time() - t0


def get_time_io():
    t0 = time.time()
    _ = thread_computer()
    return time.time() - t0


async def complex():
    t0 = time.time()
    task1 = asyncio.create_task(async_computer())
    task2 = asyncio.create_task(async_computer())

    _ = process_computer()
    _ = await task1
    _ = thread_computer()
    _ = process_computer()
    _ = await task2
    _ = thread_computer()
    return time.time() - t0


if __name__ == '__main__':
    print(get_time_cpu())
    print(get_time_io())
    print(asyncio.run(async_computer()))
    print(asyncio.run(complex()))
