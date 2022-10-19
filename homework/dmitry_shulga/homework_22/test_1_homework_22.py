from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_basket(chrome_driver):
    chrome_driver.get("https://www.demoblaze.com/index.html")
    link_product = chrome_driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    ActionChains(chrome_driver).key_down(Keys.CONTROL).click(link_product).key_up(Keys.CONTROL).perform()
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    cart_button = chrome_driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    assert cart_button.is_displayed()
    cart_button.click()
    sleep(2)
    Alert(chrome_driver).accept()
    chrome_driver.close()
    sleep(2)
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    cart_button_main = chrome_driver.find_element(By.CSS_SELECTOR, 'a[href="cart.html"]')
    cart_button_main.click()
    sleep(2)
    product = chrome_driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert "Samsung galaxy s6" in product.text, "Invalid message"
    print(product.text)
    chrome_driver.quit()
