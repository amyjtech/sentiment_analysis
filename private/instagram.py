# Used for general errors
import sys
# Writing to csv file
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
-------------------
x Scrape comments under post
x Click '+' and load all comments
x Scrape indefinitely/user specified amount
x Save comments to csv file
x Save data in an easy to manage way
o Scrape specific time/dates
o Scrape replies to comments
o Read/identify comments scraped so they are not scraped again
o Save URLs scraped
o Scrape Hashtags
Errors:
! Not identifying header logic and adding header again to comments
    - Manually removed 19/20 'headers'
    
! Struggling with writing data to .csv easily/clean
    - delimiter = | to prevent rows written being str and "" or written as s,t,r
    - manually changed header from insta_name|insta_text to insta_name,insta_text for pandas
    
! Verified users have an extra column, need to handle
    omengq,Verified,ManiLa,5d1 likeReply
'''
# Going to the Instagram we want to scrape
driver.get("https://www.instagram.com/rideclutch")

# Setting variables
# recent_post = identifies element used to select/click on posts
# wait = lets driver know to wait 10secs for element to be found or throw an error -- used for expected_conditions or EC
recent_post = driver.find_element_by_class_name("_9AhH0")
wait = WebDriverWait(driver, 10)

# Telling driver to wait until element appears
insta_profile = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_9AhH0")))

# Click on element once it appears
recent_post.click()

# list for collecting urls


# Loads all the comments on an image
def insta_load_comment():
    click = 0
    print(f"Loading Comments: {driver.current_url}")
    
    # Endless click
    while click < 20:
        try:
            # Waits until comment_body loads before cont
            comment_body = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk")))
            
            # Setting variable for '+' button to load more comments
            load_more = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button")
            
            # Action to click the '+' button
            load_more.click()
            click = click + 1
            print(f"Click {click} successful")
            # Prevent detection for scraping
            time.sleep(3) 
            
        # Let user know they have reached end of comments
        except exceptions.NoSuchElementException as e:
            print(f"End of comments")
            break
        
# Clicks on the right arrow to navigate to the next page
def insta_click_right():
    r_arrow = driver.find_element_by_link_text("Next")
    r_arrow.click()

# Saves comments after they have been loaded
def insta_save_comment():  
    # CSV File
    insta_file = "insta_comments.csv"
    
    # Setting scraped_posts to 0 so we can set an amount
    scraped_posts = 0
    
    # Setting amount of posts to scrape
    while scraped_posts < 30:
  
        try:            
            comment_body = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk")))

            comment = comment_body.find_elements_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul")
            print(f"Scraping: {driver.current_url}")
            csv_header=False
            # Opening CSV file, 'a+' appends and reads, encoding utf-8 prevents errors and saves emojis, newline='' prevents \n spacing betwen rows
            with open(insta_file, 'a+',encoding='utf-8',newline='') as csvfile:          
                # Creating CSV Writer
                insta_csv = csv.writer(csvfile,delimiter="|")
                
                # # TO DO: NOT FUNCTIONING
                # insta_header = ['insta_name','insta_text','insta_time','no_reply']
                
                # if not csv_header:
                #     insta_csv.writerow(insta_header)
                #     csv_header=True
                # # END TO DO: NOT FUNCTIONING
                    
                # 'comment' is a list so we are iterating through
                for single in comment:
                    # converting to text
                    single = single.text
                    # no_comma removes commas from the comments, preventing errors in the future when uploading to pandas df
                    no_comma = single.replace(',','')
                    # Removes the \n at the end and replaces with ,
                    line = [no_comma.replace('\n', ',')]
                    
                    print(line)
                    # Saving each line to csv, since it is a list prevents python seperating each char (e,x,a,m,p,l,e)
                    insta_csv.writerow(line)

                # Adding scraped posts and letting user know it was successful
                scraped_posts = scraped_posts + 1 
                print(f"Scraped {len(comment)} comment(s) from {driver.current_url}\nScraped {scraped_posts} post(s)")
                
                # Clicking to the next comment and loading them, starting process over until clicks reached
                insta_click_right()
                insta_load_comment()
        # Except handling will print system error, let user know scrape was not complete, and close driver/system
        except:
            print(sys.exc_info())
            print(f"\nScrape incomplete\nScraped {scraped_posts} posts")
            driver.quit()
            sys.exit()
    # Let user know posts were scraped
    else:
        print(f"Scraped {scraped_posts} posts\nInstagram scrape complete")
        driver.quit()

# These 2 functions run the instagram scraper
insta_load_comment()
insta_save_comment()