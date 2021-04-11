from sqlalchemy import text

from database import Session


def test_session():
    with Session() as session:
        assert not session.autocommit
        assert not session.autoflush
        assert session.bind
        assert session.future

        result = session.query(text("'OK'"))
        assert "OK" == result.first()[0]
