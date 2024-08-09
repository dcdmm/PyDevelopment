import asyncio
import concurrent.futures
import requests


# 阻塞任务(不支持asyncio异步操作的第三方库)
def blocking_io(url):
    return requests.get(url).content


# 阻塞任务(CPU密集型任务)
def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print("say_after", what)
    return what


async def async_job():
    l = await asyncio.gather(say_after(1, 'hello'),
                             say_after(2, 'world'))
    print("async_job", l)


# 直接调用阻塞任务:阻塞整个异步事件循环
# run_in_executor中执行阻塞任务:阻塞任务(进程池/线程池中)后台执行,不影响异步事件循环

async def not_async_job():
    # Return the running event loop in the current OS thread.
    loop = asyncio.get_running_loop()

    # Arrange for func to be called in the specified executor.
    # if executor is None. The default executor can be set by loop.set_default_executor(), otherwise, a concurrent.futures.ThreadPoolExecutor will be lazy-initialized and used by run_in_executor() if needed.
    # This method returns a asyncio.Future object.
    result = await loop.run_in_executor(None, blocking_io, 'https://www.baidu.com/')
    print('default: ', result)

    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io, "https://www.baidu.com/")
        print('ThreadPoolExecutor0: ', result)

    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print('ProcessPoolExecutor', result)


async def run_all():
    await say_after(1, "dcdmm")
    await async_job()
    await not_async_job()


if __name__ == '__main__':
    asyncio.run(run_all())
