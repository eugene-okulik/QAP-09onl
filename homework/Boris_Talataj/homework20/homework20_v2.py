from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from time import sleep

options = Options()
options.add_argument("start-maximized")
chrome_driver = webdriver.Chrome(options=options)

chrome_driver.get('http://automationpractice.com/')
contact_us = chrome_driver.find_element(By.ID, 'contact-link')
contact_us.click()

email_address = chrome_driver.find_element(By.ID, 'email')
email_address.send_keys('btalataj@gmail.com')

subject_heading = chrome_driver.find_element(By.XPATH, "//option[contains(text(),'Webmaster')]")
subject_heading.click()

message = chrome_driver.find_element(By.ID, 'message')
message.send_keys('Платье просто песня. Беру.')

order_reference = chrome_driver.find_element(By.ID, 'id_order')
order_reference.send_keys('http://automationpractice.com/index.php?id_product=6&controller=product')

send = chrome_driver.find_element(By.ID, 'submitMessage')
send.click()

