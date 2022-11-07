from pages.base_page import BasePage
from selenium.webdriver.common.by import By

our_team_field = (By.XPATH, "//h3[text() = 'Our team']")


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def our_company_info_displayed(self):
        our_team = self.find_element(our_team_field)
        return 'OUR TEAM' in our_team.text
