import concurrent.futures
import time

numbers = [1, 2, 3, 4, 5]


def custom_sleep(n):
    time.sleep(n)
    return n


# # **************************************************************************
# start_single = time.time()
#
# single_result = []
# for i in numbers:
#     single_result.append(custom_sleep(i))
#
# end_single = time.time()
# print(single_result)
#
# print('{:.4f} s'.format(end_single - start_single))  # print->15.0381 s
# # **************************************************************************

# **************************************************************************
start_f0 = time.time()

# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.

"""
max_workers: The maximum number of threads that can be used to execute the given calls.

if max_workers is None:
    max_workers = min(32, (os.cpu_count() or 1) + 4)
if max_workers <= 0:
    raise ValueError("max_workers must be greater than 0")
"""
with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    f0_result = executor.map(custom_sleep, numbers)

end_f0 = time.time()
print(type(f0_result))  # print-><class 'generator'>
print(list(f0_result))  # print->[1, 2, 3, 4, 5]

print('{:.4f} s'.format(end_f0 - start_f0))  # print->5.0164 s
# **************************************************************************

# # **************************************************************************
# start_f1 = time.time()
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1_result = [executor.submit(custom_sleep, n) for n in numbers]
#
# end_f1 = time.time()
# print(type(f1_result[0]))  # print-><class 'concurrent.futures._base.Future'>
# print([f1r.result() for f1r in f1_result])  # print->[1, 2, 3, 4, 5]
#
# print('{:.4f} s'.format(end_f1 - start_f1))  # print->5.0026 s
# # **************************************************************************
