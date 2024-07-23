



# await 协程对象/Future/task对象

import asyncio
import time

async def say_after(delay, what):
    print("start")
    await asyncio.sleep(delay)  # 等待
    print(what)
    print("end")

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())