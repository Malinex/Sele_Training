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
    title = "123"
    description = "567"
    app.session.login("lmalinowski", "malin1")
    app.session.open_subforum_page()
    ##
    number_of_topics_before_submit = app.session.number_of_topics(wd)
    app.session.create_new_topic(title, description)
    time.sleep(3)
    app.session.open_subforum_by_nav_bar()
    number_of_topics_after_submit = app.session.number_of_topics(wd)
    assert number_of_topics_after_submit == number_of_topics_before_submit+1
    # wada nr 1: nie sprawdza czy jest więcej, sprawdza czy są rózne długości
    # wada nr 2: ważniejsza:: nie sprawdza czy stworzył się TEN konkretny temat
    # .topictitile => text == title -> jest -> ile jest (3)
    # sprawdzasz ILE elementów o takiej nazwie jest
    # potem sprawdzasz po dodaniu ile elementów o takiej nazwie jest

    # board > Łukasz > dupa > zosia > Łukasz





"""
DRY -> Don't repeat yourself
YAGNI -> you aren't gonna need it
KISS -> keep it simple stupid
SOLID -> read it
"""