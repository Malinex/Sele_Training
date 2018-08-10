import pytest
from fixture.application import Application
from cfg_ATT import config
import time
# nie dokonczone
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_send_priv_message(app):
    subject_of_message = "test message " + app.session.random_chars(10, 15)
    content_of_message = app.session.random_chars(100, 150)
    recipient = config.username2
    app.session.login(config.username, config.password)
    assert app.session.get_logged_user_name() == config.username
    app.session.go_to_private_messages()
    assert app.session.check_if_user_in_private_masseges()
    app.session.create_new_priv_message(recipient, subject_of_message, content_of_message)
    app.session.go_to_outbox_after_sending_a_message()
    assert app.session.check_message_in_outbox(subject_of_message)