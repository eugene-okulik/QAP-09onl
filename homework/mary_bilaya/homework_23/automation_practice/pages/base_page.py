from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver:  WebDriver):
        self.driver = driver
        self.base_url = 'http://automationpractice.com/'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_elements(by_name, by_val)

    # def find_inner_element(self, args: tuple):
    #     self.find_element()
    #     by_name, by_val = args
    #     outer_element = self.driver.find_element(by_name, by_val)
    #     return outer_element.find_elements(by_name, by_val)
    #     se







