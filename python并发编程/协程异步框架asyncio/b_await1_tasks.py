import asyncio
import time


async def say_after(delay, what):
    print("start:", what)
    await asyncio.sleep(delay)
    print("end:", what)
    return what


"""
Task Object

Tasks are used to run coroutines in event loops. If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future. When the Future is done, the execution of the wrapped coroutine resumes.

Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations.
"""


async def main():
    # Wrap the coro coroutine into a Task and schedule its execution. Return the Task object.
    task1 = asyncio.create_task(
        say_after(2, 'hello'))
    task2 = asyncio.create_task(
        say_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    r1 = await task1
    print(r1)  # print->hello
    r2 = await task2
    print(r2)  # print->world

    print(f"finished at {time.strftime('%X')}")  # 总耗时2s


asyncio.run(main())
