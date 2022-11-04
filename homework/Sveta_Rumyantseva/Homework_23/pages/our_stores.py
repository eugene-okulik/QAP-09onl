from pages.base_page import BasePage
from selenium.webdriver.common.by import By

newsletter_field = (By.ID, "newsletter-input")
submit_button = (By.NAME, "submitNewsletter")


class OurStores(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url3)

    def fill_email_in_newsletters_field(self, email):
        self.find_element(newsletter_field).send_keys(email)  # insert address in newsletter field

    def click_submit_button(self):
        self.find_element(submit_button).click()
