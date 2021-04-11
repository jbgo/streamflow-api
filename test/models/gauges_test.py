from models.gauges import fetch_gauges
from models.gauges import GaugeConfig
from pydantic import ValidationError
import pytest
from test.fixtures import mock_gauges_response


def test_gauge_config():
    conf = GaugeConfig(
        id=42,
        name="Cossatot",
        usgs_site="08061540",
        preferred_variable="gage_height",
    )
    assert conf.name == "Cossatot"
    assert conf.usgs_site == "08061540"
    assert conf.preferred_variable == "gage_height"


def test_gauge_config_validation():
    with pytest.raises(ValidationError):
        conf = GaugeConfig(
            id=42,
            name="Cossatot",
            usgs_site="08061540",
            preferred_variable="burger",
        )


def test_fetch_gauges(mock_gauges_response):
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
    assert len(gauges) == 2

    gauge = gauges[0]
    assert gauge.name == "Cossatot"
    assert len(gauge.data) > 0
    assert isinstance(gauge.data[0], float)
