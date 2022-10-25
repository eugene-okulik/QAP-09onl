import pytest
from pages.home_page import HomePage
from pages.best_sales_page import BestSalesPage
from time import sleep

TEST_DATA = ['--',
             'Price: Lowest first',
             'Price: Highest first',
             'Product Name: A to Z',
             'Product Name: Z to A',
             'In stock',
             'Reference: Lowest first',
             'Reference: Highest first']


@pytest.mark.parametrize('sort_by', TEST_DATA)
def test_sort_by_field(driver, sort_by):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_best_sales_button()
    best_sales_page = BestSalesPage(driver)
    best_sales_page.sort_by(sort_by)
    assert sort_by in best_sales_page.sort_check()


def test_view_change(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_best_sales_button()
    best_sales_page = BestSalesPage(driver)
    best_sales_page.click_list_button()
    assert best_sales_page.check_selected_button() == 'List'
    best_sales_page.click_grid_button()
    assert best_sales_page.check_selected_button() == 'Grid'
