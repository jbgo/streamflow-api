import json

import pytest
import responses

from database import Session


@pytest.fixture
def db():
    """SQLAlchemy ORM session for test database."""
    with Session() as session:
        yield session


@pytest.fixture
def mock_gauges_response():
    """Mock HTTP response to the USGS water services API."""
    with responses.RequestsMock() as rsps:
        with open("./test/data/gauges_response.json") as io:
            data = json.loads(io.read())

        rsps.add(
            responses.GET,
            "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=08061540,08055000&period=P1D&parameterCd=00060,00065&siteStatus=all",
            json=data,
        )

        yield rsps
