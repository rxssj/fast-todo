from fastapi import FastAPI
from middleware.cors import init_cors

app = FastAPI()

init_cors(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}