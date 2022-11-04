from time import sleep
import pytest
from pages.best_sales_page import BestSalesPage


def test_button_enabled(driver):
    best_sales = BestSalesPage(driver)
    best_sales.open_page()
    best_sales.click_best_sallers()
    best_sales.click_product()
    best_sales.click_button_add_to_card()
    assert best_sales.button_priceed_to_checkout().is_enabled()

