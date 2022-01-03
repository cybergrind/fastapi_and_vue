import httpx
import pytest
from api.factories import AuthorF, BookF
from api.main import app


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client


async def test_read_main(client):
    response = await client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


async def test_authors(client):
    resp = await client.get('/api/author')
    assert resp.status_code == 200
    j = resp.json()
    assert j[0]['first_name'] == 'Stanislav'


async def test_factories():
    assert BookF()
    assert AuthorF()


async def test_create_author(client: httpx.AsyncClient):
    resp = await client.post('/api/author', json={'first_name': 1})
    assert resp.status_code == 422

    resp = await client.post('/api/author', json={'first_name': 'author', 'last_name': 'last'})
    assert resp.status_code == 201
    assert resp.json()['id'] == 3

    resp = await client.post('/api/author', json={'first_name': 'author', 'last_name': 'last'})
    assert resp.status_code == 201
    assert resp.json()['id'] == 4
