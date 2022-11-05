from selenium.webdriver.common.by import By

about_us = (By.CSS_SELECTOR, '[title="About us"]')
dresses_button = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
best_sellers_link = (By.CSS_SELECTOR, '#block_various_links_footer > ul > li:nth-child(3) > a')
best_sellers_menu_link = (By.XPATH, '//*[@id="best-sellers_block_right"]/h4/a')
stores_link = (By.XPATH, '//*[@id="block_various_links_footer"]/ul/li[4]/a')
phone_number = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/span/strong')