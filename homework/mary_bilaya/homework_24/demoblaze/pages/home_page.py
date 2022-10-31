from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

sign_up_link = (By.ID, 'signin2')
log_in_link = (By.ID, 'login2')
cart_link = (By.ID, 'cartur')
laptops_link = (By.CLASS_NAME, 'list-group-item')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_sign_up_link(self):
        self.find_element(sign_up_link).click()

    def click_log_in_link(self):
        self.find_element(log_in_link).click()

    def click_cart_link(self):
        self.find_element(cart_link).click()

    def click_laptops_link(self):
        list_of_link = self.find_elements(laptops_link)
        laptops = list_of_link[2]
        self.scroll_to_the_bottom_of_page()
        sleep(3)    # for demonstration purposes
        laptops.click()



