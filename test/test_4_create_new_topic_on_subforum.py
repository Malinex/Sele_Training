import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_topic_on_subforum(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page2()
    topics_before_submit = len(wd.find_elements_by_class_name("forum-title"))
    app.session.create_new_topic("123", "567")
    topics_after_submit = len(wd.find_elements_by_class_name("forum-title"))
    assert topics_after_submit is not topics_before_submit