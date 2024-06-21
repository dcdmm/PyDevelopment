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

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f0_result = executor.map(fibonacci, numbers)

    end_f0 = time.time()
    print(list(f0_result))

    print('{:.4f} s'.format(end_f0 - start_f0))  # print->16.5110 s
    # **************************************************************************

    # **************************************************************************
    start_f1 = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1_result = [executor.submit(fibonacci, n) for n in numbers]

    end_f1 = time.time()
    print([f1r.result() for f1r in f1_result])

    print('{:.4f} s'.format(end_f1 - start_f1))  # print->15.6768 s
    # **************************************************************************


