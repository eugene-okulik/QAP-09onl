from pages.home_page import HomePage
from pages.about_us_page import AboutUsPage


def test_about_us(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_about_us_button()
    about_us_page = AboutUsPage(driver)
    assert about_us_page.our_company_info_displayed()
