from pages.base_page import BasePage
from selenium.webdriver.common.by import By

about_us_field = (By.CSS_SELECTOR, 'div[class="rte"]')


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def about_us_info(self, info):
        return f'{info}' in self.find_element(about_us_field).text
