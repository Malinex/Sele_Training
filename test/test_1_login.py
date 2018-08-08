import pytest
from fixture.application import Application

# h87 daje okejke
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    assert app.session.get_logged_user_name() == "lmalinowski"