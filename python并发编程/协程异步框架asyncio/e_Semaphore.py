import asyncio

# 并发限制
semaphore = asyncio.Semaphore(4)  # 限制同时运行的协程数最多为4


async def io_job(n):
    print(f"Starting coroutine {n}")
    await asyncio.sleep(1)
    print(f"Coroutine {n} finished")


async def io_job_limit(n):
    async with semaphore:
        await io_job(n)


async def main_with_limit():
    await asyncio.gather(*[io_job_limit(i) for i in range(1, 15)])


asyncio.run(main_with_limit())

print("************************************************************************")


async def main_no_limit():
    await asyncio.gather(*[io_job(i) for i in range(1, 15)])


asyncio.run(main_no_limit())
