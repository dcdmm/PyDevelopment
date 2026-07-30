import redis


pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    password="qwer123456",
    db=0,
    decode_responses=True,
    max_connections=50
)

r = redis.Redis.from_pool(connection_pool=pool)
print(r.ping())

print(r.exists("china"))
print(r.set('china', 'good'))
print(r.get("china"))

for key in r.keys():
    r.delete(key)
r.close()