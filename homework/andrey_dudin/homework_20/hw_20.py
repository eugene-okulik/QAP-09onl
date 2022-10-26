from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''
Напишите программу, которая зайдет на сайт http://automationpractice.com/, кликнет по ссылке Contact us, 
полностью заполнит форму (кроме аплода файла) и нажмет Send.
'''

def open_chrome_session():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def fill_form_and_send_a_message(driver):
    # open a Website
    driver.get('http://automationpractice.com')
    driver.find_element(By.ID, 'contact-link').click()    # find and click the button 'Contact us' on the page
    driver.find_element(By.XPATH, "//option[contains(text(),'Webmaster')]").click() #select Webmaster
    driver.find_element(By.ID, 'email').send_keys("test@mail.ru") #filled email field
    driver.find_element(By.ID, 'id_order').send_keys("order field value")  # filled order field
    driver.find_element(By.ID, 'message').send_keys("message field value")  # filled message field
    driver.find_element(By.ID, 'submitMessage').click() #send values


driver = open_chrome_session()
fill_form_and_send_a_message(driver)
driver.quit()