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


def task1(driver):
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
    driver.quit()


def task2(driver):
    driver.get('https://demoqa.com/menu#')

    main_item_2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
    main_item_2.click()

    sub_sub_list = driver.find_element(By.XPATH, '//*[@id="nav"]//li[3]/a')
    sub_sub_list.click()

    sud_sub_item_2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')
    sud_sub_item_2.click()

    driver.quit()


def task3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')

    text = 'Funny ducks'

    show_prompt_box = driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()

    Alert(driver).send_keys(text)
    Alert(driver).accept()

    check_text = driver.find_element(By.ID, 'promptreturn').text

    assert check_text == text


driver = driver()
task1(driver)
task2(driver)
task3(driver)
driver.quit()