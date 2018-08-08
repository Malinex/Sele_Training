import pytest
from fixture.application import Application

# nie ma okejki
# h87 da okejke

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_web(app):
    wd = app.wd
    assert wd.title == "ATT Nauka - Index page"