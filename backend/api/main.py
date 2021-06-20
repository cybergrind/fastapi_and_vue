from typing import Any, List

from fastapi import FastAPI

from .models import Author, Book
from .utils import ORJSONResponse


app = FastAPI()


@app.get('/')
async def root():
    return ORJSONResponse({'status': 'ok'})


AUTHORS = [
    Author(id=1, first_name='Stanislav', last_name='Lem'),
    Author(id=2, first_name='Ursula', last_name='Le Guin'),
]


@app.get('/author')
async def author() -> List[Author]:
    return ORJSONResponse(AUTHORS)


@app.get('/book')
async def book() -> List[Book]:
    return ORJSONResponse({})
