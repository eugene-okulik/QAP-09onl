from page.home_page import HomePage
from page.stores_page import StoresPage


def test_error_message(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_our_stores_button()
    stores_page = StoresPage(driver)
    stores_page.click_serch_botton()
    assert stores_page.error_message_displayed()
