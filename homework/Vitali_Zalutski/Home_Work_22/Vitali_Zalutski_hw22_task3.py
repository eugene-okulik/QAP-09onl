from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_sub_sub_item_2(chrome_driver):
    chrome_driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    button_show_promt_click = chrome_driver.find_element(By.ID, 'promptexample')
    button_show_promt_click.click()
    Alert(chrome_driver).send_keys("Hello, Im user")
    Alert(chrome_driver).accept()
    sleep(2)
    alert_text = chrome_driver.find_element(By.ID, 'promptreturn')
    assert "Hello, Im user" in alert_text.text, "Invalid message"
