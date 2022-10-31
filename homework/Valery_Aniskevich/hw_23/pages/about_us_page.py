from pages.base_page import BasePage
from locators import all_locators as apl


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_about_us(self):
        self.find_element(apl.about_us).click()

    def check_img_our_team(self):
        return self.find_element(apl.img_our_team)

    def check_icon_home(self):
        return self.find_element(apl.icon_home)
