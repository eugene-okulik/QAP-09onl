from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def check_send(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys("helloworld@gmail.com")
    order_field = driver.find_element(By.CSS_SELECTOR, "#id_order")
    order_field.send_keys("some_order")
    message_field = driver.find_element(By.CSS_SELECTOR, "#message")
    message_field.send_keys("some_message")
    check_box = Select(driver.find_element(By.CSS_SELECTOR, "#id_contact"))
    check_box.select_by_value("2")
    # file_upload = driver.find_element(By.CSS_SELECTOR, "#fileUpload")
    # filepath = "C:/Users/Home/Pictures/mv.jpg"
    # file_upload.send_keys(filepath)

    submit_button = driver.find_element(By.ID, 'submitMessage')
    submit_button.click()
    succsess_message = driver.find_element(By.CSS_SELECTOR, '[class="alert alert-success"]').text
    print(succsess_message)
    sleep(3)


driver = open_chrome()
check_send(driver)
driver.quit()
