import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path='C:\\chromedriver.exe')


@pytest.fixture(scope='session')
def driver():
    print('Before test')
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options, service=service)
    sleep(5)
    yield chrome_driver
    chrome_driver.quit()
    print(' code off')


@pytest.mark.simple
def test_simple_1():
    print('Before Testing "test_simple_1"')
    assert 5 == 5
    print('After Testing "test_simple_1"')


@pytest.mark.hard
def test_go_to_site(driver):
    print('Testing button "contact_us"')
    driver.get('http://automationpractice.com/index.php')
    element_button = driver.find_element(By.ID, 'contact-link')
    element_button.click()
    sleep(3)
    print('After Testing')


@pytest.mark.skip("this code is incomplete")
def test_simple_2():
    print('Before Testing "test_simple_2"')
    assert 15 != 10


