import asyncio

async def fetch_data(x):
    print(f"开始处理任务 {x}")
    await asyncio.sleep(2)  # 模拟异步操作，如网络请求
    print(f"完成任务 {x}")
    return f"数据{x}"

async def main():
    # 使用 asyncio.gather() 并行运行多个协程
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)  # 输出所有协程的返回结果

asyncio.run(main())
