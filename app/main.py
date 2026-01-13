from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routers import api_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB and create tables if they don't exist
    print("Starting application and verifying database connection...")
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all) # Uncomment only for testing/reset
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables verified/created.")
    
    yield
    
    # Shutdown
    print("Application shutting down.")

app = FastAPI(
    title="FlyBlue Flight System API",
    version="1.0.0",
    description="Asynchronous API for flight booking management.",
    lifespan=lifespan
)

# CORS Configuration
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include V1 routers
app.include_router(api_v1)

@app.get("/")
def read_root():
    return {"message": "FlyBlue API is active", "status": "200", "docs": "/docs"}