import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def chrome_driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
