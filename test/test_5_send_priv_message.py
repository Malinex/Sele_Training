import pytest
from fixture.application import Application

# nie dokonczone
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_priv_message(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.go_to_outbox()
    number_of_msgs_before_test = app.session.number_of_topics()
    app.session.create_new_priv_message("lmalinowski", "testowa wiadomość", "test_pm aaaaaaaaaaaaa")
    app.session.go_to_outbox()
    number_of_msgs_after_test = app.session.number_of_topics()
    assert number_of_msgs_before_test is not number_of_msgs_after_test