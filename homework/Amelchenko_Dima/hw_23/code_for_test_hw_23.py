from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def open_best_sellers(driver):
    driver.get("http://automationpractice.com/index.php?controller=best-sales")


def open_our_stores(driver):
    driver.get("http://automationpractice.com/index.php?controller=stores")


def open_about_us(driver):
    driver.get("http://automationpractice.com/index.php?id_cms=4&controller=cms")


def find_add_to_compare(driver):
    return driver.find_element(By.CLASS_NAME, 'add_to_compare')


def find_compare(driver):
    return driver.find_element(By.CLASS_NAME, 'compare-form')


def check_compare(compare, driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(compare))
    assert compare.is_enabled()


def find_search_box(driver):
    return driver.find_element(By.ID, 'searchbox')


def find_our_company(driver):
    return driver.find_element(By.CLASS_NAME, 'page-subheading')
