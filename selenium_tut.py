from selenium import webdriver
# This allows you to interact with webpage, type/enter text, etc.
from selenium.webdriver.common.keys import Keys
# Needed for using Chrome profile
from selenium.webdriver.chrome.options import Options

# Used for Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# Was getting an encoding error.  Passing r"" creates a raw string preventing errors when locating the file
options.add_argument("user-data-dir=C:\\Users\\AmySmith\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# Variable = path to the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# The driver is what navigates the page, I chose Chrome
driver = webdriver.Chrome(PATH, options=options)

# driver.get("webpage") will bring up any page you need
driver.get("https://www.instagram.com")

# Provides the title of the webpage
print(driver.title)

# driver.close() closes the current tab, not the entire browser
# driver.close()

# driver.quit() closes the entire browser
# driver.quit()

# Search by ID, Name, Class
# Selenum picks up the first element so ID is best

# search = driver.find_element_by_name("q")

# search.send_keys("Python")
# # The code below hits the 'enter' key
# search.send_keys(Keys.RETURN)

'''
Exolicit Waits + Finding results
'''
# Explicit Wait - allows the page to load before going forward
# try:
#     body = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "rso"))
#     )
#     print(body.text)

# This should allow you to find results by name loop thru and show them
# Not working w/ Google bc of class names
result_title = body.find_elements_by_class_name("yuRUbf")
for result in result_title:
    header = result.find_elements_by_class_name("IsZvec")
    
print(header.text)
    
# except:
#     print("!! Selenium force close")
#     driver.quit()