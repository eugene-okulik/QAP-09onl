from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_first(driver):
    driver.get('https://www.demoblaze.com/index.html')
    samsung = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(samsung).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    name_product = driver.find_element(By.TAG_NAME, 'h2').text
    print(f'\nYou choosed: {name_product}')
    add_button = driver.find_element(By.CLASS_NAME, 'btn-success')
    add_button.click()
    sleep(2)  # for alert
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart_button = driver.find_element(By.ID, 'cartur')
    cart_button.click()
    basket = driver.find_element(By.CSS_SELECTOR, 'tr[class="success"]')
    products = basket.find_elements(By.TAG_NAME, 'td')
    your_product = products[1].text
    print(f'\nProduct in cart: {your_product}')
    assert name_product == your_product


def test_second(driver):
    driver.get('https://demoqa.com/menu#')
    main_menu = driver.find_element(By.ID, 'nav')
    main_items = main_menu.find_elements(By.TAG_NAME, 'li')
    main_item_2 = main_items[1]
    ActionChains(driver).move_to_element(main_item_2).perform()
    sub = main_item_2.find_elements(By.TAG_NAME, 'li')
    sub_sub = sub[2]
    ActionChains(driver).move_to_element(sub_sub).perform()
    sub_sub_items = sub_sub.find_elements(By.TAG_NAME, 'li')
    sub_sub_item_2 = sub_sub_items[1]
    ActionChains(driver).move_to_element(sub_sub_item_2).perform()
    sleep(1)


def test_third(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    prompt_box_button = driver.find_element(By.ID, 'promptexample')
    prompt_box_button.click()
    my_text = ('Something')
    Alert(driver).send_keys(my_text)
    Alert(driver).accept()
    sleep(3)  # for me to see
    alert_text = driver.find_element(By.ID, 'promptreturn').text
    print(f'\nYou asked me to write: {alert_text}')
    assert my_text == alert_text
