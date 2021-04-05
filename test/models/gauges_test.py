from models.gauges import fetch_gauges, GaugeConfig
from pydantic import ValidationError
import pytest


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


def test_fetch_gauges():
    configs = [
        GaugeConfig(name='Cossatot', usgs_site='08061540', preferred_variable='gage_height'),
        GaugeConfig(name='Denton Creek', usgs_site='08055000', preferred_variable='discharge'),
    ]
    gauges = fetch_gauges(configs)
    assert len(gauges) == 2
    assert gauges[0].config.name == 'Cossatot'
    assert len(gauges[0].data) > 0
    assert isinstance(gauges[0].data[0], float)
