from typing import Any, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .factories import AuthorF, BookF
from .models import AuthorIn, AuthorOut, Book
from .utils import ORJSONResponse


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins='http://localhost:8080')


@app.get('/')
async def root():
    return ORJSONResponse({'status': 'ok'})


AUTHORS = [
    AuthorOut(id=1, first_name='Stanislav', last_name='Lem'),
    AuthorOut(id=2, first_name='Ursula', last_name='Le Guin'),
]
BOOKS = [BookF() for _ in range(10)]


@app.get('/author', response_model=List[AuthorOut])
async def author():
    return ORJSONResponse(AUTHORS)


@app.post('/author', response_model=AuthorOut, status_code=201)
async def create_author(data: AuthorIn):
    a = AuthorOut(**data.dict(), id=AUTHORS[-1].id + 1)
    AUTHORS.append(a)
    return a


@app.post('/author/generate', response_model=AuthorOut, status_code=201)
async def generate_author():
    a = AuthorF()
    AUTHORS.append(a)
    return a


@app.get('/book', response_model=Book)
async def book():
    return ORJSONResponse(BOOKS)
