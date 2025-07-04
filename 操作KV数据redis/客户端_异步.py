import redis.asyncio as redis


client = redis.Redis(
    host='localhost',
    port=6379,
    password="qwer123456",
    db=0,
    decode_responses=True
)
