from pages.home_page import HomePage
from selenium.webdriver.common.by import By


our_stores_text = (By.CLASS_NAME, "page-heading")
ok_button = (By.CLASS_NAME, "dismissButton")
search_button = (By.XPATH, "//button[@name='search_locations']")


class OurStoresPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_our_stores_page(self):
        self.open_page()
        self.click_our_stores_button()

    def check_our_stores_text(self):
        check_our_text = self.find_element(our_stores_text)
        return "OUR STORE(S)!" in check_our_text.text

    def check_button_ok(self):
        check_ok = self.find_element(ok_button)
        return check_ok.is_displayed()

    def click_button_ok(self):
        self.find_element(ok_button).click()

    def check_button_search(self):
        self.window_skroll()
        check_search = self.find_element(search_button)
        return check_search.is_displayed()



