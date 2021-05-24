from selenium import webdriver
# This allows you to interact with webpage, type/enter text, etc.
from selenium.webdriver.common.keys import Keys
# Needed for using Chrome profile
from selenium.webdriver.chrome.options import Options

from selenium.common import exceptions

# Used for Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs

# Used for sleep
import time

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

'''
INSTAGRAM SCRAPER

Runs/opens the desired Instagram page

https://www.instagram.com/rideclutch
    x Clicking and grabbing comments from posts by clicking on most recent post

https://www.instagram.com/explore/tags/rideclutch/
    o Hashtags are not functional -- stretch

1. Need to save the 'https://www.instagram.com/p/' url for each post
    - Able to set limit of URL's collected
        x Create a for loop for this and set a max
    x Access comments [username, comment, days posted, reply/if any replies]
    - Access date/time post was created
        o Need to access on page
'''

# driver.get("webpage") will bring up any page you need
driver.get("https://www.instagram.com/rideclutch")

# Clicks on the first/most recent post
prev = driver.find_element_by_class_name("_9AhH0")
prev.click()

# Sleeping lets the page to load before continuing
# Having problems with explicit wait
time.sleep(3)

# Gathers the URL of the current page
def get_url():
    print(driver.current_url)

# Loads all the comments on an image
'''
!! Need to handle when button disappears/end of comments
'''
def insta_load_comment():
    click = 0

    try:
        # Load more comments by clicking button
        load_more = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button")
        # Action to click the button
        load_more.click()
        click = click + 1
        print(f"Click {click} successful")    
    except exceptions.InvalidSelectorException as e:
        print(f"{e}")
    
    while click < 3:
        try:
            time.sleep(3)
            load_more.click()
            click = click + 1
            print(f"Click {click} successful")
            
        # Will receive an error unless this expection is in place
        # Retries clicking the button
        except exceptions.StaleElementReferenceException as e:
            print(f"\n{e}\nAttempting to access again")
            load_more = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button")
             # Action to click the button
            load_more.click()
            click = click + 1
            print(f"Click {click} successful") 
    
def insta_save_comment():
    # Appending the comments to instagram_comments.txt file
    save_insta = open("instagram_comments.txt", "a", encoding="utf-8")
                
    comment_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk")))
    
    comment = comment_body.find_elements_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul")
    
    # Reading through comments and writing to file
    # Each instance is seperated by \n
    for x in comment:        
        save_insta.write(x.text)
        save_insta.write("/")

# Clicks on the right arrow to navigate to the next page
def insta_click_right():
    r_arrow = driver.find_element_by_link_text("Next")
    r_arrow.click()