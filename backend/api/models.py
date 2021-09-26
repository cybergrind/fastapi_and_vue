import orjson
from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str

    class Config:
        json_dumps = orjson.dumps
        json_loads = orjson.loads


class AuthorOut(AuthorBase):
    id: int


class AuthorIn(AuthorBase):
    pass


class Book(BaseModel):
    id: int
    title: str
    year: int
    author: AuthorOut
