from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import pytest


def test1(driver):
    driver.get('https://www.demoblaze.com/')
    sleep(2)
    lumia = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/div/h4/a')
    ActionChains(driver).key_down(Keys.CONTROL).click(lumia).key_up(Keys.CONTROL).perform()
    tab = driver.window_handles
    driver.switch_to.window(tab[1])
    sleep(2)
    name = driver.find_element(By.XPATH, "//*[contains(@class,'name')]").text
    print(f" chose: {name}")
    add_button = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    add_button.click()
    sleep(5)
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(tab[0])
    cart_button = driver.find_element(By.XPATH, '//*[@id="cartur"]')
    cart_button.click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    name1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text
    print(f"Product in cart: {name1}")
    assert name == name1


def test2(driver):
    driver.get('https://demoqa.com/menu#')
    button = driver.find_element(By.ID, 'nav')
    main_items = button.find_elements(By.TAG_NAME, 'li')
    main_item_2 = main_items[1]
    main_item_2_buttons = main_item_2.find_elements(By.TAG_NAME, 'li')
    sub_sub_list = main_item_2_buttons[2]
    sub_sub_list_buttons = sub_sub_list.find_elements(By.TAG_NAME, 'li')
    sub_sub_item_2 = sub_sub_list_buttons[1]
    ActionChains(driver).move_to_element(main_item_2).move_to_element(sub_sub_list).click(sub_sub_item_2).perform()
    sleep(0.5)


def test3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    prompt_box_button = driver.find_element(By.ID, 'promptexample')
    prompt_box_button.click()
    my_text = ('Something')
    Alert(driver).send_keys(my_text)
    Alert(driver).accept()
    sleep(5)
    alert_text = driver.find_element(By.ID, 'promptreturn').text
    print(f'\nYou asked me to write: {alert_text}')
    assert my_text == alert_text
