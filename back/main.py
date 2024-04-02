from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from db.main import prisma
from routes.commune import communes
from routes.compare import compare
from routes.election import election

@asynccontextmanager
async def lifespan(app: FastAPI):  
    await prisma.connect()
    yield
    await prisma.disconnect()
    
app = FastAPI(lifespan=lifespan)

origins = ['127.0.0.1']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(communes)
app.include_router(compare)
app.include_router(election)