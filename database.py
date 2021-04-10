import os
import sqlalchemy

DB_URL = os.getenv("DB_URL", "mysql+pymysql://localhost")

def sql_engine():
    return sqlalchemy.create_engine(DB_URL, future=True)

def sql_connection():
    engine = sql_engine()
    return engine.connect()
