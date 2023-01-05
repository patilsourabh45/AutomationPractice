import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")


driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

# time.sleep(10)
locatorLoding = (By.XPATH, '//*[@id="loading"]')
eleLoding = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locatorLoding))
print("Text : ", eleLoding.text)
# text = driver.find_element(By.XPATH, '//*[@id="loading"]').text
# print("Text : ", text)

locatorH4 = (By.XPATH, '//*[@id="finish"]/h4')
eleLoding = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locatorH4))
text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text
print("Text : ", text)
expected_conditions.alert_is_present
### DOM => Document object model
## Visibility =>  element is avaible in HTML and visible on web page
## presence =>  element is available on HTML page ## may be or may not be visible on web page