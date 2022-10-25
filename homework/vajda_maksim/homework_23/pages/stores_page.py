from pages.base_page import BasePage
from selenium.webdriver.common.by import By

your_location_field = (By.CSS_SELECTOR, 'input[class="form-control grey"]')
radius_select = (By.CSS_SELECTOR, 'select[name="radius"]')
search_button = (By.CSS_SELECTOR, 'button[name="search_locations"]')
error_block = (By.CSS_SELECTOR, 'p[class="fancybox-error"]')


class StoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def your_location_search(self, my_location, visible_text):
        self.find_element(your_location_field).send_keys(my_location)
        self.select_by_visible_text(radius_select, visible_text)
        self.find_element(search_button).click()

    def check_error(self):
        return self.find_element(error_block).is_displayed()
