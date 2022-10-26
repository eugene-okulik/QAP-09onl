from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sort_by_select = (By.CSS_SELECTOR, 'select[id="selectProductSort"]')
sorted_text = (By.CSS_SELECTOR, 'div[id="uniform-selectProductSort"]')
grid_button = (By.CSS_SELECTOR, 'li[id="grid"]')
list_button = (By.CSS_SELECTOR, 'li[id="list"]')
selected_button = (By.CSS_SELECTOR, 'li[class="selected"]')


class BestSalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def sort_by(self, visible_text):
        self.select_by_visible_text(sort_by_select, visible_text)

    def sort_check(self):
        return self.find_element(sorted_text).text

    def click_grid_button(self):
        self.find_element(grid_button).click()

    def click_list_button(self):
        self.find_element(list_button).click()

    def check_selected_button(self):
        return self.find_element(selected_button).text
