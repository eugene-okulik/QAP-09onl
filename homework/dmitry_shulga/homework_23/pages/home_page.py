from pages.base_page import BasePage
from selenium.webdriver.common.by import By


best_sellers_button = (By.CSS_SELECTOR, "a[title = 'Best sellers'")
our_stores_button = (By.CSS_SELECTOR, "a[title = 'Our stores'")
about_us_button = (By.CSS_SELECTOR, "a[title = 'About us'")


class HomePage(BasePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_page(self):
        self.chrome_driver.get(self.base_url)

    def click_best_sellers_button(self):
        self.find_element(best_sellers_button).click()

    def click_our_stores_button(self):
        self.find_element(our_stores_button).click()

    def click_about_us_button(self):
        self.find_element(about_us_button).click()


