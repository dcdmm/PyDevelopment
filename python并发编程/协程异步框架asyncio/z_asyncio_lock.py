import asyncio


# 协程数
TASK_COUNT = 10
INCREMENTS_PER_TASK = 100


async def increment_without_lock(counter: dict[str, int]) -> None:
    """不加锁:其他协程可能在await时读到相同的旧值"""
    # 设置当前值为0:
    # 协程1读取0 → 暂停
    # 协程2读取0 → 暂停
    # ...
    # 协程10读取0 → 暂停

    # 协程1写入1
    # 协程2写入1
    # ...
    # 协程10写入1

    # 本轮只+1
    for _ in range(INCREMENTS_PER_TASK):
        old_value = counter["value"]
        await asyncio.sleep(0.01) 
        counter["value"] = old_value + 1


async def increment_with_lock(
    counter: dict[str, int], lock: asyncio.Lock
) -> None:
    """加锁:每次只允许一个协程完成“读取—修改—写回”"""
    # 协程1(获得锁后,其他协程无法进入这段代码,避免共享数据被重复覆盖)：读取 0 → 写入 1 → 释放锁
    # 协程2：读取 1 → 写入 1 → 释放锁
    # ...
    # 协程10：读取 2 → 写入 1 → 释放锁

    # 本轮+10
    for _ in range(INCREMENTS_PER_TASK):
        async with lock:
            old_value = counter["value"]
            await asyncio.sleep(0.01)  
            counter["value"] = old_value + 1


async def main() -> None:
    expected = TASK_COUNT * INCREMENTS_PER_TASK

    counter_without_lock = {"value": 0}
    await asyncio.gather(
        *(increment_without_lock(counter_without_lock) for _ in range(TASK_COUNT))
    )

    counter_with_lock = {"value": 0}
    lock = asyncio.Lock()  # 所有协程必须共享同一把锁
    await asyncio.gather(
        *(increment_with_lock(counter_with_lock, lock) for _ in range(TASK_COUNT))
    )

    print(f"正确结果应该是: {expected}")
    print(f"没有 Lock 的结果: {counter_without_lock['value']}")
    print(f"使用 Lock 的结果: {counter_with_lock['value']}")


if __name__ == "__main__":
    asyncio.run(main())
