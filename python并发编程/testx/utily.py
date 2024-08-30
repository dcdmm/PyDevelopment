import concurrent.futures

LST = [40000000] * 36


def func(x):
    sums = 0
    for i in range(x):
        sums += i
    return sums


def pool_computer():
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        f0_result = executor.map(func, LST)
    return list(f0_result)
