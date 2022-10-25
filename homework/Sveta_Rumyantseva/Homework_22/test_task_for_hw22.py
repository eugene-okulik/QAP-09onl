from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_order_item(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item_link = driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=2" and @class="hrefch"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(item_link).key_up(Keys.CONTROL).perform()  # open link in new tab
    sleep(2)  # demonstration

    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])  # switch to the new tab with an item
    add_button = driver.find_element(By.XPATH, '//a[@onclick="addToCart(2)" and @href="#"]')
    sleep(2)  # demonstration
    ActionChains(driver).click(add_button).perform()  # or  add_button.click()
    sleep(2)  # demonstration
    Alert(driver).accept()
    driver.close()  # close the current tab: all_tabs[1]

    driver.switch_to.window(all_tabs[0])  # switch to the previous tab: all_tabs[0]
    cart = driver.find_element(By.ID, 'cartur')
    sleep(2)  # demonstration
    cart.click()
    sleep(2)  # demonstration
    item_text = driver.find_element(By.CLASS_NAME, 'success').text

    assert "Nokia lumia 1520" in item_text


def test_check_menu(driver):
    driver.get('https://demoqa.com/menu#')
    menu_list = driver.find_elements(By.CSS_SELECTOR, 'a[href="#"]')
    ActionChains(driver).move_to_element(menu_list[1]).move_to_element(menu_list[4]).\
        move_to_element(menu_list[6]).click().perform()

    assert menu_list[6].text == 'Sub Sub Item 2'


def test_check_alert(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    show_prompt_box_button = driver.find_element(By.ID, 'promptexample')
    sleep(3)  # demonstration
    show_prompt_box_button.click()

    alert_message = 'Test message'
    Alert(driver).send_keys('Test message')
    sleep(1)  # demonstration
    Alert(driver).accept()

    result_message = driver.find_element(By.ID, 'promptreturn').text
    sleep(2)  # demonstration
    assert alert_message == result_message
