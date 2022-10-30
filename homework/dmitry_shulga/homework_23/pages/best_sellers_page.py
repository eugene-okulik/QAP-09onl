from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


product = (By.CLASS_NAME, "right-block")
add_to_cart = (By.CSS_SELECTOR, "a[data-id-product = '7']")
add_to_compare = (By.CLASS_NAME, "add_to_compare")
proceed_to_checkout_button = (By.CSS_SELECTOR, "a[title = 'Proceed to checkout']")
compare_button = (By.CLASS_NAME, "compare-form")
sort_by_select = (By.ID, "selectProductSort")


class BestSellersPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_best_sellers_page(self):
        self.open_page()
        self.click_best_sellers_button()

    def sort_by(self):
        sort_by_value = Select(self.find_element(sort_by_select))
        sort_by_value.select_by_value("reference:desc")

    def sort_by_text(self):
        sort_text = self.find_element(sort_by_select)
        return "Reference: Highest first" in sort_text.text

    def add_to_compare(self):
        ActionChains(self.chrome_driver).move_to_element(self.find_element(product)).click(self.find_element(add_to_compare)).perform()

    def check_compare(self):
        checkout_button = self.find_element(proceed_to_checkout_button)
        return checkout_button.is_enabled()

    def add_to_cart(self):
        ActionChains(self.chrome_driver).move_to_element(self.find_element(product)).click(self.find_element(add_to_cart)).perform()

    def proceed_to_checkout_button(self):
        checkout_button = self.find_element(proceed_to_checkout_button)
        return checkout_button.is_displayed()


