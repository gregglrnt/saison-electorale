from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.main import prisma
from routes.commune import router

@asynccontextmanager
async def lifespan(app: FastAPI):  
    await prisma.connect()
    yield
    await prisma.disconnect()
    
app = FastAPI(lifespan=lifespan)

app.include_router(router)