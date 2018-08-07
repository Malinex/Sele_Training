import pytest
from fixture.application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_get_subforum_page(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page()
    time.sleep(2)
    assert app.session.get_topic_tittle_name() == "Łukasz"