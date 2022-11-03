from pages.base_page import BasePage
from selenium.webdriver.common.by import By


sign_in_button = (By.CLASS_NAME, 'login')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def sign_in_button(self):
        return self.find_element(sign_in_button)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_sign_in_button(self):
        self.find_element(sign_in_button).click()
