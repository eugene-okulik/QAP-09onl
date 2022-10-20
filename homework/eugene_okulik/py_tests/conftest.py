import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    print('Before test')
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(30)
    # sleep(3)
    yield chrome_driver
    print('after test')
    chrome_driver.quit()
