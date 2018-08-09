import pytest
from fixture.application import Application
from cfg_ATT import config
import time

# nie ma okejki i jest babol time.sleep(2)

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_get_subforum_page(app):
    wd = app.wd
    subforum_title = config.main_subforum_title
    app.session.login(config.username, config.password)
    app.session.open_subforum_page(subforum_title)
    assert app.session.get_subforum_name() == subforum_title