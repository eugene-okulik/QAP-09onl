from pages.home_page import HomePage
from pages.sign_up_page import SignUp
from time import sleep


def test_sign_up_page(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_sign_up_link()
    sleep(3)    # for demonstration purposes
    sign_up_page = SignUp(driver)
    sign_up_page.enter_username(name='marybilaya')
    sign_up_page.enter_password(password='asdfg')
    sign_up_page.click_sign_up_button()
    sleep(3)    # for demonstration purposes
    assert sign_up_page.check_alert_message()
    sign_up_page.accept_alert_message()
    sleep(3)  # for demonstration purposes
    sign_up_page.close_sign_up_page()
    sleep(3)  # for demonstration purposes
