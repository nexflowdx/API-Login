import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

SENHA = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://postgres:{SENHA}@localhost:5432/api_login"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()