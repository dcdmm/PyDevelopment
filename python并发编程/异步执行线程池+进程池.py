from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time


def cpu_bound_task(task_id):
    """模拟CPU密集型任务"""
    print(f"开始CPU任务{task_id}")
    result = sum(i * i for i in range(100000000))
    print(f"完成CPU任务{task_id}")
    return result


def io_bound_task(task_id):
    """模拟I/O密集型任务"""
    print(f"开始I/O任务{task_id}")
    time.sleep(5.5)
    print(f"完成I/O任务{task_id}")
    return task_id


def run_tasks():
    # 进程池+线程池
    with ProcessPoolExecutor(max_workers=None) as process_pool, \
            ThreadPoolExecutor(max_workers=None) as thread_pool:

        # 提交CPU密集型任务到进程池
        cpu_tasks = [process_pool.submit(cpu_bound_task, i) for i in range(5)]
        # 提交I/O密集型任务到线程池
        io_tasks = [thread_pool.submit(io_bound_task, i) for i in range(5)]

        # 并行执行CPU密集型任务和I/O密集型任务
        cpu_result = [f1r.result() for f1r in cpu_tasks]
        io_result = [f1r.result() for f1r in io_tasks]

        return cpu_result, io_result


"""
可能的print打印结果:
开始I/O任务0
开始I/O任务1开始I/O任务2

开始I/O任务3开始I/O任务4

开始CPU任务0
开始CPU任务1
开始CPU任务2
开始CPU任务3
开始CPU任务4
完成CPU任务1
完成CPU任务0
完成CPU任务4
完成I/O任务0完成I/O任务3完成I/O任务1完成I/O任务2



完成I/O任务4
完成CPU任务2
完成CPU任务3
"""
if __name__ == "__main__":
    cr, ir = run_tasks()
    print(cr)
    print(ir)