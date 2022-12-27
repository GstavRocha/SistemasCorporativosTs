from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def onLoad():
    return {'Server': 'Rodando'}
