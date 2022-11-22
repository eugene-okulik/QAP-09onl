from pages.base_page import BasePage
from selenium.webdriver.common.by import By


sort_by_field = (By.ID, 'uniform-selectProductSort')
sort_by_select_field = (By.ID, 'selectProductSort', 'Product Name: A to Z')


class BestSalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_product_name(self):
        self.select_by_text(sort_by_select_field)

    def select_product_name_is_displayed(self):
        sort_by = self.find_element(sort_by_field)
        sort_by_select = sort_by.find_element(By.TAG_NAME, 'span')
        return 'Product Name: A to Z' in sort_by_select.text