from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


def open_chrome():
    options = Options()
    # options.add_argument('start-maximized')
    # options.add_argument('window-size=2048,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def check_contact_us_form(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_links = driver.find_elements(By.LINK_TEXT, 'Contact us')
    contact_us_links[1].click()
    select = Select(driver.find_element(By.ID, 'id_contact'))
    select.select_by_visible_text('Webmaster')
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email_field.send_keys('pawel.malashko@yandex.ru')
    order_ref = driver.find_element(By.NAME, 'id_order')
    order_ref.send_keys('http://automationpractice.com/index.php?id_product=1&controller=product')
    message = driver.find_element(By.NAME, 'message')
    message.send_keys('I have some problem with this item')
    upload_file = driver.find_element(By.NAME, 'fileUpload')
    upload_file.send_keys("C:\\Users\\Pavel\\photo.jpg")
    sleep(3)
    email_field.send_keys(Keys.ENTER)
    alert_success = driver.find_element(By.CLASS_NAME, 'alert-success')
    print(alert_success.text)
    sleep(5)


driver = open_chrome()
check_contact_us_form(driver)
driver.quit()
