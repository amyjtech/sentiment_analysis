import sys
import csv

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
-------------------
x Scrape comments under post
o Scrape all comments under post
    ! Only scrapes 7 comments per post
    x Fixed Error: (<class 'TypeError'>, TypeError("'NoneType' object is not iterable")
o Scrape indefinitely/user specified amount
x Save data in an easy to manage way

o Scrape specific time/dates
o Scrape replies to comments
o Read/identify comments scraped so they are not scraped again
o Save URLs scraped

Errors:
! Scraping the same posts, logic to save post_url in list not functional
! Only scrapes 7 comments per post
! Not identifying header logic and adding header again to comments
    - Manually removed 'headers'
'''
def fb_save_comments():
    print("Starting FB Scrape")
    try:
        # Searching posts in 'username', and selecting their comments
        for post in get_posts('rideclutch',options={"comments": True}):
            # Setting post url to variable for use
            post_url = post['post_url']
            
            # Selenium grabs post url and goes to page
            driver.get(post_url)

            # Wait for div with comment section to load before scraping to avoid errors
            comment_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#facebook ._-kb div")))
                

            fb_file = "fb_comments.csv"
                
            # Opening CSV file, 'a+' appends and reads, encoding utf-8 prevents errors and saves emojis, newline='' prevents \n spacing betwen rows
            with open(fb_file, 'a+',encoding='utf-8',newline='') as csvfile:          
                # Creating CSV Writer
                fb_csv = csv.writer(csvfile,delimiter='|')
                
                fb_header = ['fb_name','fb_text','fb_time']
                
                if 'fb_name' in fb_file:
                    pass
                else:
                    fb_csv.writerow(fb_header)
                # Accessing the comments data under the post which is a list with a dict inside
                comments_data = post['comments_full']

                # Accessing the dict within the list and specific comment data
                for comment in comments_data:
                    # Setting variables
                    commenter_name = comment.get('commenter_name')
                    comment_text = comment.get('comment_text')
                    comment_time = comment.get('comment_time')

                    # Setting up list for file
                    fb_comments = [commenter_name, comment_text, str(comment_time)]
                    
                    fb_csv.writerow(fb_comments)
                # Stating scrape of post with URL complete & counting comments scraped

                print(f"Scraped: {len(comment)} comments from {post_url}")
                # Force slowing scrape between pages to avoid detection
                time.sleep(20)
    # Stating scrape was complete and successful
    except TypeError as e:
        print(f"Unable to scrape {post_url}\n{e}\nContinuing FB scrape")

            
    print("Facebook Scrape Complete\n")
    driver.quit()
          
fb_save_comments()