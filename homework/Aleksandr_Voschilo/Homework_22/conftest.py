import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    # print('Before test')
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    # print('After test')
    # chrome_driver.quit()


@pytest.fixture(scope='session')
def all_tests():
    print('\nBefore all tests')
    yield None
    print('\nAfter all tests')


@pytest.fixture(scope='function')
def each_test():
    print('\nBefore test')
    yield None
    print('\nAfter test')
