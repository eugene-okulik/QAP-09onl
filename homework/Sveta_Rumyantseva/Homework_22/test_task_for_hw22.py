from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_order_item(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item_link = driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=2" and @class="hrefch"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(item_link).key_up(Keys.CONTROL).perform()  # open link in new tab
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(item_link),
                                    message=f"Element is clickable by locator {item_link}")
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])  # switch to the new tab with an item
    add_button = driver.find_element(By.XPATH, '//a[@onclick="addToCart(2)" and @href="#"]')
    add_button.click()  # bad version for only click(): ActionChains(driver).click(add_button).perform()

    WebDriverWait(driver, 10).until(EC.alert_is_present(), message=f"Alert is not present")
    Alert(driver).accept()
    driver.close()  # close the current tab: all_tabs[1]

    driver.switch_to.window(all_tabs[0])  # switch to the previous tab: all_tabs[0]
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
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
    show_prompt_box_button.click()

    alert_message = 'Test message'
    Alert(driver).send_keys('Test message')
    Alert(driver).accept()

    result_message = driver.find_element(By.ID, 'promptreturn').text
    assert alert_message == result_message
