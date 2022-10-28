from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, chrome_driver: WebDriver):
        self.chrome_driver = chrome_driver
        self.base_url = "http://automationpractice.com/index.php"

    def find_element(self, args):
        by_name, by_value = args
        return self.chrome_driver.find_element(by_name, by_value)

    def window_skroll(self):
        self.chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

