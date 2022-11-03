from selenium.webdriver.common.by import By

username_field = (By.ID, 'loginusername')
password_field = (By.ID, 'loginpassword')
log_in_button = (By.CSS_SELECTOR, 'button[onclick="logIn()"]')
welcome_field = (By.ID, 'nameofuser')