import asyncio


# 协程函数
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


# 协程对象
m = main()
print(m, type(m))  # print->class 'coroutine'>

# This function runs the passed coroutine, taking care of managing the asyncio event loop and finalizing asynchronous generators.
# Tis function always creates a new event loop and closes it at the end.
asyncio.run(m)
