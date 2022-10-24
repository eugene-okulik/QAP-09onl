from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Task. Напишите программу, которая зайдет на сайт http://automationpractice.com/, кликнет по ссылке Contact us,
# полностью заполнит форму (кроме аплода файла) и нажмет Send.
#
# Для самых любопытных (выполнять необязательно)
# Заполните также поле загрузки файла, т.е. приаттачьте файл.
# После отправки вам будет отображено, что все оправлено успешно. Получите со страницы тот текст, который будет
# находиться в зеленом прямоугольнике и распечатайте его.


def open_chrome_session():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def fill_in_form_send_a_message(driver):
    # open a Website
    driver.get('http://automationpractice.com')
    contact_us_button = driver.find_element(By.ID, 'contact-link')    # find the button 'Contact us' on the page
    contact_us_button.click()    # push the button

    # fill in a field 'subject heading'
    select = Select(driver.find_element(By.ID, 'id_contact'))
    select.select_by_value('1')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'id_contact'), 'Webmaster'))
    select_text_prompt = driver.find_element(By.ID, 'desc_contact1')
    print("select text prompt is displayed:", select_text_prompt.is_displayed())
    assert select_text_prompt.is_displayed(), 'the text prompt did not appear'
    print("select text prompt:", select_text_prompt.text)

    # fill in the field 'Email address'
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email_field.send_keys('qatester09@mail.ru')

    # fill in the field 'Order reference'
    order_reference_field = driver.find_element(By.ID, 'id_order')
    order_reference_field.send_keys('Printed Dress')

    # fill in field message
    fill_in_field_message = driver.find_element(By.XPATH, '//textarea[@id="message" and @name="message"]')
    fill_in_field_message.send_keys('Homework_20_was_done_by_Mary_Bilaya')

    # fill in an invisible field 'fileUpload'
    attach_file = driver.find_element(By.NAME, 'fileUpload')    # find an invisible field 'fileUpload'
    wait = WebDriverWait(driver, 20)
    wait.until(EC.invisibility_of_element_located(attach_file))
    attach_file.send_keys('C:\\Users\\Masha\\PycharmProjects\\QAP-09onl\\homework\\mary_bilaya\\homework_20\\attach_file.txt')

    # find the button 'Send' on the page
    send_button = driver.find_element(By.NAME, 'submitMessage')
    send_button.click()    # push the button

    # result of all work
    message_block = driver.find_element(By.CLASS_NAME, 'alert-success')
    message_block.is_displayed()
    print(message_block.text)


driver = open_chrome_session()    # create a driver
fill_in_form_send_a_message(driver)    # run a test
driver.quit()    # quit a driver