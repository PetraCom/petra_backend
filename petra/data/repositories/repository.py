import aioredis
import json

from data.db import db_api
import config


class Repository:
    @classmethod
    async def create(cls, redis_uri):
        self = Repository()
        self.redis = await aioredis.create_redis_pool(redis_uri)
        return self

    async def add_data(self, data):
        await self.redis.set('data', data)
        await self.redis.incr('data_counter')
        db = db_api.DbApi(config.POSTGRES_URI)
        await db.insert_data(json.loads(data))

    async def get_all_data(self):
        return await self.redis.get('data')

    async def get_data_by_id(self, pet_id):
        dataset = json.loads(await self.get_all_data())
        return [data for data in dataset if data['pet_id'] == pet_id]
