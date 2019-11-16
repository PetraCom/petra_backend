import asyncio
import websockets

from data.repositories import repository as repository
import config


async def get_data():
    while True:
        async with websockets.connect(config.WS_DNA_SERVER_URI) as ws:
            await ws.send('get_data')
            data = await ws.recv()
            rep = await repository.Repository.create(config.REDIS_URI)
            await rep.add_data(data)
            await asyncio.sleep(1)


if __name__ == '__main__':
    print('Start data getter ...')
    asyncio.run(get_data())
