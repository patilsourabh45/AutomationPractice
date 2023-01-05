import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'Click Here').click()

print("Current window handle : ", driver.current_window_handle)
print("window handles : ", driver.window_handles)

#
# Current window handle :  CDwindow-544CB4B2164590DD050A1E106E77BE6B
# window handles :  ['CDwindow-544CB4B2164590DD050A1E106E77BE6B', 'CDwindow-814CD0E44DB1AF7A9A5403612E532783']

driver.switch_to.window(driver.window_handles[-1])  ### If you want to switch to lastly opened window
###driver.switch_to.window(driver.window_handles[0]) If you want to switch to main window
###driver.switch_to.window('main') If you want to switch to main window

text = driver.find_element(By.CSS_SELECTOR, 'body > div > h3').get_attribute("innerHTML")
print(text)
print("Current window handle : ", driver.current_window_handle)
driver.refresh()

###----------------------------------------------------------
##Assignment IMP

## Facebook
## Gmail
## Amazon
##Flipkart
##credence.com

## handles.find
userinput = "Facebook.com"      ##v input function
all_handles = driver.window_handles
for handle in all_handles:
    driver.switch_to.window(handle)
    print(driver.title)
    print(driver.current_url)

    if(driver.title == userinput):
        break
## write logic to operate on facebook.com


## make entry to dictionary, key = titile/url , value = handle