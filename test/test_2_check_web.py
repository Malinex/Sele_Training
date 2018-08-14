import pytest
from fixture.application import Application
from cfg_ATT import config

# nie ma okejki
# h87 da okejke

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_web(app):
    wd = app.wd
    app.session.open_home_page()
    assert app.session.check_tittle("ATT Nauka - Index page")