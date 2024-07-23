import asyncio


async def func():
    print(11111)

# 协程对象(内部代码不会执行)
result = func()

#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)  # 事件循环来执行这个代码

# 更加简洁
asyncio.run(result)