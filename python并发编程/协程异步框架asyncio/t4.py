import asyncio
import time

# 协程函数
async def say_after(delay, what):
    print("start")
    await asyncio.sleep(delay)  # 等待
    print(what)
    print("end")

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')  # 等
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())