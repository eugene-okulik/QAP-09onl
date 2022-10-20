"""
Первый тест
https://www.demoblaze.com/index.html

1. откройте товар в новой вкладке
2. Перейдите на вкладку с товаром
3. Добавьте товар в корзину
4. Закройте вкладку с товаром
5. На начальной вкладке откройте корзину
6. Убедитесь, что в корзине тот товар, который вы добавляли
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep


def test_demoblaze(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.CSS_SELECTOR, 'a[class="hrefch"]')
    product_name = product.text
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    driver.switch_to.window((driver.window_handles[1]))
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]').click()
    sleep(3)    # Waiting for Alert block
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window((driver.window_handles[0]))
    driver.find_element(By.CSS_SELECTOR, 'a[id="cartur"]').click()
    block = driver.find_element(By.CSS_SELECTOR, 'tr[class="success"]')
    product_in_cart = ((block.find_elements(By.TAG_NAME, 'td'))[1]).text
    assert product_in_cart == product_name
