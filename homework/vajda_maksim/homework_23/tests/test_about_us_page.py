import pytest
from pages.home_page import HomePage
from pages.about_us_page import AboutUsPage

TEST_DATA = ['OUR COMPANY', 'OUR TEAM', 'TESTIMONIALS']


@pytest.mark.parametrize('info', TEST_DATA)
def test_about_us_info(driver, info):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_about_us_button()
    about_us_page = AboutUsPage(driver)
    assert about_us_page.about_us_info(info)

