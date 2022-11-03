from pytest_bdd import scenario, given, when, then
from pages.home_page import HomePage
from pages.log_in_page import LogIn


@scenario('log_in.feature', 'Username field exists')
def test_username_field():
    pass


@scenario('log_in.feature', 'Password field exists')
def test_password_field():
    pass


@given('I am on home page')
def open_home_page(driver):
    HomePage(driver).open_page()


@when('I click log in button')
def click_log_in_button(driver):
    HomePage(driver).click_log_in_link()


@then('I see a username field')
def check_username_field(driver):
    assert LogIn(driver).check_that_username_field_is_displayed()


@then('I see a password field')
def check_password_field(driver):
    assert LogIn(driver).check_that_password_field_is_displayed()






