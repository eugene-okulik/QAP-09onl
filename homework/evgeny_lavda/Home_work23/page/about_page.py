from page.main_page import MainPage
from selenium.webdriver.common.by import By
from locators import selector as apl


about_us_field = (By.CSS_SELECTOR, 'div[class="rte"]')


class AboutUsPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    def return_button(self):
        button = self.find_element(apl.return_to_home)
        return button.is_displayed()