import asyncio
import time


async def say_after(delay, what):
    print("start:", what)
    await asyncio.sleep(delay)
    print("end:", what)
    return what


async def main():
    print(f"started at {time.strftime('%X')}")

    # Suspend the execution of coroutine on an awaitable object. Can only be used inside a coroutine function.
    # There are three main types of awaitable objects: coroutines, Tasks, and Futures.
    r1 = await say_after(2, 'hello')  # 耗时1s
    print(r1)  # print->hello
    r2 = await say_after(1, 'world')  # 耗时2s
    print(r2)  # print->world

    print(f"finished at {time.strftime('%X')}")  # 总耗时3s


asyncio.run(main())
