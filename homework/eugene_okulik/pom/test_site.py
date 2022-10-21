from selenium.webdriver.common.by import By
import code_for_test_site as runner


def test_nava(driver):
    print('testing nava')
    runner.open_main_page(driver)
    navigation = runner.find_navigation(driver)
    runner.check_that_navigation_is_displayed(navigation)