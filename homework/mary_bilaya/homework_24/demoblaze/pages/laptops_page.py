from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

mac_book_air = (By.CLASS_NAME, 'hrefch')
add_to_cart_air = (By.CSS_SELECTOR, 'a[onclick="addToCart(11)"]')
home_link = (By.CLASS_NAME, 'nav-link')


class Laptops(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_mac_book_air(self):
        laptops = self.find_elements(mac_book_air)
        air = laptops[2]
        self.scroll_to_the_bottom_of_page()
        air.click()

    def add_to_cart_air(self):
        self.find_element(add_to_cart_air).click()

    def check_alert_message(self):
        return 'Product added' in Alert(self.driver).text

    def accept_alert_message(self):
        Alert(self.driver).accept()

    def go_to_home_page(self):
        all_links = self.find_elements(home_link)
        home = all_links[0].click()
        self.scroll_to_the_bottom_of_page()

