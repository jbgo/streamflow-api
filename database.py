import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_ECHO = bool(os.getenv("DB_ECHO", False))
DB_URL = os.environ["DB_URL"]

engine = create_engine(DB_URL, echo=DB_ECHO, future=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
