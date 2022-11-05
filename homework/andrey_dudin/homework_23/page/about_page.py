from page.base_page import BasePage
from locators import locators


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def dresses_button(self):
        button = self.find_element(locators.dresses_button)
        return button.is_displayed()