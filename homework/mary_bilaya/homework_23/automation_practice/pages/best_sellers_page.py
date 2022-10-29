from pages.locators import best_sellers_locators as bsl
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

list_display_link = (By.CLASS_NAME, 'icon-th-list')
lowest_price_list = (By.CSS_SELECTOR, 'span[itemprop="price"]')
compare_button = (By.CSS_SELECTOR, 'button[type="submit"]')
add_to_compare_button = (By.CLASS_NAME, 'add_to_compare')
product_comparison = (By.CLASS_NAME, 'page-heading')


class SellersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_sort_by_field(self):
        select = Select(self.find_element(bsl.sort_by_field))
        select.select_by_visible_text('Price: Lowest first')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element(bsl.sort_by_field, 'Price: Lowest first'))

    def click_list_display_link(self):
        self.find_element(list_display_link).click()

    def click_add_to_compare(self):
        self.find_element(add_to_compare_button).click()

    def check_that_button_compare_is_worked(self):
        all_elements = self.find_elements(compare_button)
        button = all_elements[1]
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(compare_button))
        button.click()
        comparison = self.find_element(product_comparison).text
        return 'PRODUCT COMPARISON' in comparison









