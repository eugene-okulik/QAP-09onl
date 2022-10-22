from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


service = Service(executable_path='C:\\chromedriver.exe')


def open_chrome():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(15)
    return driver


def use_site(driver):
    driver.get('http://automationpractice.com/index.php')
    use_contact_us = driver.find_element(By.ID, 'contact-link')
    use_contact_us.click()

    subject = Select(driver.find_element(By.ID, 'id_contact'))
    subject.select_by_visible_text('Webmaster')

    email_address = driver.find_element(By.ID, 'email')
    email_address.send_keys('V.Zalutski@mail.ru')
    email_address.send_keys(Keys.ENTER)

    order = driver.find_element(By.ID, 'id_order')
    order.send_keys('http://automationpractice.com/index.php?id_product=1&controller=product')

    message = driver.find_element(By.ID, 'message')
    message.send_keys("I want to buy this")

    send = driver.find_element(By.ID, 'submitMessage')
    send.click()


driver = open_chrome()
use_site(driver)
driver.quit()