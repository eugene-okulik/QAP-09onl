from page.home_page import HomePage
from page.stores_page import StoresPage


def test_check_phone_number_value(driver):
    home_page = HomePage(driver)
    home_page.open_page() # open page http://automationpractice.com/
    home_page.scroll_page_to_bottom()
    home_page.click_stores_link()
    phone_number = StoresPage(driver)
    assert phone_number.check_element_text() == '0123-456-789'