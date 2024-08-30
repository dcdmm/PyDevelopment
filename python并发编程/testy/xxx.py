import asyncio
import time


async def say_after(delay, what):
    print("start:", what)
    await asyncio.sleep(delay)
    print("end:", what)
    return what


async def main():
    print(f"started at {time.strftime('%X')}")

    # Run awaitable objects in the aws sequence concurrently.
    # If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.
    # If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in aws.
    l = await asyncio.gather(say_after(1, 'hello'),
                             say_after(2, 'world'))
    print(l)  # print->['hello', 'world']

    print(f"finished at {time.strftime('%X')}")  # 总耗时2s
