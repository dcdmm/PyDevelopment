import asyncio
import aiomysql



async def test_example():
    conn = await aiomysql.connect(host='localhost',
                                  port=19950,
                                  user='root',
                                  password='dsjk@186115!',
                                  db='amp',
                                  charset='utf8mb4')

    cur = await conn.cursor()
    await cur.execute("SELECT id, city_name FROM ai_setting LIMIT 2")
    r = await cur.fetchall()
    print(r)
    column_names = [desc[0] for desc in cur.description]
    print(column_names)
    await cur.close()
    conn.close()

asyncio.run(test_example())
