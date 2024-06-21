import time
import concurrent.futures

numbers = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# # **************************************************************************
# start_single = time.time()
#
# single_result = []
# for i in numbers:
#     single_result.append(fibonacci(i))
#
# end_single = time.time()
# print(single_result)
#
# print('{:.4f} s'.format(end_single - start_single))  # print->40.2218 s
# # **************************************************************************

if __name__ == '__main__':
    # **************************************************************************
    start_f0 = time.time()

    # The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
    # Both implement the same interface, which is defined by the abstract Executor class.

    # 多进程代码必须在`if __name__ == '__main__':`块中执行

    """
    max_workers: The maximum number of processes that can be used to execute the given calls.
                 If None or not given then as many worker processes will be created as the machine has processors.
    """
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(fibonacci, numbers)

    end_f0 = time.time()
    print(type(f0_result))  # print-><class 'generator'>
    print(list(f0_result))

    print('{:.4f} s'.format(end_f0 - start_f0))  # print->16.5110 s
    # **************************************************************************

    # # **************************************************************************
    # start_f1 = time.time()
    #
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     f1_result = [executor.submit(fibonacci, n) for n in numbers]
    #
    # end_f1 = time.time()
    # print(type(f1_result[0]))  # print-><class 'concurrent.futures._base.Future'>
    # print([f1r.result() for f1r in f1_result])
    #
    # print('{:.4f} s'.format(end_f1 - start_f1))  # print->15.6768 s
    # # **************************************************************************
