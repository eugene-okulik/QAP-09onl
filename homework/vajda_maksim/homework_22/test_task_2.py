"""
Второй тест
https://demoqa.com/menu#

выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 - здесь никакого ассерта не получится сделать
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def test_demoqa(driver):
    driver.get('https://demoqa.com/menu#')
    sleep(3)  # Demo
    block = driver.find_element(By.CSS_SELECTOR, 'div[class="nav-menu-container"]')
    main_item2 = (block.find_elements(By.TAG_NAME, 'li'))[1]
    sub_sub_list = (main_item2.find_elements(By.TAG_NAME, 'li'))[2]
    sub_sub_item2 = (sub_sub_list.find_elements(By.TAG_NAME, 'li'))[1]
    ActionChains(driver).move_to_element(main_item2).move_to_element(sub_sub_list).move_to_element(sub_sub_item2).perform()
    sleep(3)  # Demo
