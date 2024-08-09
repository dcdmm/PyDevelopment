import asyncio
from qdrant_client import AsyncQdrantClient, models

# The AsyncQdrantClient provides the same methods as the synchronous counterpart QdrantClient.
# 同步操作(QdrantClient)切换到异步操作(AsyncQdrantClient)只需在方法调用前添加`await`关键字即可(upload_collection方法除外,仍是普通函数)
aqc = AsyncQdrantClient(url="http://localhost:6333")


async def create(client):
    if await client.collection_exists(collection_name="collection0"):
        await client.delete_collection(collection_name="collection0")

    await client.create_collection(
        collection_name="collection0",
        vectors_config=models.VectorParams(size=3, distance=models.Distance.COSINE),
    )


async def upsert(client):
    await client.upsert(
        collection_name="collection0",
        points=models.Batch(
            ids=[1, 2, 3, 1],
            payloads=[
                {"color": "red"},
                {"color": "green"},
                {"color": "blue"},
                {"color": "yellow"}
            ],
            vectors=[
                [0.1, 0.1, 0.1],
                [0.2, 0.2, 0.2],
                [0.3, 0.3, 0.3],
                [0.4, 0.4, 0.4],
            ],
        ),
    )


async def search(client, query_vector):
    points = await client.search(
        collection_name="collection0",
        query_vector=query_vector,
        limit=1
    )
    return points


async def main(client):
    vectors = [[0.1, 0.1, 0.1]] * 1000
    semaphore = asyncio.Semaphore(100)  # 并发限制

    async def search_with_limit(query_vector):
        async with semaphore:
            return await search(client, query_vector)

    result_list = await asyncio.gather(*[search_with_limit(q) for q in vectors])
    print(result_list)


async def run_all(aqc):
    await create(aqc)
    await upsert(aqc)
    await main(aqc)


asyncio.run(run_all(aqc))
