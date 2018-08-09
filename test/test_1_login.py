import pytest
from fixture.application import Application
from cfg_ATT import config

# h87 daje okejke
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    wd = app.wd
    app.session.login(config.username, config.password)
    assert app.session.get_logged_user_name() == config.username