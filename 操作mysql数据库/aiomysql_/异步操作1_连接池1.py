import asyncio
import aiomysql


async def query(pool, sql):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            return await cur.fetchall(), [desc[0] for desc in cur.description]


async def go():
    # 创建连接池
    pool = await aiomysql.create_pool(
        # minimum sizes of the pool.
        minsize=1,
        # maximum sizes of the pool.
        maxsize=10,
        host='localhost',
        port=19950,
        user='root',
        password='dsjk@186115!',
        db='amp',
        charset='utf8mb4')
    sqls = [
        "SELECT id, city_name FROM ai_setting LIMIT 2",
        "SELECT * FROM ai_bca limit 2",
        "SELECT * FROM ai_kbextra limit 2"
    ]
    r = await asyncio.gather(*[query(pool, sql) for sql in sqls])
    pool.close()
    await pool.wait_closed()
    return r

result = asyncio.run(go())
print(result)
