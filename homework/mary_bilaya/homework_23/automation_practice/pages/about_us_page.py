from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# the_first_rule = (By.NAME, 'Top quality products')
# the_second_rule = (By.NAME, 'Best customer service')
# the_third_rule = (By.NAME, '30-days money back guarantee')
block_of_rules = (By.CLASS_NAME, 'list-1')
rules = (By.TAG_NAME, 'li')


class AboutUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def the_rules_is_displayed(self):
        all_block_rules = self.find_element(block_of_rules)
        # all_rules = all_block_rules.find_elements(rules)



