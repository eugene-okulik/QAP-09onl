from pages.home_page import HomePage
from pages.stores_page import StoresPage


def test_stores(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_our_stores_button()
    stores_page = StoresPage(driver)
    stores_page.scroll_page_to_bottom()
    stores_page.enter_searching_details('Minsk')
    assert stores_page.error_field_displayed()
