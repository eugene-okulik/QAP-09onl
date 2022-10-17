from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def open_chrome():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def filling_form(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    select = Select(driver.find_element(By.ID, 'id_contact'))
    select.select_by_value('1')
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email_field.send_keys('aniskevich@mail.ru')
    order_reference = driver.find_element(By.ID, 'id_order')
    order_reference.send_keys('12345678')
    message_field = driver.find_element(By.NAME, 'message')
    message_field.send_keys('no matter what text')
    attach_file = driver.find_element(By.ID, 'fileUpload')
    attach_file.send_keys('C:\\Users\\PK\\PycharmProjects\\new\\QAP-09onl\\homework\\Valery_Aniskevich\\hw_20\\some_file.txt')
    send_button = driver.find_element(By.NAME, 'submitMessage')
    send_button.click()
    final_message_text = driver.find_element(By.CLASS_NAME, 'alert-success').text
    print(final_message_text)


driver = open_chrome()
filling_form(driver)
driver.quit()