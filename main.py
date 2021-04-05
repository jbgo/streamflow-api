from fastapi import FastAPI
from models.gauges import fetch_gauges, GaugeConfig
import requests


app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Welcome to flow.swiftcurrent.com")

@app.get("/gauges")
async def gauges():
    configs = [
        GaugeConfig(name='Cossatot', usgs_site='08061540', preferred_variable='gage_height'),
        GaugeConfig(name='Denton Creek', usgs_site='08055000', preferred_variable='discharge'),
    ]
    gauges = fetch_gauges(configs)
    return dict(gauges=gauges)
