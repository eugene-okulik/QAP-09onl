from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver_chrome = webdriver.Chrome(options=options)
    driver_chrome.implicitly_wait(10)
    return driver_chrome


def test_contact_us(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php')

    contact_us_button = driver_chrome.find_element(By.ID, 'contact-link')
    contact_us_button.click()

    select = Select(driver_chrome.find_element(By.ID, 'id_contact'))
    select.select_by_value('2')

    email_addres = driver_chrome.find_element(By.ID, 'email')
    email_addres.send_keys('medope5875@haboty.com')

    order_reference = driver_chrome.find_element(By.ID, 'id_order')
    order_reference.send_keys('37515E')

    message = driver_chrome.find_element(By.ID, 'message')
    message.send_keys('Hello world')

    send_batton = driver_chrome.find_element(By.ID, 'submitMessage')
    send_batton.click()

    report_your_message = driver_chrome.find_element(By.XPATH, '//*[@id="center_column"]/p')
    #report_your_message_text = report_your_message.find_element(By.TAG_NAME, 'p').text
    print(report_your_message.text)


driver_chrome = driver()
test_contact_us(driver_chrome)
driver_chrome.quit()