from page.home_page import HomePage
from page.about_page import AboutUsPage


def test_error_message(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_about_us_button()
    about_page = AboutUsPage(driver)
    assert about_page.return_button()
