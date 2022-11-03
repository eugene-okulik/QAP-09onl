from selenium.webdriver.chrome.webdriver import WebDriver


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

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_page_to_middle(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
