import pytest
from fixture.application import Application
import time

# nie ma okejki i jest babol time.sleep(2)

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_get_subforum_page(app):
    wd = app.wd
    subforum_title = "Łukasz"
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page(subforum_title)
    time.sleep(2)
    assert app.session.get_subforum_name() == subforum_title

    #