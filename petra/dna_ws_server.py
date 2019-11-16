import asyncio
import websockets
import json

import config
from domain.entities import dataset as dataset


async def send_data(ws, path):
    data = json.dumps({'status': 'Success',
                       'raw': dataset.get_dataset()})
    await ws.send(data)


start_server = websockets.serve(send_data,
                                config.WS_DNA_SERVER_HOST,
                                config.WS_DNA_SERVER_PORT)


if __name__ == '__main__':
    print('Start server ...')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
