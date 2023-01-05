import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")  ## open website or url
time.sleep(2)
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "/html/body/button").click()
time.sleep(5)

driver.switch_to.alert.accept()

driver.switch_to.frame("iframeResult")