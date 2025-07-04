import redis


pool = redis.ConnectionPool(
    host='localhost',
    port=6379)

r = redis.Redis.from_pool(connection_pool=pool)

