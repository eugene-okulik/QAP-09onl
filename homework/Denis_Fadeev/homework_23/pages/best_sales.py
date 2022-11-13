from pages.base_page import BasePage
from selenium.webdriver.common.by import By

go_to_best_sales = (By.CSS_SELECTOR, 'a[title="Best sellers"]')
clothes_by_in_stock = (By.ID, 'selectProductSoft')
in_stock = (By.CLASS_NAME, "In stock")
more_cloth = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[2]/span')
check_price = (By.XPATH, '//*[@id="our_price_display"]')


class BestSales(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def click_go_to_best_sales(self):
        self.find_element(go_to_best_sales).click()

    def open_in_stock(self):
        self.find_element(clothes_by_in_stock)
        self.select_by_text(in_stock)
        self.find_element(more_cloth)
        price = self.find_element(check_price)
        return '$28.98' in price.text

    def select_by_text(self, in_stock):
        pass
