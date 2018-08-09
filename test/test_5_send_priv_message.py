import pytest
from fixture.application import Application
from cfg_ATT import config
# nie dokonczone
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_send_priv_message(app):
    subject_of_message = app.session.random_chars(5, 15)
    content_of_message = app.session.random_chars(50, 100)
    recipient = config.username2
    app.session.login(config.username, config.password)
    app.session.create_new_priv_message(recipient, subject_of_message, content_of_message)
    app.session.go_to_outbox_by_private_messages()
    assert app.session.check_message_in_outbox(subject_of_message)