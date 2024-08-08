import asyncio
from qdrant_client import models
from qdrant_client import AsyncQdrantClient


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
    vectors = [[0.1, 0.1, 0.1]] * 100
    result_list = await asyncio.gather(*[search(client, q) for q in vectors])
    print(result_list)


asyncio.run(create(aqc))
asyncio.run(upsert(aqc))

import time

t0 = time.time()
asyncio.run(main(aqc))
t1 = time.time()
print(t1 - t0)