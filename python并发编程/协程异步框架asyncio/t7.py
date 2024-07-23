import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

# 报错
# task_list = [asyncio.create_task(func()),
#              asyncio.create_task(func())]

# 正确
task_list = [func(),
             func()]

done, _ = asyncio.run(asyncio.wait(task_list))