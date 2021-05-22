from selenium import webdriver
# This allows you to interact with webpage, type/enter text, etc.
from selenium.webdriver.common.keys import Keys
# Needed for using Chrome profile
from selenium.webdriver.chrome.options import Options

# Used for Explicit Waits
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs

# Used for sleep
import time

'''
Runs/opens the desired Instagram page

https://www.instagram.com/rideclutch

https://www.instagram.com/explore/tags/rideclutch/
'''

options = webdriver.ChromeOptions()
# Was getting an encoding error.  Passing r"" creates a raw string preventing errors when locating the file
options.add_argument("user-data-dir=C:\\Users\\AmySmith\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# Prevents windows error
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# This prevents the browser from closing immediately after running
options.add_experimental_option("detach", True)
# Variable = path to the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# The driver is what navigates the page, I chose Chrome
driver = webdriver.Chrome(PATH, options=options)

# driver.get("webpage") will bring up any page you need
driver.get("https://www.instagram.com/rideclutch")




'''
1. Need to save the 'https://www.instagram.com/p/' url for each post
    - Able to set limit of URL's collected
        o Create a for loop for this and set a max
    - Access comments [username, comment, url to profile]
        o "EtaWk" class is for comment section
        P9YgZ?
    - Access date/time post was created
        o
'''

# Clicks on the first/most recent post
prev = driver.find_element_by_class_name("_9AhH0")
prev.click()

# Sleeping lets the page to load before continuing
# Having problems with explicit wait
time.sleep(3)

# Gathers the URL of the current page
print(driver.current_url)

# Load all comments by clicking button
load_more = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button")

load_more.click()


# Clicks on the right arrow to navigate to the next page
# r_arrow = driver.find_element_by_link_text("Next")
# r_arrow.click()