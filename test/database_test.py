import database

def test_engine():
    engine = database.sql_engine()
    assert engine.name == 'mysql'
    assert engine.driver == 'pymysql'
    assert 'future' in engine.__module__
