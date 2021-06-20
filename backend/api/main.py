from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()

@app.get('/')
async def root():
    return ORJSONResponse({'status': 'ok'})
