from pages.best_sales import BestSales


def test_page_best_sales(driver):
    best_sales = BestSales(driver)
    best_sales.open_page()
    best_sales.click_go_to_best_sales()
    best_sales.open_in_stock()

