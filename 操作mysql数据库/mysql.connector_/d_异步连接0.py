import asyncio
from mysql.connector.aio import connect


async def main():
    async with await connect(host='localhost',
                             port=19950,
                             user='root',
                             password='dsjk@186115!',
                             database='amp',
                             charset='utf8mb4') as cnx:
        async with await cnx.cursor() as cur:
            await cur.execute("SELECT version()")
            results = await cur.fetchall()
            return results

m = main()
r = asyncio.run(m)
print(r)
