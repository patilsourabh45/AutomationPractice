

import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

alert = webdriver.Chrome()
alert.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# time.sleep(2)
# clickforJS = alert.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button").click()
# time.sleep(3)
# alert.switch_to.alert.accept()   #click ok button
# print("Result : ",alert.find_element(By.ID,"result").text)
#
# time.sleep(2)
#
# clickforJScf = alert.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(2) > button").click()
# time.sleep(2)
# alert.switch_to.alert.accept()      #click ok button
# # alert.switch_to.alert.dismiss()     #click cancle button
# print("Result = ",alert.find_element(By.ID,"result").text)
#
# time.sleep(2)
alert.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button").click()

name_prompt = Alert(alert)
name_prompt.send_keys("Willian Shakesphere")
time.sleep(5)
name_prompt.accept()
#
# clickforJSpromt = alert.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button").click()
# time.sleep(2)
# alert.switch_to.alert.send_keys("Yes I am a JS prompt...thank You..! ")
# time.sleep(5)
# alert.switch_to.alert.accept()
print("Result = ",alert.find_element(By.ID,"result").text)
time.sleep(2)

alert.refresh()
alert.close()

