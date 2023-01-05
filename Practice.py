# import time
#
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://facebook.com")
# driver.maximize_window()
#
# print("title", driver.title)
# print("url", driver.current_url)
# driver.get("https://amazon.com")
# driver.back()
# time.sleep(5)
# driver.forward()

# inputEmail=driver.find_element(By.NAME,"email")
# inputEmail.send_keys("patilsourabh45@gmail.com")
#
# inputPass=driver.find_element(By.NAME,"pass")
# inputPass.send_keys("12345")
#
# loginBtn=driver.find_element(By.NAME,"login")
# loginBtn.click()
#
# inputEmail=driver.find_element(By.ID,"email")
# inputEmail.send_keys("patilsourabh45@gmail.com")
#
# inputPass=driver.find_element(By.ID,"pass")
# inputPass.send_keys("12345")
#
# loginBtn=driver.find_element(By.ID,"u_0_5_IE")

# inputEmail=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
# inputEmail.send_keys("patilsourabh45@gmail.com")
#
# inputPass=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
# inputPass.send_keys("1234")
#
# loginBtn=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
# loginBtn.click()
#
# driver.close()
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/Testing/PythonPractice/AutomationPractice/SampleHTMLFile.html")

driver.maximize_window()

inputElement = driver.find_element(By.ID, "text")
print("Attribute",inputElement.get_attribute("disabled")) #True

inputElement = driver.find_element(By.ID, "text")
print("isEnabled", inputElement.is_enabled())  #False

inputElement = driver.find_element(By.ID, "text1")
print("isEnabled", inputElement.is_enabled())   #True

inputElement = driver.find_element(By.ID, "text2")
print("isEnabled", inputElement.is_enabled())

inputElement = driver.find_element(By.ID, "text")
print("isDisplayed", inputElement.is_displayed()) #True

inputElement = driver.find_element(By.ID, "text1")
print("isDisplayed", inputElement.is_displayed())

inputElement = driver.find_element(By.ID, "text2")
print("isDisplayed", inputElement.is_displayed())

inputElement = driver.find_element(By.ID, "text3")
print("isDisplayed", inputElement.is_displayed())


inputElement = driver.find_element(By.ID, "text")
print("isSelected", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "text1")
print("isSelected", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "text2")
print("isSelected", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "text3")
print("isSelected", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "checkbox")
print("isSelectedCheckbox", inputElement.is_selected()) #True

inputElement = driver.find_element(By.ID, "checkbox1")
print("isSelectedCheckbox1", inputElement.is_selected()) #False



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()     # Creating class object of Chrome
# driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
#
# driver.execute_script('window.scrollBy(0,3000)')
# # driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
# # driver.execute_script('window.scrollTo(0,0)')
# # driver.execute_script('window.scrollBy(0,-3000)')
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
#
# ele = driver.find_element(By.XPATH, "//*[@id='Languages_influenced_by_Python']")
# driver.execute_script("arguments[0].scrollIntoView()", ele)

