import pytest
from fixture.application import Application
from cfg_ATT import config
# nie dokonczone
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_send_priv_message(app, self):
    wd = app.wd
    subject_of_message = app.session.random_chars(5, 15)
    content_of_message = app.session.random_chars(20, 40)
    recipient = config.recipient
    app.session.login(config.username, config.password)
    app.session.go_to_outbox()
    number_of_msgs_before_test = app.session.number_of_topics()
    app.session.create_new_priv_message(recipient, subject_of_message, content_of_message)
    self.app.session.go_to_outbox()
    number_of_msgs_after_test = app.session.number_of_topics()
    assert number_of_msgs_before_test is not number_of_msgs_after_test