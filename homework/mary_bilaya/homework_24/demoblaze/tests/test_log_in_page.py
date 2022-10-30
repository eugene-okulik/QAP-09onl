from pages.home_page import HomePage
from pages.log_in_page import LogIn
from time import sleep


def test_log_in_page(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_log_in_link()
    sleep(3)    # for demonstration purposes
    log_in_page = LogIn(driver)
    assert log_in_page.check_that_username_field_is_displayed()
    log_in_page.enter_username(name='marybilaya')
    assert log_in_page.check_that_password_field_is_displayed()
    log_in_page.enter_password(password='asdfg')
    log_in_page.click_log_in_button()
    sleep(3)    # for demonstration purposes
    assert log_in_page.check_welcome_field(name='marybilaya')

