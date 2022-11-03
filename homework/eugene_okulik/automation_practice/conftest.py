import pytest
import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    # sleep(3)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="function")
def test_data():
    with open('test_data.txt', 'r') as data_file:
        return json.load(data_file)
