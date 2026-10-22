import asyncio


async def iter_records():
    """async def + yield定义异步生成器(也是异步可迭代对象)"""
    for page in range(1, 4):
        print(f"[数据源] 开始读取第 {page} 页的记录...")

        for name in ("A", "B"):
            # 模拟记录逐条到达,真实业务中这里可以是异步网络读取
            await asyncio.sleep(0.8)
            yield f"第 {page} 页的记录 {name}"


async def other_work():
    for i in range(1, 13):
        await asyncio.sleep(0.3)
        print(f"[其他任务] 第 {i} 次执行：后台任务继续运行。")


async def main():
    background = asyncio.create_task(other_work())

    count = 0
    # async for:逐次等待异步迭代器的 __anext__() 结果(获取下一项时若需挂起等待,事件循环可调度其他就绪任务)
    async for record in iter_records():
        print(f"[处理] {record}")
        print(type(record))
        count += 1
        if count == 3:
            print("[处理] 只需要 3 条，提前结束；后续记录不再读取。")
            # break后不再获取后续数据
            break

    await background
    print("over!")


if __name__ == "__main__":
    asyncio.run(main())
