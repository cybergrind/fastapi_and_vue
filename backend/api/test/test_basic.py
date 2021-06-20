import httpx
import pytest
from api.main import app


pytestmark = pytest.mark.asyncio


async def test_read_main():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
