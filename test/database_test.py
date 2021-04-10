import database
import sqlalchemy

def test_engine():
    engine = database.sql_engine()
    assert engine.name == 'mysql'
    assert engine.driver == 'pymysql'
    assert 'future' in engine.__module__

def test_connection():
    with database.sql_connection() as conn:
        result = conn.execute(sqlalchemy.text("select 'hello world'"))
        assert 'hello world' == result.first()[0]
