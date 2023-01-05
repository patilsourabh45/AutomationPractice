
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://facebook.com")

## Absoult path (full path) : c:/Credence/Python/FacebookLoginTest.png
driver.get_screenshot_as_file("C:\\tmp\\Class\\FacebookLoginTest.png")

## relative path : with respect to current working directory.. where your executing script is located
driver.get_screenshot_as_file("Screenshots\\FacebookLoginTest.png")

driver.get_screenshot_as_file("..\\FacebookLoginTest.png")  ##  1 parent folder up by ..

driver.get_screenshot_as_file("..\\..\\FacebookLoginTest.png")  ##  2 parent folder up by ..



## another method for screenshot

driver.save_screenshot("FacebookTestWithoutExt")        ## relative path
## here you can also use both path absolute and relative path



