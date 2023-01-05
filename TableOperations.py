import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")


print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').text)     ## company
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').get_attribute('innerHTML'))
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[2]').text)     ## Contact
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[1]').text)     ## Alfreds Futterkiste

## when path start form root and go upto element called as absolute path
## when path start from element itself or not from root called as relative path

## html website root => html
## computer folders root => drive name e.g. c, d, etc.


### print how many rows are in table
#print(len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')))     ##
print(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr').__len__())     ##


### print how many columns are in table
# print(len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th')))     ##

thElements = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th')
print(thElements.__len__())     ##


### assignment : print all table values by using loop
# Company	Contact	Country
# Alfreds Futterkiste	Maria Anders	Germany
# Centro comercial Moctezuma	Francisco Chang	Mexico
# Ernst Handel	Roland Mendel	Austria
# Island Trading	Helen Bennett	UK
# Laughing Bacchus Winecellars	Yoshi Tannamuri	Canada
# Magazzini Alimentari Riuniti	Giovanni Rovelli	Italy
