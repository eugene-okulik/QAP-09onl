from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


def open_chrome():
    service = Service(executable_path='C:\\TMS\\chromedriver.exe')
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    return chrome_driver

def choose_contact_us(chrome_driver):
    chrome_driver.get('http://automationpractice.com/')
    contact_us_button = chrome_driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    write_email = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    write_email.send_keys('my@mail.ru')
    write_order_reference = chrome_driver.find_element(By.ID, 'id_order')
    write_order_reference.send_keys('qwerty')
    write_texts = chrome_driver.find_element(By.ID, 'message')
    write_texts.send_keys('TEXT')
    send_button = chrome_driver.find_element(By.ID, 'submitMessage')
    send_button.click()
    sleep(5)
'''
def write_text(chrome_driver):
    write_email = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    write_email.send_keys('my@mail.ru')
    write_order_reference = chrome_driver.find_element(By.ID, 'id_order')
    write_order_reference.send_keys('qwerty')
    write_texts = chrome_driver.find_element(By.ID, 'message')
    write_texts.send_keys('TEXT')
'''

chrome_driver = open_chrome()
choose_contact_us(chrome_driver)
chrome_driver.quit()

# sleep(3)
# chrome_driver.quit()