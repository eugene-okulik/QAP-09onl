from pages.best_sellers_page import BestSellersPage
from time import sleep


def test_best_sellers(chrome_driver):
    best_sellers = BestSellersPage(chrome_driver)
    best_sellers.open_best_sellers_page()
    best_sellers.sort_by()
    assert best_sellers.sort_by_text()
    print(best_sellers.sort_by_text())
    best_sellers.add_to_compare()
    assert best_sellers.check_compare()
    print(best_sellers.check_compare())
    best_sellers.add_to_cart()
    sleep(5)
    assert best_sellers.proceed_to_checkout_button()
    print(best_sellers.proceed_to_checkout_button())
    chrome_driver.quit()

