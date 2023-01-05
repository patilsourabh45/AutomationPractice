import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

# print(driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th[1]").text)
# print(driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th[2]").text)
# print(driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[2]/td[1]").text)
# print(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr').__len__())

trElements = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr').__len__()
tdElements = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th').__len__()

# for i in range(2, trElements+1):
#     ele = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th["+str(i)+"]").text
#     print(ele, end="       ")


for i in range(2, trElements+1):
    for j in range(1, tdElements + 1):
        ele = driver.find_element(By.XPATH, "/ html / body / div[7] / div[1] / div[1] / div[3] / div / table / tbody / tr["+str(i)+"] / td["+str(j)+"]").text

        print(ele, end="       ")
    print()