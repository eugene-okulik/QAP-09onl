from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from time import sleep


service = Service(executable_path='C:\\Users\\chromedriver_win32\\chromedriver.exe')
crome_driver = webdriver.Chrome(service=service)

crome_driver.get('http://automationpractice.com/')
contact_us = crome_driver.find_element(By.ID, 'contact-link')
contact_us.click()

email_address = crome_driver.find_element(By.ID, 'email')
email_address.send_keys('btalataj@gmail.com')
email_address.send_keys(Keys.ENTER)

order_reference = crome_driver.find_element(By.ID, 'id_order')
order_reference.send_keys('http://automationpractice.com/index.php?id_product=6&controller=product')

send = crome_driver.find_element(By.ID, 'submitMessage')
send.click()
