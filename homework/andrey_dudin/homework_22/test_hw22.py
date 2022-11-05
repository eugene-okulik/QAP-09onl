import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep

def test_check_product_name_in_cart(driver):
    '''
    Первый тест
    https://www.demoblaze.com/index.html
    откройте товар в новой вкладке
    Перейдите на вкладку с товаром
    Добавьте товар в корзину
    Закройте вкладку с товаром
    На начальной вкладке откройте корзину
    Убедитесь, что в корзине тот товар, который вы добавляли
    '''
    driver.get('https://www.demoblaze.com/index.html')
    model=driver.find_element(By.LINK_TEXT, 'Nokia lumia 1520')
    ActionChains(driver).key_down(Keys.CONTROL).click(model).key_up(Keys.CONTROL).perform()
    driver.switch_to.window((driver.window_handles[1]))
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(2)"]').click()
    sleep(1)    # Waiting for Alert block
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window((driver.window_handles[0]))
    driver.find_element(By.ID, 'cartur').click()
    product=driver.find_element(By.CSS_SELECTOR, 'tr[class="success"]')
    product_name = ((product.find_elements(By.TAG_NAME, 'td'))[1]).text
    assert product_name=="Nokia lumia 1520"


def test_navigation(driver):
    '''
    https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 -
    здесь никакого ассерта не получится сделать
    '''
    driver.get('https://demoqa.com/menu#')
    main_item2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
    sub_sub_list = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
    sub_sub_item2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')
    ActionChains(driver).move_to_element(main_item2).move_to_element(sub_sub_list).move_to_element(sub_sub_item2).perform()
    sleep(3)


def test_text_in_prompt_box(driver):
    '''
    https://testpages.herokuapp.com/styled/alerts/alert-test.html
    Нажать на кнопку "Show prompt box", ввести в алерт какой-то ваш текст,
    нажать ок, проверить, что текст, который вы ввели появился под кнопкой
    '''
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    promt_box = driver.find_element(By.ID, 'promptexample')
    promt_box.click()
    Alert(driver).send_keys("Test text to prompt box")
    Alert(driver).accept()
    sleep(3)
    promt_value = driver.find_element(By.ID, 'promptreturn')
    assert promt_value.text=="Test text to prompt box"

