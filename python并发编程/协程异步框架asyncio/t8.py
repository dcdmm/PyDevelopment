import asyncio
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     fut = loop.create_future()
#
#     await fut
#
#
# asyncio.run(main())

async def set_afeter(fut):
    await asyncio.sleep(2)
    fut.set_result("5555")

async def main():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    await loop.create_task(set_afeter(fut))
    data = await fut
    print(data)

asyncio.run(main())