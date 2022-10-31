from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from time import sleep
from pages.locators import our_stores_locators as osl


class OurStore(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_your_location_data(self, location):
        self.find_element(osl.your_location_field).send_keys(location)
        sleep(3)    # for demonstration purposes

    def select_radius(self, radius):
        select = Select(self.find_element(osl.radius_field))
        select.select_by_value(radius)

    def click_search_button(self):
        self.find_element(osl.search_button).click()

    def check_that_alert_message_is_displayed(self, location):
        alert_message_text = self.find_element(osl.alert).text
        return f'{location} Not found' in alert_message_text

