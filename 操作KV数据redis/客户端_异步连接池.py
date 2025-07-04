import redis.asyncio as redis
import asyncio

pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    password="qwer123456",
    db=0,
    decode_responses=True,
    max_connections=50
)
r = redis.Redis(connection_pool=pool)


async def main(client):
    print(await client.ping())

    print(await client.exists("china"))
    print(await client.set('china', 'good'))
    print(await client.get("china"))

    for key in await client.keys():
        await client.delete(key)
    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main(client=r))
