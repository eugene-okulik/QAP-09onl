from pages.about_us_page import AboutUs
from pages.home_page import HomePage


def test_about_us_page(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_about_us()
    about_us_page = AboutUs(driver)
    assert about_us_page.our_team_image_is_displayed()
    assert about_us_page.testimonials_text_is_displayed()