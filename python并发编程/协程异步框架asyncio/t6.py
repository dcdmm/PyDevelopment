import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("main函数开始")
    task_list = [asyncio.create_task(func()),
                 asyncio.create_task(func())]
    print("main函数结束")

    done, pending = await asyncio.wait(task_list)
    print(done, pending)
    print(type(done), type(pending))
    for i in done:
        print(type(i))
        print(i.result())
    # await func()
    # await func()

asyncio.run(main())