from pages.base_page import BasePage
from selenium.webdriver.common.by import By


sort_by_field = (By.ID, 'uniform-selectProductSort')
sort_by_select_field = (By.ID, 'selectProductSort', 'Price: Lowest first')


class BestSalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_lowest_first_price(self):
        self.select_by_text(sort_by_select_field)

    def price_lowest_first_in_sort_by_field_displayed(self):
        sort_by = self.find_element(sort_by_field)
        sort_by_select = sort_by.find_element(By.TAG_NAME, 'span')
        return 'Price: Lowest first' in sort_by_select.text

