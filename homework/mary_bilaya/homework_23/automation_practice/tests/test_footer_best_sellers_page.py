from pages.home_page import HomePage
from pages.best_sellers_page import SellersPage
from time import sleep


def test_best_sellers(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_best_sellers()
    best_sellers = SellersPage(driver)
    sleep(3)    # for demonstration purposes
    best_sellers.select_sort_by_field()
    best_sellers.click_list_display_link()
    best_sellers.click_add_to_compare()
    assert best_sellers.check_that_button_compare_is_worked()
    sleep(3)    # for demonstration purposes





