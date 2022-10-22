import pytest

from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage


CREDENTIALS = [
    {'login': 'my@mail.com', 'passwd': 'sskdjhskdjfh'},
    {'login': 'your@mail.com', 'passwd': 'ertedrtyryt'},
    {'login': 'his@mail.com', 'passwd': 'jsdgjdhgudfy'},
]


@pytest.mark.parametrize('creds', CREDENTIALS)
def test_login_failed(driver, creds):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_sign_in_button()
    auth_page = AuthenticationPage(driver)
    auth_page.enter_login_details(email=creds['login'], passwd=creds['passwd'])
    assert auth_page.check_that_alert_displayed()
