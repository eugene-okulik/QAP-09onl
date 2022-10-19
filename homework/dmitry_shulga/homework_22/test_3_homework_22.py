from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_sub_sub_item_2(chrome_driver):
    chrome_driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    show_prompt_box = chrome_driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()
    Alert(chrome_driver).send_keys("Hello world")
    Alert(chrome_driver).accept()
    sleep(2)
    hello_text = chrome_driver.find_element(By.ID, 'promptreturn')
    assert "Hello world" in hello_text.text, "Invalid message"


