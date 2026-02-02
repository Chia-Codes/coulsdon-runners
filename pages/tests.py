import pytest

from pages.models import Page


@pytest.mark.django_db
def test_page_detail_client(client):
    Page.objects.create(slug="about", title="About", body="hello", published=True)
    r = client.get("/p/about/")
    assert r.status_code == 200
    assert b"About" in r.content
