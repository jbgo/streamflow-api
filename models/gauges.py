from collections import OrderedDict
import enum
from typing import List

from pydantic import BaseModel
import requests
import sqlalchemy as sa
import sqlalchemy.orm


ORMBase = sa.orm.declarative_base()


class GaugeVariableEnum(str, enum.Enum):
    gage_height = "gage_height"
    discharge = "discharge"


GAUGE_VARIABLE_CODES = {
    "00060": "discharge",
    "00065": "gage_height",
}


class GaugeConfig(BaseModel):
    name: str
    usgs_site: str
    preferred_variable: GaugeVariableEnum


class GaugeConfigDB(ORMBase):
    __tablename__ = "gauge_configs"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    usgs_site = sa.Column(sa.String(32), nullable=False)
    preferred_variable = sa.Column(sa.Enum(GaugeVariableEnum), nullable=False)


class GaugeData(BaseModel):
    name: str
    config: GaugeConfig
    data: List[float] = []


GAUGES_URL_TEMPLATE = "https://waterservices.usgs.gov/nwis/iv/?format=json&sites={sites}&period=P1D&parameterCd=00060,00065&siteStatus=all"


def fetch_gauges(gauge_configs: List[GaugeConfig]) -> List[GaugeData]:
    gauges_by_site = OrderedDict(
        [
            (conf.usgs_site, GaugeData(name=conf.name, config=conf))
            for conf in gauge_configs
        ]
    )

    sites = ",".join(gauges_by_site.keys())
    url = GAUGES_URL_TEMPLATE.format(sites=sites)
    resp = requests.get(url)
    data = resp.json()

    for ts in data["value"]["timeSeries"]:
        site = ts["sourceInfo"]["siteCode"][0]["value"]
        var_code = ts["variable"]["variableCode"][0]["value"]
        gauge = gauges_by_site[site]
        if gauge.config.preferred_variable == GAUGE_VARIABLE_CODES[var_code]:
            gauge.data = [float(x["value"]) for x in ts["values"][0]["value"]]

    return list(gauges_by_site.values())
