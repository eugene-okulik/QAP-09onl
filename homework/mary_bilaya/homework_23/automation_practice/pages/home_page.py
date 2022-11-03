from pages.base_page import BasePage
from pages.locators import home_page_locators as hpl


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def click_footer_best_sellers(self):
        self.find_element(hpl.footer_best_sellers_link).click()

    def click_footer_our_stores(self):
        self.find_element(hpl.footer_our_stories_link).click()

    def click_footer_about_us(self):
        self.find_element(hpl.footer_about_us_link).click()
