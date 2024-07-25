import asyncio


# 协程函数
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


# 协程对象
m = main()
print(m, type(m))  # print->class 'coroutine'>

# Execute the coroutine coro and return the result.
# This function runs the passed coroutine, taking care of managing the asyncio event loop, finalizing asynchronous generators, and closing the executor.
asyncio.run(m)
