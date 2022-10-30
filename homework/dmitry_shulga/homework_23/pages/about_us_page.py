from pages.home_page import HomePage
from selenium.webdriver.common.by import By


about_us_text = (By.CLASS_NAME, "rte")
our_company_text = (By.XPATH, "//h3[text() = 'Our company']")
our_team_text = (By.XPATH, "//h3[text() = 'Our team']")


class AboutUsPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_about_us_page(self):
        self.open_page()
        self.click_about_us_button()

    def check_about_us_text(self):
        check_about_text = self.find_element(about_us_text)
        return "ABOUT US" in check_about_text.text

    def check_our_company_text(self):
        check_our_company_text = self.find_element(our_company_text)
        return "OUR COMPANY" in check_our_company_text.text

    def check_our_team_text(self):
        check_our_team_text = self.find_element(our_team_text)
        return "OUR TEAM" in check_our_team_text.text
