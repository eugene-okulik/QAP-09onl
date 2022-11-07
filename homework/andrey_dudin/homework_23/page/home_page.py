from page.base_page import BasePage
from locators import locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_about_us_button(self):
        self.find_element(locators.about_us).click()

    def click_best_sellers_link(self):
        self.find_element(locators.best_sellers_link).click()

    def click_stores_link(self):
        self.find_element(locators.stores_link).click()


