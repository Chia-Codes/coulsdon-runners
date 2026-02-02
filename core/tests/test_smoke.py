import pytest


@pytest.mark.django_db
def test_home_smoke(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Coulsdon Runners" in resp.content
