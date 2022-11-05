from page.home_page import HomePage
from page.best_sales_page import BestSalesPage


def test_check_top_sellers_text_value(driver):
    home_page = HomePage(driver)
    home_page.open_page() # open page http://automationpractice.com/
    home_page.scroll_page_to_bottom()
    home_page.click_best_sellers_link()
    best_sales = BestSalesPage(driver)
    assert best_sales.check_element_text() == 'TOP SELLERS'