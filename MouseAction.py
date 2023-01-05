import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

hoverEle = driver.find_element(By.ID, 'myDropdown')      ##is not clickable
dropdownOption2 = driver.find_element(By.ID, 'dropOption2') #### element not interactable # we can not directly reach to element before reaching to parent

actionObj = ActionChains(driver)
actionObj.move_to_element(hoverEle).move_to_element(dropdownOption2).click().perform()

####-------------------------------------------------------------------------
## Double click

btn = driver.find_element(By.ID, 'myButton')
actionObj.double_click(btn).perform()

###====================================================================

actionObj.context_click().perform() # option 1, without element right click. will click where your mouse poiter present

actionObj.context_click(btn).perform() # option 2, right click on given element

##====================================================================
### Drag an drop

driver.find_element(By.ID, 'checkBox1').click()
dropSource = driver.find_element(By.XPATH, '//*[@id="logo"]')
dropDestination = driver.find_element(By.ID, "drop2")
time.sleep(3)
actionObj.drag_and_drop(dropSource, dropDestination).perform()
