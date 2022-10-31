from pages.base_page import BasePage
from selenium.webdriver.common.by import By

cart_text = (By.CLASS_NAME, 'success')


class Cart(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_that_product_was_added_to_cart(self):
        cart_title_text = self.find_element(cart_text).text
        return 'MacBook air' in cart_title_text

