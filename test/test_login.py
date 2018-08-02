import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    wd = app.wd
    app.session.login(username="lmalinowski", password="malin1")
    assert wd.find_element_by_id("username_logged_in").text == "lmalinowski"
    app.session.logout()

def test_check_web(app):
    wd = app.wd
    app.session.login(username="lmalinowski", password="malin1")
    assert "attnauka.webd.pro" in wd.current_url

def test_subforum_page(app):
    wd = app.wd
    app.session.login(username="lmalinowski", password="malin1")
    app.session.open_subforum_page()
    assert wd.find_element_by_id("forum-search").text