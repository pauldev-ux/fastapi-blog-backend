#app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.testing import future

from app.config import settings

#crear engine para postgresql
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  #True para ver las consultas en consola
    future=True
)

#sesion
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

#Base para los modelos
Base = declarative_base()

#dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
