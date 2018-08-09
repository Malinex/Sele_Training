import pytest
from fixture.application import Application
import time
# nie ma okejki, sleeper itp

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_topic_on_subforum(app):
    wd = app.wd
    subject_of_topic = app.session.random_chars(5, 15)
    content_of_topic = app.session.random_chars(50, 100)
    subforum_title = "Łukasz"
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page(subforum_title)
    app.session.create_new_topic(subject_of_topic, content_of_topic)
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page(subforum_title)
    assert app.session.check_subject_in_list_of_topics(subject_of_topic)




"""
DRY -> Don't repeat yourself
YAGNI -> you aren't gonna need it
KISS -> keep it simple stupid
SOLID -> read it
"""