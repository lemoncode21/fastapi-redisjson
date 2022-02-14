from fastapi import FastAPI
import router

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"


app.include_router(router.router)