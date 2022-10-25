from pages.about_us_page import AboutUs
from pages.home_page import HomePage


def test_about_us_page(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_about_us()
    about_us_page = AboutUs(driver)
    about_us_page.the_rules_is_displayed()
