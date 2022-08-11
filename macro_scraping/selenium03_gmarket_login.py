import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.gmarket.co.kr/')
time.sleep(2)
driver\
    .find_element(By.CSS_SELECTOR, '#desktop_layout-header > div > div > div.box__navigation > div.box__usermenu > ul > li:nth-child(1) > a')\
    .click()
time.sleep(2)
driver\
    .find_element(By.CSS_SELECTOR, '#id')\
    .send_keys('kssk30', Keys.TAB, '1q2w3e4r##')
time.sleep(1)
driver\
    .find_element(By.CSS_SELECTOR, '#mem_login > div.login-input > div.btn-login > button')\
    .click()
time.sleep(2)
driver.get('https://cart.gmarket.co.kr/ko/pc/cart/#/')
time.sleep(2)
html = driver.page_source
print(html)
driver.close()
