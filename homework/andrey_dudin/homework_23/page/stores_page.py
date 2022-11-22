from page.base_page import BasePage
from locators import locators


class StoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_element_text(self):
        return self.find_element(locators.phone_number).text