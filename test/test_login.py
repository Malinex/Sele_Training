import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    assert app.session.get_logged_user_name() == "lmalinowski"





def test_check_web(app):
    wd = app.wd
    app.session.login(username="lmalinowski", password="malin1")
    assert "attnauka.webd.pro" in wd.current_url

    """
    assert wd.title == "dupa jasia"
    
    """

def test_subforum_page(app):
    wd = app.wd
    app.session.login(username="lmalinowski", password="malin1")
    app.session.open_subforum_page()