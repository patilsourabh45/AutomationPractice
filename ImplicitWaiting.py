import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.implicitly_wait(10)       ## it came with selenium  ## it will wait maximum till given sec. and minimum till webcontrol is available to find
## write it once and it wil be applicable to all web element
driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

# time.sleep(10)
text = driver.find_element(By.XPATH, '//*[@id="loading"]').text
print("Text : ", text)


##time.sleep(10)           ## python code.. it will pause execution of script minimum till given sec
## for each web element you need to provide time.sleep for wait
text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text

print("Text : ", text)