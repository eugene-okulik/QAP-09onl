import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
from conftest import driver


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    link = driver.find_element(By.LINK_TEXT, 'Nexus 6')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    driver.switch_to.window((driver.window_handles[1]))
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(3)"]').click()
    sleep(1)
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    product = driver.find_element(By.CSS_SELECTOR, 'tr[class="success"]')
    product_name = ((product.find_elements(By.TAG_NAME, 'td'))[1]).text
    assert product_name == "Nexus 6"


def test_2(driver):
    driver.get('https://demoqa.com/menu#')
    main_item2 = driver.find_element(By.XPATH, '//a[text()="Main Item 2"]')
    sub_sub_list = driver.find_element(By.XPATH, '//a[text()="SUB SUB LIST »"]')
    sub_sub_item2 = driver.find_element(By.XPATH, '//a[text()="Sub Sub Item 2"]')
    ActionChains(driver).move_to_element(main_item2).move_to_element(sub_sub_list).move_to_element(
        sub_sub_item2).perform()


def test_3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.find_element(By.ID, 'promptexample').click()
    Alert(driver).send_keys('Some text')
    Alert(driver).accept()
    assert driver.find_element(By.ID, 'promptreturn').text == 'Some text'
