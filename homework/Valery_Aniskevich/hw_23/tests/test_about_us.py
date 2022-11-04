from pages.about_us_page import AboutUsPage
from time import sleep


def test_img_is_displayed(driver):
    img_about_us = AboutUsPage(driver)
    img_about_us.open_page()
    img_about_us.click_about_us()
    assert img_about_us.check_img_our_team().is_displayed()


def test_icon_home_is_enabled(driver):
    icon_about_us = AboutUsPage(driver)
    icon_about_us.open_page()
    icon_about_us.click_about_us()
    assert icon_about_us.check_icon_home().is_enabled()
