from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from coftest import driver

# Первый тест
# https://www.demoblaze.com/index.html
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    phone = driver.find_element(By.LINK_TEXT, 'Nokia lumia 1520')
    ActionChains(driver).key_down(Keys.CONTROL).click(phone).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_button = driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(2)"]')
    add_button.click()
    sleep(3)
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart_button = driver.find_element(By.ID, 'cartur')
    cart_button.click()
    selected_phone = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert 'Nokia lumia 1520' in selected_phone.text


# Второй тест
# https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2
# - здесь никакого ассерта не получится сделать


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    main_item2 = driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]')
    sub_sub_list = driver.find_element(By.XPATH, '//a[text() = "SUB SUB LIST »"]')
    sub_sub_item2 = driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    ActionChains(driver).move_to_element(main_item2).move_to_element(sub_sub_list).move_to_element(
        sub_sub_item2).perform()

# Третий тест
# https://testpages.herokuapp.com/styled/alerts/alert-test.html
# Нажать на кнопку "Show prompt box", ввести в алерт какой-то ваш текст, нажать ок, проверить, что текст, который вы
# ввели появился под кнопкой.


def test_three(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    promt_box = driver.find_element(By.ID, 'promptexample')
    promt_box.click()
    Alert(driver).send_keys('test text')
    Alert(driver).accept()
    sleep(2)
    promt_text = driver.find_element(By.ID, 'promptreturn')
    assert 'test text' in promt_text.text
