import os
import time
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = min(32, (os.cpu_count() or 1) + 4)
GLOBAL_THREAD_POOL = ThreadPoolExecutor(max_workers=MAX_WORKERS)  # 全局进程池同理


def io_bound_task(task_id):
    """模拟I/O密集型任务"""
    print(f"开始I/O任务{task_id}")
    time.sleep(2)
    print(f"完成I/O任务{task_id}")
    return task_id * 10


def batch_execute(data):
    futures = [GLOBAL_THREAD_POOL.submit(io_bound_task, item) for item in data]
    return [f.result() for f in futures]


def batch_execute_map(data):
    return list(GLOBAL_THREAD_POOL.map(io_bound_task, data))


if __name__ == "__main__":
    # 模拟多次调用,体现全局池"创建一次,反复使用"的优势
    print("=== 第一批任务 ===")
    result1 = batch_execute([1, 2, 3])
    print(f"结果: {result1}\n")

    print("=== 第二批任务 ===")
    result2 = batch_execute_map([4, 5, 6])
    print(f"结果: {result2}\n")

    print("=== 第三批任务 ===")
    result3 = batch_execute([7, 8, 9])
    print(f"结果: {result3}")

    print("=== 第四批任务 ===")
    result4 = batch_execute_map([10, 11, 12])
    print(f"结果: {result4}\n")
