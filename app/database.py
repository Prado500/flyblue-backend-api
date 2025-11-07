# database.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

#URL de conexión a la base de datos PostgreSQL
DATABASE_URL = f""


"""engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()"""
