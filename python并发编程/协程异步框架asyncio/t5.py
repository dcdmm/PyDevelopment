import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    # print("main函数开始")
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())
    # print("main函数结束")

    res1 = await task1
    res2 = await task2
    print(res1,res2)
    # await func()
    # await func()

asyncio.run(main())