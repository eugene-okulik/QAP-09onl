from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


def open_chrome():
    options = Options()
    # options.add_argument('start-maximized')
    # options.add_argument('window-size=2048,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    # sleep(3)
    return driver


def check_alert(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    send_button = driver.find_element(By.NAME, 'submitMessage')
    send_button.click()
    alert_block = driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_block_text = alert_block.text
    # alert_block_text = alert_block.get_attribute('innerText')
    alert_block_color = alert_block.value_of_css_property('background-color')
    assert alert_block_color == '#f3515c', 'Invalid color of alert block'
    assert 'Invalid name' in alert_block_text, 'Invalid message in alert block'
    sleep(3)


def check_alert_header(driver):
    driver.get('http://automationpractice.com/index.php')
    contact_us_links = driver.find_elements(By.LINK_TEXT, 'Contact us')
    print(contact_us_links)
    contact_us_links[1].click()
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email_field.send_keys('some text')
    sleep(2)
    email_field.clear()
    sleep(2)
    email_field.send_keys('kjsdgfdfd')
    # email_field.send_keys(Keys.ENTER)
    email_field.submit()
    alert_block = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    # '//*[@id="center_column"]/div'
    # '//*[@id="uniform-fileUpload"]/span[1]'
    # '/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/p[5]/div/span[1]'
    alert_header_text = alert_block.find_element(By.TAG_NAME, 'p').text
    assert alert_header_text == 'There is 1 error', 'Some error message'


def checks(driver):
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category#/')
    checkbox = driver.find_element(By.ID, 'layered_category_4')
    print(checkbox.is_selected())
    checkbox.click()
    print(checkbox.is_selected())
    add_to_compare = driver.find_element(By.CLASS_NAME, 'add_to_compare')
    green_button = driver.find_element(By.CLASS_NAME, 'bt_compare')
    print(green_button.is_enabled())
    add_to_compare.click()
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable(green_button), message='green button not found')
    print(green_button.is_enabled())


def check_select(driver):
    driver.get('http://automationpractice.com/index.php?controller=contact')
    select = Select(driver.find_element(By.ID, 'id_contact'))
    sleep(3)
    select.select_by_value('2')
    sleep(3)
    select.select_by_visible_text('Webmaster')
    sleep(3)


def get_cookies(driver):
    driver.get('https://demoblaze.com/')
    print(driver.get_cookies())
    driver.add_cookie({'name': 'test1', 'value': 'test_value', 'httpOnly': True})
    print(driver.get_cookies())


def tabs(driver):
    sleep(5)
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    print('old tab: ', driver.find_element(By.TAG_NAME, 'h3').text)
    driver.switch_to.window(driver.window_handles[1])
    print('new tab: ', driver.find_element(By.TAG_NAME, 'h3').text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print('old tab2: ', driver.find_element(By.TAG_NAME, 'h3').text)



driver = open_chrome()
tabs(driver)
driver.quit()
