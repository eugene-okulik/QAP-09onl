import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=2"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    my_product = driver.find_element(By.TAG_NAME, 'h2').text
    print(f"I chose: {my_product}")
    cart_button = driver.find_element(By.CLASS_NAME, 'btn-success')
    cart_button.click()
    sleep(1)  # need for alert window
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    main_cart_button = driver.find_element(By.ID, 'cartur')
    main_cart_button.click()
    find_product_name = driver.find_element(By.CSS_SELECTOR, 'tr[class="success"]')
    find_name = find_product_name.find_elements(By.TAG_NAME, 'td')
    product_in_cart = find_name[1].text
    print(f"Product in cart: {product_in_cart}")
    assert my_product == product_in_cart


def test_2(driver):
    driver.get('https://demoqa.com/menu#')
    button = driver.find_element(By.ID, 'nav')
    main_items = button.find_elements(By.TAG_NAME, 'li')
    main_item_2 = main_items[1]
    main_item_2_buttons = main_item_2.find_elements(By.TAG_NAME, 'li')
    sub_sub_list = main_item_2_buttons[2]
    sub_sub_list_buttons = sub_sub_list.find_elements(By.TAG_NAME, 'li')
    sub_sub_item_2 = sub_sub_list_buttons[1]
    ActionChains(driver).move_to_element(main_item_2).move_to_element(sub_sub_list).click(sub_sub_item_2).perform()
    sleep(0.5)  # demonstrative


def test_3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    show_promt_box = driver.find_element(By.ID, 'promptexample')
    show_promt_box.click()
    my_text = "I love Selenium"
    Alert(driver).send_keys(my_text)
    Alert(driver).accept()
    check_text = driver.find_element(By.ID, 'promptreturn').text
    assert check_text == my_text



