import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture(scope='function')
def driver():
    print('Before test')
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    sleep(3)
    yield chrome_driver
    print('after test')
    chrome_driver.quit()


@pytest.mark.simple
def test_aa1():
    print('test aa1')
    assert 1 == 1


@pytest.mark.hard
def test_nava(driver):
    print('testing nava')
    driver.get('https://demoblaze.com/')
    element = driver.find_element(By.ID, 'nava')
    assert element.is_displayed()


def test_signin2(driver):
    print('testing signin2')
    driver.get('https://demoblaze.com/')
    element = driver.find_element(By.ID, 'signin2')
    assert element.is_displayed()


@pytest.mark.simple
def test_aa2():
    print('test aa2')
    assert 2 == 2
