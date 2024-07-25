import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    # Suspend the execution of coroutine on an awaitable object. Can only be used inside a coroutine function.
    # There are three main types of awaitable objects: coroutines, Tasks, and Futures.
    await say_after(1, 'hello')  # 耗时1s
    await say_after(2, 'world')  # 耗时2s

    print(f"finished at {time.strftime('%X')}")  # 总耗时3s


asyncio.run(main())
