import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

time.sleep(3)
## page scroll by pixel
driver.execute_script('window.scrollBy(0, 3000)')

time.sleep(3)
## page scroll by or upto sepcific element
ele = driver.find_element(By.ID, 'Programming_examples')
driver.execute_script("arguments[0].scrollIntoView()", ele)

## scroll till the end of page
time.sleep(3)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(3)
## page scroll upside by pixel
driver.execute_script('window.scrollBy(0, -3000)')

# time.sleep(3)
# ## page scroll to top by pixel
# driver.execute_script('window.scrollBy(0, -document.body.scrollHeight)')

time.sleep(3)
## page scroll to top by pixel
driver.execute_script("window.scrollTo(0, 0)")


#### IMP - scrollBy vs scrollTo
