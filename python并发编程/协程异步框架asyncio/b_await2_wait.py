import asyncio
import time


async def say_after(delay, what):
    print("start:", what)
    await asyncio.sleep(delay)
    print("end:", what)
    return what


async def main():
    task_list = [
        asyncio.create_task(say_after(1, 'hello')),  # 默认name=None
        asyncio.create_task(say_after(2, 'world'), name="w")
    ]

    print(f"started at {time.strftime('%X')}")

    # Run Future and Task instances in the aws iterable concurrently and block until the condition specified by return_when..
    # The aws iterable must not be empty.
    done, pending = await asyncio.wait(task_list)

    print(type(done))  # <class 'set'>
    for i in done:
        # print(i)
        print(i.get_name())
        print(i.result())

    print(f"finished at {time.strftime('%X')}")  # 总耗时2s


asyncio.run(main())
