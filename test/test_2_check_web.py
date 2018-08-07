import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_web(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    assert wd.title == "ATT Nauka - Index page"