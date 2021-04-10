import json

import pytest
import responses


@pytest.fixture
def mock_gauges_response():
    with responses.RequestsMock() as rsps:
        with open('./test/data/gauges_response.json') as io:
            data = json.loads(io.read())

        rsps.add(responses.GET,
                           'https://waterservices.usgs.gov/nwis/iv/?format=json&sites=08061540,08055000&period=P1D&parameterCd=00060,00065&siteStatus=all',
                           json=data)

        yield rsps
