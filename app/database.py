import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import ssl

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def is_azure_environment():
    return DATABASE_URL and "postgres.database.azure.com" in DATABASE_URL

if is_azure_environment():
    # Azure PostgreSQL Configuration (SSL required)
    print("AZURE MODE: Applying SSL database configuration.")
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,
        connect_args={
            "ssl": ssl.create_default_context(cafile="/etc/ssl/certs/ca-certificates.crt")
        }
    )
else:
    # Local Configuration (Standard)
    print("LOCAL MODE: Using standard connection.")
    engine = create_async_engine(DATABASE_URL, echo=True)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    """
    FastAPI dependency to obtain an asynchronous DB session.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()