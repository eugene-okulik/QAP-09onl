from selenium.webdriver.common.by import By


def open_main_page(driver):
    driver.get('https://demoblaze.com/')


def find_navigation(driver):
    return driver.find_element(By.ID, 'nava')


def check_that_navigation_is_displayed(navigation):
    assert navigation.is_displayed()