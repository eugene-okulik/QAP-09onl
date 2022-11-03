from pages.about_us import AboutUs


def test_page_about_us(driver):
    about_us = AboutUs(driver)
    about_us.open_page()
    about_us.click_go_to_about_us()
    about_us.check_text()

