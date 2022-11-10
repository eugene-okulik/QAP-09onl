from pages.base_page import BasePage
from selenium.webdriver.common.by import By


go_to_our_stores = (By.CSS_SELECTOR, 'a[title="Our stores"]')
button_ok_on_map = (By.XPATH, '//*[@id="map"]/div[2]/table/tr/td[2]/button')
location = (By.XPATH, '//*[@id="addressInput"]')
button_search = (By.XPATH, '//*[@id="center_column"]/div[2]/div[3]/button/span')
radius = (By.XPATH, '//*[@id="radiusSelect"]', '25')


class OurStores(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def click_go_to_our_stores(self):
        self.find_element(go_to_our_stores).click()

    def click_button_ok_on_map(self):   # error on google map
        self.click_go_to_our_stores()
        self.find_element(button_ok_on_map).click()

    def search_location(self, city: str):
        self.find_element(location).send_keys(city)
        self.select_by_value(radius)
        self.find_element(button_search).click()

    def select_by_value(self, radius):
        pass
