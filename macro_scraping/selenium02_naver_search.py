import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.naver.com/')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#query').send_keys('강남역 침수', Keys.ENTER)
time.sleep(5)

driver.close()