from fastapi.testclient import TestClient
import pytest
from sqlalchemy import text

from main import app
from models.gauges import GaugeConfig, GaugeConfigDB

from test.fixtures import db, mock_gauges_response


client = TestClient(app)


@pytest.fixture
def db_setup(db):
    db.execute(text(f"TRUNCATE TABLE {GaugeConfigDB.__tablename__}"))
    db.flush()


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome to flow.swiftcurrent.com"}


def test_gauges(mock_gauges_response):
    resp = client.get("/gauges")
    assert resp.status_code == 200
    assert len(resp.json()["gauges"]) == 2


def test_list_gauge_configs(db, db_setup):
    db.add(
        GaugeConfigDB(
            name="Cossatot", usgs_site="08061540", preferred_variable="gage_height"
        )
    )
    db.add(
        GaugeConfigDB(
            name="Denton Creek", usgs_site="08055000", preferred_variable="discharge"
        )
    )
    db.commit()

    resp = client.get("/gauge_configs")
    assert resp.status_code == 200

    data = resp.json()
    assert len(data) == 2


def test_create_gauge_config(db, db_setup):
    resp = client.post(
        "/gauge_configs",
        json=dict(
            name="Cossatot", usgs_site="08061540", preferred_variable="gage_height"
        ),
    )

    assert resp.status_code == 201
    print(resp.json())

    gc = GaugeConfig(**resp.json())

    gc_db = db.query(GaugeConfigDB).filter_by(id=gc.id).first()
    assert gc_db
    assert gc == GaugeConfig.from_orm(gc_db)
    assert gc.id > 0
    assert gc.name == "Cossatot"
    assert gc.usgs_site == "08061540"
    assert gc.preferred_variable == "gage_height"
