from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver_chrome = webdriver.Chrome(options=options)
    driver_chrome.implicitly_wait(10)
    return driver_chrome


def cart_task1(driver):
    driver.get('https://www.demoblaze.com/index.html')

    samsung_galaxy_s6 = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(samsung_galaxy_s6).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart = driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    add_to_cart.click()

    expectation_alert = WebDriverWait(driver, 10)
    expectation_alert.until(EC.alert_is_present())
    Alert(driver).accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    open_cart = driver.find_element(By.ID, 'cartur')
    open_cart.click()

    check_cart = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    driver.implicitly_wait(10)
    assert check_cart.text == 'Samsung galaxy s6'
    print('Device "Samsung galaxy s6" added to cart')


driver = driver()
cart_task1(driver)
driver.quit()
