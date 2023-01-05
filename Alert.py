import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")  ## open website or url
driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button").click()

driver.switch_to.alert.dismiss()
