from fastapi import FastAPI, Depends

from database import Session, get_session
from models.gauges import fetch_gauges
from models.gauges import GaugeConfigCreate, GaugeConfig, GaugeConfigDB


app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Welcome to the Streamflow API")


@app.get("/gauges")
async def gauges():
    configs = [
        GaugeConfig(
            id=1,
            name="Cossatot",
            usgs_site="08061540",
            preferred_variable="gage_height",
        ),
        GaugeConfig(
            id=2,
            name="Denton Creek",
            usgs_site="08055000",
            preferred_variable="discharge",
        ),
    ]
    gauges = fetch_gauges(configs)
    return dict(gauges=gauges)


@app.get("/gauge_configs")
async def list_gauge_configs(db: Session = Depends(get_session)):
    return db.query(GaugeConfigDB).all()


@app.post("/gauge_configs", status_code=201)
async def create_gauge_config(
    gauge_config_create: GaugeConfigCreate, db: Session = Depends(get_session)
):
    gc_db = GaugeConfigDB(**gauge_config_create.dict())
    db.add(gc_db)
    db.commit()
    db.refresh(gc_db)

    return gc_db
