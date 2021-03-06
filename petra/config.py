import os


WS_DNA_SERVER_HOST = os.getenv('WS_DNA_SERVER_HOST', '0.0.0.0')
WS_DNA_SERVER_PORT = int(os.getenv('WS_DNA_SERVER_PORT', 8765))
WS_DNA_SERVER_URI = f'ws://{WS_DNA_SERVER_HOST}:{WS_DNA_SERVER_PORT}'
WS_PETRA_SERVER_HOST = os.getenv('WS_PETRA_SERVER_HOST', '0.0.0.0')
WS_PETRA_SERVER_PORT = int(os.getenv('WS_PETRA_SERVER_PORT', 8766))
WS_PETRA_SERVER_URI = f'ws://{WS_PETRA_SERVER_HOST}:{WS_PETRA_SERVER_PORT}'

POSTGRES_URI = os.getenv('POSTGRES_URI')

REDIS_URI = os.getenv('REDIS_URI')
