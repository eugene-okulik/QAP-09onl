from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


def open_chrome():
    service = Service(executable_path='C:\\TMS\\chromedriver.exe')
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    return chrome_driver


def tools_qa(chrome_driver):
    chrome_driver.get('https://demoqa.com/menu#')
    my_item_2 = chrome_driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]')
    sub_sub_list = chrome_driver.find_element(By.XPATH, '//a[text() = "SUB SUB LIST »"]')
    sub_sub_item_2 = chrome_driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    ActionChains(chrome_driver).move_to_element(my_item_2).move_to_element(sub_sub_list).move_to_element(
        sub_sub_item_2).perform()
    sleep(1)
    assert "Sub Sub Item 2" in sub_sub_item_2.text
    print(f"QA software use: {sub_sub_item_2.text}.")


chrome_driver = open_chrome()
tools_qa(chrome_driver)
chrome_driver.quit()
