import socket
from typing import Any

import orjson
from fastapi.responses import ORJSONResponse as O
from pydantic import BaseModel


def default_encode(obj):
    if isinstance(obj, BaseModel):
        return obj.dict()
    raise NotImplementedError


class ORJSONResponse(O):
    def render(self, content: Any) -> bytes:
        return orjson.dumps(content, default=default_encode)


def get_my_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    return s.getsockname()[0]
