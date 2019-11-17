import aiopg


class DbApi:
    def __init__(self, dsn):
        self.dsn = dsn

    async def insert_data(self, data):
        pool = await aiopg.create_pool(self.dsn)
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                for raw in data:
                    await cur.execute(f'INSERT INTO dna_data (pet_id, latitude, longitude) '
                                      f'VALUES (\'{raw["pet_id"]}\', {raw["latitude"]}, {raw["longitude"]})')
