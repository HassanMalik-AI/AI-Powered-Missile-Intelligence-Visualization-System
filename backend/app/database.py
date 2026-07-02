# Database connection and session management
from app.config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

print("Connected to database")