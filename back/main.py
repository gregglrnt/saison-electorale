from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.main import prisma
from routes.commune import communes
from routes.compare import compare

@asynccontextmanager
async def lifespan(app: FastAPI):  
    await prisma.connect()
    yield
    await prisma.disconnect()
    
app = FastAPI(lifespan=lifespan)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(communes)
app.include_router(compare)