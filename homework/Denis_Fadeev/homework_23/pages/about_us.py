from pages.base_page import BasePage
from selenium.webdriver.common.by import By


go_to_about_us = (By.CSS_SELECTOR, 'a[title="About us"]')
check_top_product = (By.XPATH, '//*[@id="center_column"]/div/div/div[1]/div/ul/li[1]')
check_best_customer_service = (By.XPATH, '//*[@id="center_column"]/div/div/div[1]/div/ul/li[2]')
check_money_back = (By.XPATH, '//*[@id="center_column"]/div/div/div[1]/div/ul/li[3]')


class AboutUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def click_go_to_about_us(self):
        self.find_element(go_to_about_us).click()

    def check_text(self):
        top_product = self.find_element(check_top_product)
        return 'Top quality products' in top_product.text
        best_customer_service = self.find_element(check_best_customer_service)
        return 'Best customer service' in best_customer_service.text
        money_back = self.find_element(check_money_back)
        return '30-days money back guarantee' in money_back.text
