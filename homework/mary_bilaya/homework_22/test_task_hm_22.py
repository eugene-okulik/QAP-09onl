from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep

# Test_task_1. https://www.demoblaze.com/index.html
#
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли


def test_task_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    product_text = product.text
    print("product text:", product_text)
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    sleep(3)    # for demonstration purposes
    print("window handles:", driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    btn_add_to_cart = driver.find_element(By.LINK_TEXT, 'Add to cart')
    assert btn_add_to_cart.is_displayed()
    btn_add_to_cart.click()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    btn_cart = driver.find_element(By.ID, 'cartur')
    btn_cart.click()
    assert 'Samsung galaxy s6' == product_text


# Test_task_2. https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 - здесь никакого ассерта
# не получится сделать

# Женя, не знаю в чем моя ошибка, но когда я запускаю ActionChains в одну строку, тест падает


def test_task_two(driver):
    driver.get('https://demoqa.com/menu# ')
    main_btn_block = driver.find_element(By.ID, 'nav')
    main_items = main_btn_block.find_elements(By.TAG_NAME, 'li')
    main_item_2 = main_items[1]
    sub_items = main_item_2.find_elements(By.TAG_NAME, 'li')
    sub_sub_list = sub_items[2]
    sub_sub_items = sub_sub_list.find_elements(By.TAG_NAME, 'li')
    sub_sub_item_2 = sub_sub_items[1]
    actions = ActionChains(driver)
    actions.move_to_element(main_item_2)
    actions.move_to_element(sub_sub_list)
    actions.click(sub_sub_item_2)
    # ActionChains(driver).move_to_element(main_item_2).move_to_element(sub_sub_list).click(sub_sub_item_2).perform()
    sleep(5)    # for demonstration purposes


# Test_task_3. https://testpages.herokuapp.com/styled/alerts/alert-test.html
# Нажать на кнопку "Show prompt box", ввести в алерт какой-то ваш текст, нажать ок, проверить, что текст,
# который вы ввели появился под кнопкой.


def test_task_three(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    btn_show_prompt_box = driver.find_element(By.ID, 'promptexample')
    btn_show_prompt_box.click()
    sleep(3)    # for demonstration purposes
    Alert(driver).send_keys('alert text')
    print(Alert(driver).text)
    sleep(3)    # for demonstration purposes
    Alert(driver).accept()
    check_text = driver.find_element(By.ID, 'promptreturn').text
    assert 'alert text' in check_text


