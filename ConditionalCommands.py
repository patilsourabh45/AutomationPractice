
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")  ## open website or url

inputElement = driver.find_element(By.ID, "dropOption1")  #in hover dropdown there is a option with id dropOption1
print("Is drop option displayed :", inputElement.is_displayed())
print("Is drop option displayed :", driver.find_element(By.ID, "myTextInput2").is_displayed())

####-----------------------------------------------------------------------

inputElement = driver.find_element(By.ID, "radioButton1")
print("Is radio button displayed :", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "radioButton2")
print("Is radio button displayed :", inputElement.is_selected())


##-------------------------------------------------------------------


inputElement = driver.find_element(By.ID, "myTextInput2")
print("Is enabled :", inputElement.is_enabled())

### Check if control is readonly
inputElement = driver.find_element(By.ID, "myTextInput2")
print("Is enabled :", inputElement.get_attribute('readonly'))


# driver.find_element_by_id("myTextInput2")
# driver.find_element_by_name("myTextInput2")
# driver.find_element_by_xpath("myTextInput2")
# driver.find_element_by_css_selector("myTextInput2")
# driver.find_element_by_link_text("myTextInput2")
#
#
#
# driver.find_element("named", "myTextInput2")
