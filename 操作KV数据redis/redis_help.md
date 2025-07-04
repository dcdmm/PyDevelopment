### docker run部署

```docker
# 最简部署
docker run -d --name redis -p 6379:6379 redis:7.4.4

docker run -d \
  --name redis \
  -p 6379:6379 \
  -v /home/dcgo/redis/redis.conf:/usr/local/etc/redis/redis.conf \
  -v /home/dcgo/redis/data:/data \
  redis:7.4.4 \
  redis-server /usr/local/etc/redis/redis.conf
```