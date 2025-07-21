import asyncio


class AsyncContextManager:
    # Semantically similar to __enter__(), the only difference being that it must return an awaitable.
    async def __aenter__(self):
        print("Enter context")
        return self

    # Semantically similar to __exit__(), the only difference being that it must return an awaitable.
    async def __aexit__(self, exc_type, exc, tb):
        print("Exit context")


async def async_with_example():
    # 异步上下文管理器
    async with AsyncContextManager() as manager:
        print(type(manager))


if __name__ == "__main__":
    asyncio.run(async_with_example()) 