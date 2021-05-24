import sys

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

# Used for FB scraper
from facebook_scraper import get_posts

# Used for sleep
import time

# Datetime - FB scraper
import datetime

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
FACEBOOK SCRAPER

https://www.facebook.com/rideclutch
'''
def fb_save_comments():
    try:
        # Searching posts in 'username', and selecting their comments
        for post in get_posts('rideclutch',options={"comments": True}):
            # Setting post url to variable for use
            post_url = post['post_url']
            # Appending the comments to instagram_comments.txt file
            save_fb = open("fb_comments.txt", "a", encoding="utf-8")
            
            # Selenium grabs post url and goes to page
            driver.get(post_url)

            # Wait for div with comment section to load before scraping to avoid errors
            comment_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#facebook ._-kb div")))
     
            # Let user know which URl that is being scraped
            print(f"Scraping: {driver.current_url}")

            # Accessing the comments data under the post which is a list with a dict inside
            comments_data = post['comments_full']

            # Accessing the dict within the list and specific comment data
            for comment in comments_data:
                # Setting variables
                commenter_name = comment.get('commenter_name')
                comment_text = comment.get('comment_text')
                comment_time = comment.get('comment_time')

                # Setting up list for file
                comments = [commenter_name, comment_text, str(comment_time)]

                # Reading to file
                for single in comments:
                    save_fb.write(single)
                    save_fb.write("/")
                
                save_fb.write("\n")
            # Stating scrape of post with URL complete
            fb_scraped_list.append(driver.current_url)
            print(f"Scraped: {driver.current_url}")

        # Stating scrape was complete and successful
        print("Facebook Scrape Complete\n")
        driver.quit()
    except:
        # Print error
        print(sys.exc_info())
        # Let user know scrape was incomplete
        print("Facebook Scrape Incomplete\n")
        driver.quit()
          
fb_save_comments()