from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# the_first_rule = (By.NAME, 'Top quality products')
# the_second_rule = (By.NAME, 'Best customer service')
# the_third_rule = (By.NAME, '30-days money back guarantee')
list_of_rules = (By.CLASS_NAME, 'list-1')
rules = (By.TAG_NAME, 'li')
image = (By.CSS_SELECTOR, 'img[title="cms-img"]')
testimonials_text = (By.CLASS_NAME, 'testimonials')


class AboutUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def our_team_image_is_displayed(self):
        return self.find_element(image).is_displayed()

    def testimonials_text_is_displayed(self):
        return self.find_element(testimonials_text).is_displayed()




