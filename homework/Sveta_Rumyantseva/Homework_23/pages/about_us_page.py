from pages.base_page import BasePage
from selenium.webdriver.common.by import By

parts = (By.CLASS_NAME, "page-subheading")
house_icon = (By.CLASS_NAME, "icon-home")
women_menu = (By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?id_category=3&controller=category"]')
top_menu = (By.XPATH, '//a[@class="sf-with-ul" '
                      'and @href="http://automationpractice.com/index.php?id_category=4&controller=category"]')


class AboutUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url2)

    def find_text_in_elements(self):
        elements = self.find_elements(parts)
        text_elements = []
        for i in range(len(elements)):
            text_elements.append(elements[i].text)
        return text_elements

    def click_house_icon(self):
        self.find_element(house_icon).click()  # return to a home page

    def click_top_menu(self):
        self.actions_chains(women_menu, top_menu)  # click a top in the pop-up menu: women->top
