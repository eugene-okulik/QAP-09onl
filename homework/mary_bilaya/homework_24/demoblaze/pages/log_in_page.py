from pages.base_page import BasePage
from selenium.webdriver.common.by import By

username_field = (By.ID, 'loginusername')
password_field = (By.ID, 'loginpassword')
log_in_button = (By.CSS_SELECTOR, 'button[onclick="logIn()"]')
welcome_field = (By.ID, 'nameofuser')


class LogIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, name):
        self.find_element(username_field).send_keys(name)

    def enter_password(self, password):
        self.find_element(password_field).send_keys(password)

    def click_log_in_button(self):
        self.find_element(log_in_button).click()

    def check_welcome_field(self, name):
        return f'Welcome {name}' in self.find_element(welcome_field).text