from pages.base_page import BasePage
from selenium.webdriver.common.by import By


sign_in_button = (By.CLASS_NAME, 'login')
best_sellers_button = (By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?controller=best-sales"]')
our_stores_button = (By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?controller=stores"]')
about_us_button = (By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?id_cms=4&controller=cms"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_sign_in_button(self):
        self.find_element(sign_in_button).click()

    def click_best_sellers_button(self):
        self.find_element(best_sellers_button).click()

    def click_our_stores_button(self):
        self.find_element(our_stores_button).click()

    def click_about_us_button(self):
        self.find_element(about_us_button).click()
