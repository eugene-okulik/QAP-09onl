from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from time import sleep


def open_chrome():
    service = Service(executable_path='C:\\TMS\\chromedriver.exe')
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    return chrome_driver

def add_product (chrome_driver):
    chrome_driver.get('https://www.demoblaze.com/index.html')
    chrome_driver.implicitly_wait(20)
    product = chrome_driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    product.click()
    chrome_driver.implicitly_wait(20)
    add_cart_button = chrome_driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    add_cart_button.click()
    sleep(1)
    Alert(chrome_driver).accept()
    main_button = chrome_driver.find_element(By.CSS_SELECTOR, 'a[href="index.html"]')
    ActionChains(chrome_driver).key_down(Keys.CONTROL).click(main_button).key_up(Keys.CONTROL).perform()
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    chrome_driver.close()
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    cart_button = chrome_driver.find_element(By.ID, 'cartur')
    cart_button.click()
    product_done = chrome_driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert "Samsung galaxy s6" in product_done.text
    print(f'Add product in cart: {product_done.text}.')



chrome_driver = open_chrome()
add_product(chrome_driver)
chrome_driver.quit()
