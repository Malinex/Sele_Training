import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_priv_message(app):
    wd = app.wd
    app.session.login("lmalinowski", "malin1")
    app.session.go_to_outbox()
    number_of_msgs_before_test = len(wd.find_elements_by_class_name("mark"))
    print (number_of_msgs_before_test)
    app.session.create_new_priv_message("lmalinowski", "test_subject", "test_pm")
    number_of_msgs_after_test = len(wd.find_elements_by_class_name("mark"))
    app.session.go_to_outbox()
    print(number_of_msgs_after_test)
    assert number_of_msgs_before_test is not number_of_msgs_after_test