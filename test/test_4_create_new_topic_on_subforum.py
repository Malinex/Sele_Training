import pytest
from fixture.application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_topic_on_subforum(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page()
    number_of_topics_before_submit = len(wd.find_elements_by_class_name("topictitle"))
    app.session.create_new_topic("123", "567")
    time.sleep(3)
    app.session.open_subforum_page2()
    number_of_topics_after_submit = len(wd.find_elements_by_class_name("topictitle"))
    assert number_of_topics_after_submit is not number_of_topics_before_submit