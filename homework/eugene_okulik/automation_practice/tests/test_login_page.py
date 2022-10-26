import pytest
import allure

from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage

from time import sleep


CREDENTIALS = [
    {'login': 'my@mail.com', 'passwd': 'sskdjhskdjfh'},
    {'login': 'your@mail.com', 'passwd': 'ertedrtyryt'},
    {'login': 'his@mail.com', 'passwd': 'jsdgjdhgudfy'},
]


@allure.feature('Authentication')
@allure.story('registration')
@pytest.mark.parametrize('creds', CREDENTIALS)
def test_login_failed(driver, creds):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('CLick sign in button'):
        home_page.click_sign_in_button()
    auth_page = AuthenticationPage(driver)
    with allure.step(f"Enter login {creds['login']} and password {creds['passwd']} and submit"):
        auth_page.enter_login_details(email=creds['login'], passwd=creds['passwd'])
    with allure.step('Check that aler is displayed'):
        assert auth_page.check_that_alert_displayed()


def test_scroll(driver):
    page = HomePage(driver)
    # page.open_page()
    # page.scroll_page_to_bottom()
    # sleep(3)
    page.open_page()
    page.scroll_page_to_middle()
    sleep(3)

