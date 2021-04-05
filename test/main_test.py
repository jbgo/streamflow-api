from fastapi.testclient import TestClient
from main import app
import pytest


client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome to flow.swiftcurrent.com"}


def test_gauges():
    resp = client.get("/gauges")
    assert resp.status_code == 200
    assert len(resp.json()['gauges']) == 2