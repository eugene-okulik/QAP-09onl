from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


# servicelkshfksjdhf = Service(executable_path='C:\\my_user\\chromedriver.exe')
options = Options()
# options.add_argument('start-maximized')
options.add_argument('window-size=2048,1080')
chrome_driver = webdriver.Chrome(options=options)
# chrome_driver.maximize_window()
chrome_driver.get('https://www.onliner.by/')
print(chrome_driver.current_url)
print(chrome_driver.title)
chrome_driver.quit()
