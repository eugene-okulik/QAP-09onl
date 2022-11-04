from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from time import sleep


@pytest.fixture(scope='function')
def driver():
    print(f"\n{'-' * 45}Start testing{'-' * 45}")
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    print(f"\n{'-' * 45}Finish testing{'-' * 45}")
    chrome_driver.quit()
