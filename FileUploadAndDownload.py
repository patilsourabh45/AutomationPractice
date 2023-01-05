import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)

driver.find_element(By.ID, 'file-upload').send_keys("c:\\Screenshot.png")

driver.find_element(By.ID, 'file-submit').click()


##https://the-internet.herokuapp.com/download
## write program to download.. uploaded file
