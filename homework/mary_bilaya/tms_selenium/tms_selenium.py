from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from time import sleep

# options = Options()
# options.add_argument('start-maximized')
# chrome_driver = webdriver.Chrome(options=options)
# service = Service(executable_path='C:\\Windows\\chromedriver')
chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
# sleep(5)
chrome_driver.get('https://www.onliner.by/')
# sleep(3)
print(chrome_driver.current_url)
print(chrome_driver.title)
chrome_driver.quit()


