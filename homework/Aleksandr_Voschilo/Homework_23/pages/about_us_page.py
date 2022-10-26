from pages.base_page import BasePage
from selenium.webdriver.common.by import By


our_company_field = (By.CLASS_NAME, 'cms-block')


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def our_company_info_displayed(self):
        our_company = self.find_element(our_company_field)
        return 'OUR COMPANY' in our_company.text
