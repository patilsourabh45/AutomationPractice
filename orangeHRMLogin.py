import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(10)
inputEMail = driver.find_element(By.NAME, "username")
inputEMail.send_keys("Admin")

inputPass = driver.find_element(By.NAME, "password")
inputPass.send_keys("admin123")

loginBtn = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
loginBtn.click()