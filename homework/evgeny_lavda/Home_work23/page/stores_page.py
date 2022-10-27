from page.main_page import MainPage
from locators import selector as apl


class StoresPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_serch_botton(self):
        self.find_element(apl.search_button).click()

    def error_message_displayed(self):
        error = self.find_element(apl.error_message)
        return error.is_displayed()
