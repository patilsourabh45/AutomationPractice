import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[@id='start']/button").click()
# time.sleep(10)

loading = driver.find_element(By.ID, "loading").get_attribute("innerHTML")
print("Loading text is: ", loading)

helloText = driver.find_element(By.XPATH, "//*[@id='finish']/h4").get_attribute("innerHTML")
print("Hello Text is :", helloText)

driver.find_element(By.XPATH, "//*[@id='start']/button").click()
locatorLoading = (By.XPATH, "//*[@id='loading']")

eleLoading  = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locatorLoading))

print("Loading :", eleLoading.text)

helloLocator = (By.XPATH, "//*[@id='finish']/h4")
helloText = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(helloLocator))

print("Hello Text is: ", helloText.text)



