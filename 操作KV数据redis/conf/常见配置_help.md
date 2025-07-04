```shell
# 绑定的IP地址(默认:127.0.0.1 -::1)
bind 0.0.0.0

# 端口号(默认:6379)
port 6379


# 数据库密码
requirepass qwer123456

# 缓存数据的最大内存量
maxmemory 2gb

# 内存淘汰策略
# Use the maxmemory-policy configuration directive to select the eviction policy you want to use when the limit set by maxmemory is reached.
# The following policies are available:
# noeviction: Keys are not evicted but the server will return an error when you try to execute commands that cache new data. If your database uses replication then this condition only applies to the primary database. Note that commands that only read existing data still work as normal.
# allkeys-lru: Evict the least recently used (LRU) keys.
# allkeys-lfu: Evict the least frequently used (LFU) keys.
# allkeys-random: Evict keys at random.
# volatile-lru: Evict the least recently used keys that have the expire field set to true.
# volatile-lfu: Evict the least frequently used keys that have the expire field set to true.
# volatile-random: Evict keys at random only if they have the expire field set to true.
# volatile-ttl: Evict keys with the expire field set to true that have the shortest remaining time-to-live (TTL) value.
maxmemory-policy allkeys-lru

# 数据库数量(The default database is DB 0)
databases 32

# Close the connection after a client is idle for N seconds (0 to disable)
timeout 300

# 数据库存放目录
dir /data

# RDB persistence performs point-in-time snapshots of your dataset at specified intervals.
# RDB持久化保存条件(关系:或)
save 900 1  # 900s内发生了1次更改
save 300 10  # 300s内发生了10次更改
save 60 10000  # 60s内发生了10000次更改
# The filename where to dump the DB
dbfilename dump.rdb


# AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the Redis protocol itself.
appendonly yes  # 启用 AOF
appendfilename "appendonly.aof"
# sync every time new commands are appended to the AOF. Very very slow, very safe. 
# appendfsync always
# fsync every second. Fast enough, and you may lose 1 second of data if there is a disaster.
appendfsync everysec
# Never fsync, just put your data in the hands of the Operating System. The faster and less safe method. Normally Linux will flush data every 30 seconds with this configuration, but it's up to the kernel's exact tuning.
# appendfsync no

# Set the max number of connected clients at the same time.(默认:1000)
maxclients 10000 
```