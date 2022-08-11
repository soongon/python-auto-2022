import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
time.sleep(2)
driver.get('http://www.naver.com')
time.sleep(2)
the_tag = driver.find_element(By.CSS_SELECTOR, '#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a')
the_tag.click()
time.sleep(5)
driver.close()
