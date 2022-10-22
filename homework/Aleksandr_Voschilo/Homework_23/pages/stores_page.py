from pages.base_page import BasePage
from selenium.webdriver.common.by import By


your_location_field = (By.ID, 'addressInput')
radius_field = (By.ID, 'radiusSelect', '50')
search_button = (By.NAME, 'search_locations')
error_field = (By.CLASS_NAME, 'fancybox-error')


class StoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_searching_details(self, city: str):
        self.find_element(your_location_field).send_keys(city)
        self.select_by_value(radius_field)
        self.find_element(search_button).click()

    def error_field_displayed(self):
        error = self.find_element(error_field)
        return error.is_displayed()
