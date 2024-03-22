from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.main import prisma
from routes.commune import communes
from routes.compare import compare

@asynccontextmanager
async def lifespan(app: FastAPI):  
    await prisma.connect()
    yield
    await prisma.disconnect()
    
app = FastAPI(lifespan=lifespan)

app.include_router(communes)
app.include_router(compare)