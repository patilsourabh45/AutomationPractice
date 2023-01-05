
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

inputEmail = driver.find_element(By.ID, 'email')      # To find webcontrol whoes ID is email
inputEmail.send_keys("sagar@credence.com") ## to write text into textbox

inputPass = driver.find_element(By.ID, 'pass')    ## # To find webcontrol whoes ID is pass
inputPass.send_keys("sagar@123") ## to write text into textbox

###btnLogin = driver.find_element(By.ID, 'u_0_5_Xr')    ## # To find webcontrol whoes ID is pass
btnLogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')    ## # To find webcontrol whoes ID is pass
btnLogin.click()        ## click on button

## ID - value will be unique on page
## name - Value can be duplicated