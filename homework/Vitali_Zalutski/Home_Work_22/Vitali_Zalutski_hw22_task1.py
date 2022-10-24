# https://www.demoblaze.com/index.html
#
# 1.откройте товар в новой вкладке
# 2.Перейдите на вкладку с товаром
# 3.Добавьте товар в корзину
# 4.Закройте вкладку с товаром
# 5.На начальной вкладке откройте корзину
# 6.Убедитесь, что в корзине тот товар, который вы добавляли


from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_first(chrome_driver):
    chrome_driver.get('https://www.demoblaze.com/index.html')
    product_link = chrome_driver.find_element(By.CSS_SELECTOR, f'a[href="prod.html?idp_=1"]')
    ActionChains(chrome_driver).key_down(Keys.CONTROL).click(product_link).key_up(Keys.CONTROL).perform()
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    cart_button = chrome_driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    assert cart_button.is_displayed()
    cart_button.click()
    sleep(5)
    Alert(chrome_driver).accept()
    chrome_driver.close()
    sleep(5)
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    cart_button_new = chrome_driver.find_element(By.CSS_SELECTOR, f'a[href="cart.html"]')
    cart_button_new.click()
    sleep(2)
    product = chrome_driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert "Samsung galaxy s6" in product.text, "Invalid message"
    print(product.text)
    chrome_driver.quit()


