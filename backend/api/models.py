import orjson
from pydantic import BaseModel


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        json_dumps = orjson.dumps
        json_loads = orjson.loads


class Book(BaseModel):
    id: int
    title: str
    year: int
    author: Author
