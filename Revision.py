from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

print(driver.title)

element = driver.get_screenshot_as_file("ScreenShots/f1.jpg")
