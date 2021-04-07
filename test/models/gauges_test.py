from models.gauges import fetch_gauges, GaugeConfig
from pydantic import ValidationError
from test.fixtures import mock_gauges_response
import pytest
import responses
import json


def test_gauge_config():
    conf = GaugeConfig(
        name='Cossatot',
        usgs_site='08061540',
        preferred_variable='gage_height',)
    assert conf.name == 'Cossatot'
    assert conf.usgs_site == '08061540'
    assert conf.preferred_variable == 'gage_height'


def test_gauge_config_validation():
    with pytest.raises(ValidationError):
        conf = GaugeConfig(
            name='Cossatot',
            usgs_site='08061540',
            preferred_variable = 'burger',)


def test_fetch_gauges(mock_gauges_response):
    configs = [
        GaugeConfig(name='Cossatot', usgs_site='08061540', preferred_variable='gage_height'),
        GaugeConfig(name='Denton Creek', usgs_site='08055000', preferred_variable='discharge'),
    ]
    gauges = fetch_gauges(configs)
    assert len(gauges) == 2

    gauge = gauges[0]
    assert gauge.name == 'Cossatot'
    assert len(gauge.data) > 0
    assert isinstance(gauge.data[0], float)
