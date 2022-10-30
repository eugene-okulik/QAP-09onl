from page.main_page import MainPage
from selenium.webdriver.common.by import By
from locators import selector as apl


class HomePage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_search_button(self):
        self.find_element(apl.search).click()

    def alert_message(self):
        return self.find_element(apl.alert_message)

    def click_our_stores_button(self):
        self.find_element(apl.our_stores).click()


    def click_about_us_button(self):
        self.find_element(apl.about_us).click()
