
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\sss2327\AppData\Local\Programs\Python\Python39\chromedriver.exe")

driver.get("https://facebook.com")  ## open website or url
driver.maximize_window()
print("Page title : ", driver.title)
print("Current URL : ", driver.current_url)

driver.get("https://amazon.com")  ## open website or url
driver.maximize_window()
print("Page title : ", driver.title)
print("Current URL : ", driver.current_url)
#
# driver.close()      #close current window of browser
# driver.quit()   #quits all windows opened by our script... Closes the browser and shuts down the ChromeDriver executable that is started when starting the ChromeDriver

## if you have method which doesnt require any arguements, and return some type of value
## make it as property by using @property decorator..
## when you are calling it no need to provide bracket like method call and use like attribute





### For latest version

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s=Service(r"C:\Users\sss2327\AppData\Local\Programs\Python\Python39\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get('https://www.google.com')




