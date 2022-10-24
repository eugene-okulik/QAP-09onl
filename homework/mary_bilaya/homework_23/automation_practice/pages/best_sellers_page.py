from pages.locators import best_sellers_locators as bsl
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SellersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_sort_by_field(self, select_choice):
        select = Select(self.find_element(bsl.sort_by_field))
        select.select_by_visible_text(select_choice)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element(bsl.sort_by_field, select_choice))





