from pages.base_page import BasePage
from pages.locators import log_in_page_locators as lipl


class LogIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_that_username_field_is_displayed(self):
        return self.find_element(lipl.username_field).is_displayed()

    def enter_username(self, name):
        self.find_element(lipl.username_field).send_keys(name)

    def check_that_password_field_is_displayed(self):
        return self.find_element(lipl.password_field).is_displayed()

    def enter_password(self, password):
        self.find_element(lipl.password_field).send_keys(password)

    def click_log_in_button(self):
        self.find_element(lipl.log_in_button).click()

    def check_welcome_field(self, name):
        return f'Welcome {name}' in self.find_element(lipl.welcome_field).text




