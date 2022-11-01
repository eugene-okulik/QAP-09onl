from pages.base_page import BasePage
from selenium.webdriver.common.by import By


dropdown_menu = (By.XPATH, '//select[@id="selectProductSort" and @class="selectProductSort form-control"]')
item = (By.XPATH, '//a[@class="product-name" and @itemprop="url"]')

delivery_link = (By.CSS_SELECTOR, 'a[title="Delivery"]')
delivery_text = (By.CLASS_NAME, "rte")

search_field = (By.ID, "search_query_top")
search_loupe = (By.NAME, "submit_search")

alert = (By.CLASS_NAME, "alert-warning")


class BestSellers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url1)

    def select_dropdown(self, text):
        self.select_dropdown_menu(dropdown_menu, text)

    def find_internal_text(self):
        elements = self.find_elements(item)
        text_item = []
        for i in range(len(elements)):
            text_item.append(elements[i].text)
        return text_item

    def click_delivery(self):
        self.find_element(delivery_link).click()

    def displayed_delivery_info(self):
        content = self.find_element(delivery_text)
        return content.is_displayed()

    def insert_text_in_search_field(self, word):
        self.find_element(search_field).send_keys(word)

    def click_search_loupe(self):
        self.find_element(search_loupe).click()

    def check_alert_block_text(self):
        alert_block = self.find_element(alert)
        return alert_block.text

    def check_alert_block_color(self):
        alert_block_color = self.find_element(alert).value_of_css_property('background-color')
        return alert_block_color
