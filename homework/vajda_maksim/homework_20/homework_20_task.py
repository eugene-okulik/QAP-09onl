# Задание
# Напишите программу, которая зайдет на сайт http://automationpractice.com/,
# кликнет по ссылке Contact us, полностью заполнит форму (кроме аплода файла) и нажмет Send.
#
# Для самых любопытных (выполнять необязательно)
# 1. Заполните также поле загрузки файла, т.е. приаттачьте файл.
# 2. После отправки вам будет отображено, что все оправлено успешно.
#    Получите со страницы тот текст, который будет находиться в зеленом прямоугольнике и распечатайте его.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_chrome():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def fill_the_form(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_button = driver.find_elements(By.LINK_TEXT, 'Contact us')
    contact_us_button[0].click()
    subject_heading = Select(driver.find_element(By.ID, 'id_contact'))
    subject_heading.select_by_visible_text('Customer service')
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email_field.send_keys('maksim@gmail.com')
    order_field = driver.find_element(By.ID, 'id_order')
    order_field.send_keys('11102022')
    attach_file = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_path = 'C:\TMS.png'  # файл TMS.png прикреплю в Commit
    attach_file.send_keys(file_path)
    message_field = driver.find_element(By.ID, 'message')
    message_field.send_keys('Belarus')
    send_button = driver.find_element(By.NAME, 'submitMessage')
    send_button.click()
    successfully_block = driver.find_element(By.CLASS_NAME, 'alert-success')
    successfully_block_text = successfully_block.text
    print(f'Текст из зеленого прямоугольника: <{successfully_block_text}>')


driver = open_chrome()
fill_the_form(driver)
driver.quit()
