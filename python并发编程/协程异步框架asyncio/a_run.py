import asyncio


# 协程函数
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    return "over!"


# 协程对象
m = main()
print(m, type(m))  # print->class 'coroutine'>

# Execute the coroutine coro and return the result.
# This function runs the passed coroutine, taking care of managing the asyncio event loop, finalizing asynchronous generators, and closing the executor.
# This function always creates a new event loop and closes it at the end. It should be used as a main entry point for asyncio programs, and should ideally only be called once.
r = asyncio.run(m)
print(r)