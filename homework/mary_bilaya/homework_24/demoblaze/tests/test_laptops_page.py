from pages.home_page import HomePage
from pages.laptops_page import Laptops
from time import sleep


def test_laptops_page(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_laptops_link()
    sleep(3)    # for demonstration purposes
    laptops_page = Laptops(driver)
    laptops_page.click_mac_book_air()
    laptops_page.add_to_cart_air()
    sleep(3)  # for demonstration purposes
    assert laptops_page.check_alert_message()
    laptops_page.accept_alert_message()
    laptops_page.go_to_home_page()
    sleep(3)  # for demonstration purposes




