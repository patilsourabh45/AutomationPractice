from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()

print("current window handles",driver.current_window_handle)
print("Window Handles", driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])
print("current window handles",driver.current_window_handle)
text = driver.find_element(By.CSS_SELECTOR,"body > div > h3").get_attribute("innerHTML")
print(text)