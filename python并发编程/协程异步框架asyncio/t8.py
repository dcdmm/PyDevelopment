import asyncio

async def main():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    await fut


asyncio.run(main())