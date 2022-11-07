from pages.about_us_page import AboutUsPage
from time import sleep
import allure


@allure.feature('information section')
@allure.story('about_us')
def test_img_is_displayed(driver):
    img_about_us = AboutUsPage(driver)
    with allure.step('Open home page'):
        img_about_us.open_page()
    with allure.step('Click about us button'):
        img_about_us.click_about_us()
    with allure.step('Check that picture of our team is displayed'):
        assert img_about_us.check_img_our_team().is_displayed()


@allure.feature('information section')
@allure.story('about_us')
def test_icon_home_is_enabled(driver):
    icon_about_us = AboutUsPage(driver)
    icon_about_us.open_page()
    icon_about_us.click_about_us()
    assert icon_about_us.check_icon_home().is_enabled()
