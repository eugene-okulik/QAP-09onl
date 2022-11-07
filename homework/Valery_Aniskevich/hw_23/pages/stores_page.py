from pages.base_page import BasePage
from locators import all_locators as apl


class OurStores(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_our_stores(self):
        self.find_element(apl.our_stores).click()

    def check_heading_text(self):
        return self.find_element(apl.heading).text
