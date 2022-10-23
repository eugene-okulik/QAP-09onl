# Второй тест
# https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 - здесь никакого ассерта не получится сделать


from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_move_to(chrome_driver):
    chrome_driver.get('https://demoqa.com/menu#')
    main_item = chrome_driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]')
    move_to_sub = chrome_driver.find_element(By.XPATH, '//a[text() = "SUB SUB LIST »"]')
    move_to_sub_2 = chrome_driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    ActionChains(chrome_driver).move_to_element(main_item).move_to_element(move_to_sub).move_to_element(move_to_sub_2).click()
    sleep(3)
