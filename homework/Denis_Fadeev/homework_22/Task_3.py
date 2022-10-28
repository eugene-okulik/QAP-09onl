from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep


def open_chrome():
    service = Service(executable_path='C:\\TMS\\chromedriver.exe')
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    return chrome_driver


def tools_qa(chrome_driver):
    chrome_driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    show_prompt_box = chrome_driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()
    Alert(chrome_driver).send_keys('Text completed')
    Alert(chrome_driver).accept()
    text = chrome_driver.find_element(By.ID, 'promptreturn')
    assert "Text completed" in text.text
    print(f"QA software write: {text.text}.")
    sleep(5)


chrome_driver = open_chrome()
tools_qa(chrome_driver)
chrome_driver.quit()
