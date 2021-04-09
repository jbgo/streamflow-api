import sqlalchemy

def sql_engine():
    return sqlalchemy.create_engine("mysql+pymysql://localhost", future=True)
