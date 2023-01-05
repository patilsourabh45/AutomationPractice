from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/Testing/PythonPractice/AutomationPractice/SampleHTMLFile.html")

btnLogin = driver.find_element(By.ID, "btn")
print("Value is:", btnLogin.get_attribute("value"))