from pages.home_page import HomePage
from pages.laptops_page import Laptops
from pages.cart_page import Cart
from time import sleep
import allure


@allure.feature('laptops page')
@allure.story('choice')
def test_laptops_page(driver):
    home_page = HomePage(driver)
    with allure.step('open home page'):
        home_page.open_page()
    with allure.step('click laptops link'):
        home_page.click_laptops_link()
    sleep(3)    # for demonstration purposes
    laptops_page = Laptops(driver)
    with allure.step('click mac book air'):
        laptops_page.click_mac_book_air()
    with allure.step('add mac book air to cart'):
        laptops_page.add_to_cart_air()
    sleep(3)  # for demonstration purposes
    with allure.step('check that alert message is displayed'):
        assert laptops_page.check_alert_message()
    with allure.step('accept alert message'):
        laptops_page.accept_alert_message()
    with allure.step('go to cart page'):
        laptops_page.go_to_cart_page()
    sleep(3)  # for demonstration purposes
    cart = Cart(driver)
    with allure.step('check that product was added to cart'):
        assert cart.check_that_product_was_added_to_cart()






