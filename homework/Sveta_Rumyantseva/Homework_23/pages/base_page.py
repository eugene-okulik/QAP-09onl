from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'http://automationpractice.com/'
        self.base_url1 = 'http://automationpractice.com/index.php?controller=best-sales'
        self.base_url2 = 'http://automationpractice.com/index.php?id_cms=4&controller=cms'
        self.base_url3 = 'http://automationpractice.com/index.php?controller=stores'

    def find_current_url(self):
        return self.driver.current_url

    def find_element(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_element(by_name, by_value)

    def find_elements(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_elements(by_name, by_value)

    def scroll_page_to_bottom(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")

    def select_dropdown_menu(self, args: tuple, text):
        by_name, by_value = args
        return Select(self.driver.find_element(by_name, by_value)).select_by_visible_text(text)

    def actions_chains(self, args: tuple, args1: tuple):
        by_name, by_value = args
        by_name1, by_value1 = args1
        return ActionChains(self.driver).move_to_element(self.driver.find_element(by_name, by_value)).\
            click(self.driver.find_element(by_name1, by_value1)).perform()
