from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_chrome_browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    chrome_driver.get('http://automationpractice.com/')
    return chrome_driver


def check_contact_us_link(chrome_driver):
    chrome_driver.get('http://automationpractice.com/index.php')
    contact_us = chrome_driver.find_element(By.ID, 'contact-link')
    contact_us.click()


def check_all_form_fields(chrome_driver):
    chrome_driver.get('http://automationpractice.com/index.php?controller=contact')
    select_field = Select(chrome_driver.find_element(By.CSS_SELECTOR, 'select[class="form-control"]'))
    select_field.select_by_visible_text('Customer service')   # choose any option and fill select field

    email_field = chrome_driver.find_element(By.ID, 'email')
    email_field.send_keys('sottopassagero@rambler.ru')  # fill email field

    order_field = chrome_driver.find_element(By.CSS_SELECTOR, 'input[name="id_order"]')
    order_field.send_keys('order3568A')   # fill order field

    message_field = chrome_driver.find_element(By.CSS_SELECTOR, 'textarea[id="message"]')
    message_field.send_keys('Please, help me to solve my problem.')  # fill message field

    # attach file
    attach_file_field = chrome_driver.find_element(By.XPATH, '//input[@name="fileUpload"]')
    attach_file_field.send_keys(r"E:\TeachMeSkills\QAP09-onl_cotinuation_clone\QAP-09onl\homework"
                                r"\Sveta_Rumyantseva\Homework_20\text_file.txt")

    send_button = chrome_driver.find_element(By.CSS_SELECTOR, 'button[name="submitMessage"]')
    send_button.click()
    # result of the send button click = message "Your message has been successfully sent to our team."
    print(chrome_driver.find_element(By.CSS_SELECTOR, 'p[class="alert alert-success"]').text)


chr_driver = open_chrome_browser()
check_contact_us_link(chr_driver)
check_all_form_fields(chr_driver)
chr_driver.quit()
