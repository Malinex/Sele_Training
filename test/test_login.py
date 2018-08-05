import pytest
import time
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
"""

def test_login(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    assert app.session.get_logged_user_name() == "lmalinowski"


def test_check_web(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    assert wd.title == "ATT Nauka - Index page"

def test_subforum_page(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page()
    app.session.assert_get_tittle_in_subforum()

def test_create_new_topic_on_subforum(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page2()
    topics_before_submit = len(wd.find_elements_by_class_name("forum-title"))
    app.session.create_new_topic("123", "567")
    topics_after_submit = len(wd.find_elements_by_class_name("forum-title"))
    assert topics_after_submit is not topics_before_submit

"""

def test_send_priv_message(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.go_to_outbox()
    number_of_msgs_before_test = len(wd.find_elements_by_class_name("mark"))
    app.session.create_new_priv_message("lmalinowski", "test_subject", "test_pm")
    number_of_msgs_after_test = len(wd.find_elements_by_class_name("mark"))
    assert number_of_msgs_before_test is not number_of_msgs_after_test

