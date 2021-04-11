import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_ECHO = bool(os.getenv("DB_ECHO", False))
DB_URL = os.getenv("DB_URL", "mysql+pymysql://localhost")

engine = create_engine(DB_URL, echo=DB_ECHO, future=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
