import asyncio


async def async_counter(stop: int, interval: float = 0.5):
    for i in range(stop):
        await asyncio.sleep(interval)
        yield i


async def main():
    print("开始使用async for遍历(有序)异步生成器(也是异步可迭代对象):")
    async for number in async_counter(stop=5, interval=0.3):
        print(f"get: {number}")
    print("over!")


if __name__ == "__main__":
    asyncio.run(main())
