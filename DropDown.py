import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")  ## open website or url
#
# time.sleep(3)
#
# ### Manual way to click option.. Jisko hum use nahi karnewale
#
# dropdownOption = driver.find_element(By.XPATH, '//*[@id="mySelect"]/option[3]')
# dropdownOption.click()
#
# #####---------------------------------------------------------------------
# time.sleep(3)
elementDrop = driver.find_element(By.ID, 'mySelect')
objDropdown = Select(elementDrop)
# objDropdown.select_by_visible_text("Set to 25%")
#
# time.sleep(3)
# objDropdown.select_by_value("100%")
#
# time.sleep(3)
# objDropdown.select_by_index(1)      ### it will select 1st index from dropdown

print(objDropdown.options)
print("NUmber of options are : ", len(objDropdown.options))

### --Task to print all options visible text and value along with index

##innerHTML

## I want to print all links visible text and href avaialable on we page

dropDrown = driver.find_element(By.ID, 'mySelect')
print(dropDrown.get_attribute('innerHTML'))
objDrop = Select(dropDrown)
for i in range(len(objDrop.options)):
    #objDrop.select_by_index(i)
    print(f'Text is: {objDrop.options[i].text} Value is: {objDrop.options[i].get_attribute("value")}  Index is:{i} \n')
    time.sleep(1)

for option in objDrop.options:
    print(f'Text is: {option.text} Value is: {option.get_attribute("value")} \n')
    time.sleep(1)
links = driver.find_elements(By.CLASS_NAME, "linkClass")
for i in links:
    print(f" link is: {i.get_attribute('href') } Text is: {i.text}")