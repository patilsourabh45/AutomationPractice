
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actionObj = ActionChains(driver)

dropSource = driver.find_element(By.XPATH, '//*[@id="box3"]')
dropDestination = driver.find_element(By.ID, "box103")
time.sleep(3)
actionObj.drag_and_drop(dropSource, dropDestination).perform()
