import pytest
from fixture.application import Application
from cfg_ATT import config
import time
# nie ma okejki, sleeper itp

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_topic_on_subforum(app):
    subject_of_topic = "test topic " + app.session.random_chars(5, 15)
    content_of_topic = app.session.random_chars(50, 100)
    subforum_title = config.main_subforum_title
    app.session.login(config.username, config.password)
    app.forum.open_subforum_page(subforum_title)
    app.forum.create_new_topic(subject_of_topic, content_of_topic)
    app.forum.return_to_topics_list()
    assert app.forum.check_subject_in_list_of_topics(subject_of_topic)




"""
DRY -> Don't repeat yourself
YAGNI -> you aren't gonna need it
KISS -> keep it simple stupid
SOLID -> read it
"""