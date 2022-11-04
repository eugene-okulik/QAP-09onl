from pages.base_page import BasePage
from locators import all_locators as apl


class BestSalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_best_sallers(self):
        self.find_element(apl.best_sallers).click()

    def click_product(self):
        self.find_elements(apl.products)[0].click()

    def click_button_add_to_card(self):
        self.find_element(apl.add_to_card_button).click()

    def button_priceed_to_checkout(self):
        return self.find_element(apl.proceed_to_checkout)
