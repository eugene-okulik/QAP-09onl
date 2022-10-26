import pytest
from pages.home_page import HomePage
from pages.best_sellers_page import SellersPage

CREDENTIALS = ['Price: Lowest first', 'Price: Highest first',
               'Product Name: A to Z', 'Product Name: Z to A', 'In stock',
               'Reference: Lowest first', 'Reference: Highest first']


@pytest.mark.parametrize('select_choice', CREDENTIALS)
def test_best_sellers(driver, select_choice):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_best_sellers()
    best_sellers = SellersPage(driver)
    # sleep(3)    # for demonstration purposes
    best_sellers.select_sort_by_field(select_choice=select_choice)





