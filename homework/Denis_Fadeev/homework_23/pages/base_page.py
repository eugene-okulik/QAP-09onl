from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'http://automationpractice.com/'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_elements(by_name, by_val)

    def scroll_page_to_button(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def enter_by_text(self, args: tuple):
        by_name, by_val, text = args
        Select(self.driver.find_element(by_name, by_val)).select_by_visible_text(text)

    def enter_by_value(self, args: tuple):
        by_name, by_val, value = args
        Select(self.driver.find_element(by_name, by_val)).select_by_value(value)
