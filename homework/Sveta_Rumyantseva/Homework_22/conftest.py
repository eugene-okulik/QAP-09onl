from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    print('\nBEFORE TEST')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    print('\nAFTER TEST')
    driver.quit()
