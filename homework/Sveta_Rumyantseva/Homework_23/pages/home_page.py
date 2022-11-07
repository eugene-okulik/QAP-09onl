from pages.base_page import BasePage
from selenium.webdriver.common.by import By

best_sellers_link = (By.CSS_SELECTOR, 'a[title="Best sellers"]')
about_us_link = (By.CSS_SELECTOR, 'a[title="About us"]')
our_stores_link = (By.CSS_SELECTOR, 'a[title="Our stores"]')
alert = (By.CLASS_NAME, "alert")


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_best_sellers_link(self):
        self.find_element(best_sellers_link).click()

    def click_about_us_link(self):
        self.find_element(about_us_link).click()

    def click_our_stores_link(self):
        self.find_element(our_stores_link).click()

    def check_alert_block(self):  # alert on home page from newsletters field
        alert_block = self.find_element(alert)
        return alert_block.text
