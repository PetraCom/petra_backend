import asyncio
import websockets
import json

import config
from data.repositories import repository as repository


async def send_data(ws, path):
    bfr = await repository.Repository.create(config.REDIS_URI)
    pet_id = get_pet_id_from_path(path)
    data = await bfr.get_data_by_id(pet_id)
    await ws.send(json.dumps(data))


def get_pet_id_from_path(path):
    return path[1:]


start_server = websockets.serve(send_data,
                                config.WS_PETRA_SERVER_HOST,
                                config.WS_PETRA_SERVER_PORT)


if __name__ == '__main__':
    print('Start websocket track server ...')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
