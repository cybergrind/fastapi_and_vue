import logging

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

log = logging.getLogger('websocket')

class WsHandler:
    log = logging.getLogger('WsHandler')

    def __init__(self, ws: WebSocket):
        self.ws = ws

    async def loop(self):
        await self.ws.send_json({'action': 'echo', 'msg': 'connection ok'})
        while True:
            try:
                msg = await self.ws.receive_json()
            except WebSocketDisconnect:
                return
            self.log.info(f'Got msg: {msg}')


async def ws_handler(ws: WebSocket):
    log.info('before accept')
    await ws.accept()
    log.info('before loop')
    await WsHandler(ws).loop()
