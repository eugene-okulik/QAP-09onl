from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

username_field = (By.ID, 'sign-username')
password_field = (By.ID, 'sign-password')
sign_up_button = (By.CSS_SELECTOR, 'button[onclick="register()"]')
close_button = (By.CSS_SELECTOR, 'button[class="close"]')


class SignUp(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, name):
        self.find_element(username_field).send_keys(name)

    def enter_password(self, password):
        self.find_element(password_field).send_keys(password)

    def click_sign_up_button(self):
        self.find_element(sign_up_button).click()

    def check_alert_message(self):
        return 'This user already exist' in Alert(self.driver).text

    def accept_alert_message(self):
        Alert(self.driver).accept()

    def close_sign_up_page(self):
        all_cross_button = self.find_elements(close_button)
        cross_button = all_cross_button[1]
        cross_button.click()


