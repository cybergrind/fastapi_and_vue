import logging
from typing import List

from api import const
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .factories import AuthorF, BookF
from .models import AuthorIn, AuthorOut, Book
from .utils import ORJSONResponse
from .websocket import ws_handler


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins='http://localhost:8080')
api = APIRouter(prefix='/api')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
log = logging.getLogger('main')


@api.get('/')
async def root():
    return ORJSONResponse({'status': 'ok'})


AUTHORS = [
    AuthorOut(id=1, first_name='Stanislav', last_name='Lem'),
    AuthorOut(id=2, first_name='Ursula', last_name='Le Guin'),
]
BOOKS = [BookF() for _ in range(10)]


@api.get('/author', response_model=List[AuthorOut])
async def author():
    log.info('authors')
    return ORJSONResponse(AUTHORS)


@api.post('/author', response_model=AuthorOut, status_code=201)
async def create_author(data: AuthorIn):
    a = AuthorOut(**data.dict(), id=AUTHORS[-1].id + 1)
    AUTHORS.append(a)
    return a


@api.post('/author/generate', response_model=AuthorOut, status_code=201)
async def generate_author():
    a: AuthorOut = AuthorF()  # type: ignore
    AUTHORS.append(a)
    return a


@api.get('/book', response_model=List[Book])
async def book():
    return ORJSONResponse(BOOKS)


@api.get('/settings')
async def get_settings():
    return {'zk_host': const.ZK_HOST}


api.websocket('/api/ws')(ws_handler)
app.include_router(api)
