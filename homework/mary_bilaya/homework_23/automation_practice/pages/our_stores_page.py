from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

your_location_field = (By.ID, 'addressInput')
search_button = (By.NAME, 'search_locations')
alert = (By.CLASS_NAME, 'fancybox-inner')


class OurStore(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_your_location(self, location):
        self.find_element(your_location_field).send_keys(location)
        self.find_element(search_button).click()
        # wait = WebDriverWait(self.driver, 20)
        # wait.until(EC.text_to_be_present_in_element(your_location_field, location),
        #            message='text is not presented in element')

    def check_that_alert_is_displayed(self, location):
        alert_message = self.find_element(alert)
        return f'{location} Not found' in alert_message.text

