from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
print(driver.title)

# dropOption = driver.find_element(By.ID, "dropOption1")
# print("IsDisplayed", dropOption.is_displayed())  #False
#
# dropOption = driver.find_element(By.XPATH, "//*[@id='mySelect']/option[1]")
# print("IsDisplayed", dropOption.is_displayed())  #True
#
# checkbox = driver.find_element(By.ID, "radioButton1")
# print("is selected", checkbox.is_selected()) #True
#
# checkbox = driver.find_element(By.ID, "radioButton2")
# print("is selected", checkbox.is_selected()) #False
#
# checkbox = driver.find_element(By.ID, "mySelect")
# print("is selected", checkbox.is_selected()) #False

dropdown = driver.find_element(By.ID, "mySelect")
objDropdown = Select(dropdown)

time.sleep(3)
# objDropdown.select_by_index(0)
# objDropdown.select_by_value("50%")
# objDropdown.select_by_visible_text("Set to 100%")

# all_options = objDropdown.options
# print("length",len(all_options))
#
# print("ALLOPTIONS",all_options)
#
# for options in all_options:
#     print("Value :", options.text, ", Text : ", options.get_attribute("value"))
#
# links = driver.find_elements(By.TAG_NAME, "a")
# print("Total links", len(links))
#
# for link in links:
#     # print("Link Text : ", link.text)
#     print("Link Text : ", link.get_attribute("innerHTML"))
