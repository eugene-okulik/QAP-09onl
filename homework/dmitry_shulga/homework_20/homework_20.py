from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def check_alert(chrome_driver):
    chrome_driver.get("http://automationpractice.com/index.php")
    contact_us_button = chrome_driver.find_element(By.ID, "contact-link")
    contact_us_button.click()
    subject_heading = Select(chrome_driver.find_element(By.ID, "id_contact"))
    subject_heading.select_by_value("2")
    email_field = chrome_driver.find_element(By.ID, "email")
    email_field.send_keys("Some_email@mail.com")
    order_field = chrome_driver.find_element(By.ID, "id_order")
    order_field.send_keys("Some order")
    message_field = chrome_driver.find_element(By.ID, "message")
    message_field.send_keys("Some_message")
    input_field = chrome_driver.find_element(By.ID, "fileUpload")
    input_field.send_keys("D:/pythonProject/QAP09-onl/QAP-09onl/homework/dmitry_shulga/homework_20/picture.jpg")
    send_button = chrome_driver.find_element(By.ID, "submitMessage")
    send_button.click()
    alert_success = chrome_driver.find_element(By.CLASS_NAME, "alert-success")
    assert "Your message has been successfully sent to our team." in alert_success.text, "Invaled message"
    print(alert_success.text)
    sleep(3)


chrome_driver = open_chrome()
check_alert(chrome_driver)
chrome_driver.quit()
