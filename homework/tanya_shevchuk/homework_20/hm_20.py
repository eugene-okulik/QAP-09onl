from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def contact_form(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    sleep(3)
    subject_heading = Select(driver.find_element(By.ID, 'id_contact'))
    subject_heading.select_by_visible_text('Customer service')
    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys('aaa111@gmail.com')
    order_reference = driver.find_element(By.ID, 'id_order')
    order_reference.send_keys('aaa111')
    message_field = driver.find_element(By.ID, 'message')
    message_field.send_keys('test hello')
    attach_file = driver.find_element(By.ID, 'fileUpload')
    attach_file.send_keys('C:\\Users\\shevt\\test_photo.jpg')
    send_button = driver.find_element(By.ID, 'submitMessage')
    send_button.click()
    alert_success = driver.find_element(By.CLASS_NAME, 'alert-success').text
    print(alert_success)

driver = open_chrome()
contact_form(driver)
driver.quit()
