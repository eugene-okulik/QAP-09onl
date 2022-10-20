"""
Третий тест
https://testpages.herokuapp.com/styled/alerts/alert-test.html

Нажать на кнопку "Show prompt box", ввести в алерт какой-то ваш текст,
нажать ок, проверить, что текст, который вы ввели появился под кнопкой.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_testpages(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    key = 'BELARUS'
    driver.find_element(By.CSS_SELECTOR, 'input[id="promptexample"]').click()
    Alert(driver).send_keys(key)
    Alert(driver).accept()
    prompt_text = driver.find_element(By.CSS_SELECTOR, 'p[id="promptreturn"]').text
    assert key == prompt_text
