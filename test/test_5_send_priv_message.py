import pytest
from fixture.application import Application
#
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
    number_of_msgs_before_test = len(wd.find_elements_by_class_name("topictitle"))
    app.session.create_new_priv_message("gholak", "testowa wiadomość", "test_pm")
    app.session.go_to_outbox()
    number_of_msgs_after_test = len(wd.find_elements_by_class_name("topictitle"))
    assert number_of_msgs_before_test is not number_of_msgs_after_test