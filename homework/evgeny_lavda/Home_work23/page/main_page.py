from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'http://automationpractice.com/'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)
