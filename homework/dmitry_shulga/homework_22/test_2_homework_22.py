from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By


def test_sub_sub_item_2(chrome_driver):
    chrome_driver.get("https://demoqa.com/menu#")
    main_item_2 = chrome_driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]')
    sub_sub_list = chrome_driver.find_element(By.XPATH, '//a[text() = "SUB SUB LIST »"]')
    sub_sub_item_2 = chrome_driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    ActionChains(chrome_driver).move_to_element(main_item_2).move_to_element(sub_sub_list).move_to_element(sub_sub_item_2).perform()
    sleep(3)
    assert "Sub Sub Item 2" in sub_sub_item_2.text, "Invalid message"
    print(sub_sub_item_2.text)
    chrome_driver.quit()
