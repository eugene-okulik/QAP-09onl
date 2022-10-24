from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def open_chrome():
    service = Service(executable_path='C:\\Windows\\chromedriver')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options, service=service)
    return driver


def check_alert(driver):
    driver.get('http://automationpractice.com/index.php')
    # sleep(5)
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    send_button = driver.find_element(By.NAME, 'submitMessage')
    send_button.click()
    alert_block = driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_block_text = alert_block.text
    alert_block_color = alert_block.value_of_css_property('background-color')
    assert alert_block_color == '#f3515c', 'Invalid color of alert block'
    # print(alert_block_text)
    assert 'Invalid name' in alert_block_text, 'Invalid message in alert block'
    sleep(3)


def check_alert_header(driver):
    driver.get('http://automationpractice.com/index.php')
    # contacts_us_link = driver.find_element(By.LINK_TEXT, 'Contact us')
    # contacts_us_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
    contacts_us_links = driver.find_elements(By.LINK_TEXT, 'Contact us')
    print(contacts_us_links)
    contacts_us_links[1].click()
    # contacts_us_link.click()
    email_fild = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail]')
    email_fild.send_keys('some text')
    email_fild.send_keys(Keys.ENTER)
    alert_block = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    alert_header_text = alert_block.find_element(By.TAG_NAME, 'p').text


def get_cookies(driver):
    driver.get('https://demoblaze.com/')
    print(driver.get_cookies())
    driver.add_cookie({'name': 'test1', 'value': 'test-value'})
    print(driver.get_cookies())


def tabs(driver):
    driver.get()


driver = open_chrome()
tabs(driver)
driver.quit()