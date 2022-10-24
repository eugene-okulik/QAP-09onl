from pages.home_page import HomePage
from pages.best_sales_page import BestSalesPage


def test_best_sales(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_best_sellers_button()
    best_sales_page = BestSalesPage(driver)
    best_sales_page.select_lowest_first_price()
    assert best_sales_page.price_lowest_first_in_sort_by_field_displayed()




