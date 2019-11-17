import asyncio
import websockets

import config


async def get_data(pet_id):
    uri = f'{config.WS_PETRA_SERVER_URI}/{pet_id}'
    while True:
        async with websockets.connect(uri) as ws:
            await ws.send('get_data')
            data = await ws.recv()
            print(data)
            await asyncio.sleep(1)


if __name__ == '__main__':
    print('Start client ...')
    asyncio.run(get_data('df096812-afb4-4915-8cb4-a80a62e6939a'))
