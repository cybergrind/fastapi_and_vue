import httpx
import pytest
from api.main import app
from api.factories import AuthorF, BookF


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client


async def test_read_main(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


async def test_authors(client):
    resp = await client.get('/author')
    assert resp.status_code == 200
    j = resp.json()
    assert j[0]['first_name'] == 'Stanislav'


async def test_factories():
    assert BookF()
    assert AuthorF()
