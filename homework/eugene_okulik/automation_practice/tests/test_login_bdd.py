from pytest_bdd import scenario, given, when, then
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage


@scenario('login.feature', 'login field exists')
def test_login_field():
    pass


@scenario('login.feature', 'password field exists')
def test_password_field():
    pass


@given('I am on home page')
def open_main_page(driver):
    home_page = HomePage(driver)
    home_page.open_page()


@when('I click login button')
def click_login_button(driver):
    HomePage(driver).click_sign_in_button()


@when('I click login field')
def click_login_field(driver):
    AuthenticationPage(driver).click_email_field()


@then('I see login field')
def check_login_field(driver):
    assert AuthenticationPage(driver).is_displayed_email_field()


@then('I see password field')
def check_password_field(driver):
    assert AuthenticationPage(driver).is_displayed_passwd_field()
