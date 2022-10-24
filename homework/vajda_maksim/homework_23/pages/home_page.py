from pages.base_page import BasePage
from selenium.webdriver.common.by import By


best_sales = (By.CSS_SELECTOR, 'a[title="Best sellers"]')
stores = (By.CSS_SELECTOR, 'a[title="Our stores"]')
about_us = (By.CSS_SELECTOR, 'a[title="About us"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_best_sales_button(self):
        self.find_element(best_sales).click()

    def click_stores_button(self):
        self.find_element(stores).click()

    def click_about_us_button(self):
        self.find_element(about_us).click()
