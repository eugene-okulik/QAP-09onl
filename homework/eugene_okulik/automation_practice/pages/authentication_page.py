from pages.base_page import BasePage
from pages.locators import authentication_page_locators as apl


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(apl.email_field).send_keys(email)

    def enter_passwd(self, passwd):
        self.find_element(apl.password_field).send_keys(passwd)

    def click_submit_button(self):
        self.find_element(apl.submit_button).click()

    def check_that_alert_displayed(self):
        alert_block = self.find_element(apl.alert)
        return 'Authentication failed' in alert_block.text

    def enter_login_details(self, email, passwd):
        self.find_element(apl.email_field).send_keys(email)
        self.find_element(apl.password_field).send_keys(passwd)
        self.find_element(apl.submit_button).click()

    def is_displayed_email_field(self):
        return self.find_element(apl.email_field).is_displayed()

    def is_displayed_passwd_field(self):
        return self.find_element(apl.password_field).is_displayed()

    def click_email_field(self):
        self.find_element(apl.email_field).click()
